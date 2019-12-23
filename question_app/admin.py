from django.contrib import admin
from question_app.models import Answer, Category, Department, Group, Key, Question, UserInformation, Score

# Register your models here.
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user','ans','question')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_category', 'group')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name_department', 'status')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name_group',)

class KeyAdmin(admin.ModelAdmin):
    list_display = ('question','scale', 'key','q2_number')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','number','category','question')

class UserInformationAdmin(admin.ModelAdmin):
    list_display = ('id','name_lastname','department','ident_number')

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user','group','score')


admin.site.register(Answer,AnswerAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Key,KeyAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(UserInformation,UserInformationAdmin)
admin.site.register(Score,ScoreAdmin)