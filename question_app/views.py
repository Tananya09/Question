from django.shortcuts import render , redirect
from django.views.decorators.csrf import csrf_protect
from question_app.models import Department, UserInformation, Question, Answer,Key,Group,Score
from django.utils import timezone
# Create your views here.



@csrf_protect
def password(request):
    if request.method == 'POST':
        ps = request.POST.get('password')
        department = Department.objects.all().filter(password = ps)
        status = department[0].status
        if str(status) == 'Online' :
            try:
                dep = department[0]
                return redirect('information_view', pk = department[0].id )
            except IndexError:
                pass
        else:
            pass

    return render(request , 'password.html')
    

def information_view(request, pk):

    name_department = Department.objects.get(id = pk)
    if request.method == 'POST':
        dp = name_department 
        identcode = request.POST.get('identcode')
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        print(dp , identcode ,name ,sex ,age)
        info_obj = UserInformation(
            department = name_department,
            ident_number = identcode,
            name_lastname = name,
            sex = sex,
            age = age
        )
        try:
            info_obj.save()
            return redirect('explanation_view', pk = info_obj.id )
        except:
            pass


    return render(request , 'information.html',{'dp' : name_department })


def question_view(request, pk , n):
    user = UserInformation.objects.get(id = pk)
    q = Question.objects.filter(number = n)
    all_q = Question.objects.all()
    num_q = len(all_q)
    nxt = True 
    prv = True 
    if n == 1:
        prv = False
    if n == num_q:
        nxt = False

    if request.POST:
        ans = request.POST.get('ans')
        print(ans)
        ans_obj = Answer(
            user = user , 
            question = q[0] , 
            ans = ans
        )
        a = Answer.objects.filter(user = user , question = q[0])
        size = len(a)
        if size==0 :
            ans_obj.save()
        else:
            a[0].ans = ans
            a[0].save()
            
        if 'next' in request.POST:
            n = n+1
            
            return redirect('question_view', pk = pk , n=n)
        if 'prev' in request.POST:
            n = n - 1
            return redirect('question_view', pk = pk , n=n)

        if 'final' in request.POST:
            return redirect('final', pk= pk)


    return render(request , 'question.html',{'questions' : q[0] , 'nxt' : nxt , 'prv' : prv})


def explanation_view(request, pk):
    if request.method == 'POST':
        ac = request.POST.get('accept')
        n=1
        print(ac)
        if ac == 'on':
            
            return redirect('question_view', pk = pk , n=n)
        else:
            pass
        
    return render(request , 'explanation.html',{'pk' : pk })


def dashboard_department(request):
    dp = Department.objects.all()
    return render(request ,'department.html',{'dp':dp})


def dashboard_user(request,pk):
    dp = Department.objects.filter(id = pk)
    user = UserInformation.objects.filter(department = dp[0])
    return render(request ,'user.html',{'user':user , 'dp':dp[0]})


def result_user(request,pk):
    user = UserInformation.objects.get(id=pk)
    ans = Answer.objects.filter(user = user)
    arr_group = create_score_group(user)
    arry_count = cal_ans_type(pk)
    count_yes = arry_count[0]
    count_no = arry_count[1]
    count_none = arry_count[2]
    cal_score_group(ans,user)
    
    score = Score.objects.filter(user = user).order_by('group')

    return render(request ,'result.html',{'u':user,'yes':count_yes , 'no' : count_no , 'none' : count_none , 'group': arr_group , 'score' : score})



def cal_score_group(ans,user):
    for a in ans:
        key = Key.objects.filter( question= a.question)
        k = key[0]
        
        if a.ans is None:
            print("0")
        else:
            if k.scale == 'Scale 1':
                
                if a.ans == k.key:
                    s = Score.objects.filter(user = user, group = k.question.category.group)
                    s = s[0]
                    score_old = s.score
                    score_new = score_old + 1
                    s.score = score_new
                    s.save()
                    print("+1")
                else:
                    print("0")

            elif k.scale == 'Scale 2':
                q2 = k.q2_number
                question2 = Question.objects.filter(number = q2)
                question2 = question2[0]
                ans2 = Answer.objects.filter(user = user , question = question2)
                ans2 = ans2[0]
                if a.ans == ans2.ans:
                    s = Score.objects.filter(user = user, group = k.question.category.group)
                    s = s[0]
                    score_old = s.score
                    score_new = score_old + 1
                    s.score = score_new
                    s.save()
                    print("+1")
                else:
                    print("0")

            elif k.scale == 'Scale 3':
                q2 = k.q2_number
                question2 = Question.objects.filter(number = q2)
                question2 = question2[0]
                ans2 = Answer.objects.filter(user = user , question = question2)
                ans2 = ans2[0]
                if a.ans == ans2.ans:
                    print("0")
                else:
                    s = Score.objects.filter(user = user, group = k.question.category.group)
                    s = s[0]
                    score_old = s.score
                    score_new = score_old + 1
                    s.score = score_new
                    s.save()
                    print("+1")



def create_score_group(user):
    arr_group = []
    group = Group.objects.all()
    for g in group:
        arr_group.append(g.name_group)
        s = Score.objects.filter(user = user, group__name_group = g.name_group)
        if len(s) == 0:
            s_obj = Score(user = user, group = g , score = 0)
            s_obj.save()
        else:
            s = s[0]
            s.score = 0
            s.save()

    return arr_group

def final(request,pk):
    arry_count = cal_ans_type(pk)
    count_yes = arry_count[0]
    count_no = arry_count[1]
    count_none = arry_count[2]
    return render(request ,'final.html',{'yes':count_yes , 'no' : count_no , 'none' : count_none})


def cal_ans_type(pk):
    user = UserInformation.objects.get(id=pk)
    ans = Answer.objects.filter(user = user)
    yes = 0
    no = 0
    none = 0
    for a in ans:
        if a.ans is None:
            none += 1
        elif a.ans == 'Yes':
            yes += 1 
        elif a.ans == 'No':
            no += 1
        else:
            pass

    arry_count = [yes,no,none]
    
    return arry_count



