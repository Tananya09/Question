from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name_department = models.CharField(max_length=255)
    password = models.CharField(max_length=5 , unique=True)
    STATUS = (('Online','Online'),('Offline','Offline'))
    status = models.CharField(max_length = 10, choices = STATUS)
    def __str__(self):
        return self.name_department

class UserInformation(models.Model):
    department = models.ForeignKey(Department , on_delete = models.PROTECT , default = "CenterID")
    ident_number = models.CharField(max_length=255 , blank=True)
    name_lastname = models.CharField(max_length=255 , blank=True)
    SEX = (('Male','Male'), ('Female','Female'))
    sex = models.CharField(max_length=10 , choices=SEX , blank=True)
    age = models.IntegerField(blank=True) 
    create_date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.name_lastname


class Group(models.Model):
    name_group = models.CharField(max_length=255)
    def __str__(self):
        return self.name_group

class Category(models.Model):
    name_category = models.CharField(max_length=255)
    group = models.ForeignKey(Group , on_delete = models.PROTECT)
    def __str__(self):
        return self.name_category

class Question(models.Model):
    category = models.ForeignKey(Category , on_delete = models.PROTECT , default = "Category")
    question = models.TextField(max_length=500)
    number = models.IntegerField(unique=True)
    score = models.IntegerField()
    def __str__(self):
        return "(%s) %s" % (self.number,self.question)


class Key(models.Model):
    question = models.ForeignKey(Question , on_delete = models.CASCADE)
    TYPE = (('Scale 1','Scale 1'),('Scale 2', 'Scale 2'),('Scale 3','Scale 3'))
    scale = models.CharField(max_length=10,choices=TYPE)
    q2_number = models.IntegerField(default='0')
    OPTION = (('Yes','Yes'), ('No','No'))
    key = models.CharField(max_length=10,choices=OPTION)
    

class Answer(models.Model):
    user = models.ForeignKey(UserInformation , on_delete = models.PROTECT , default = "User")
    question = models.ForeignKey(Question , on_delete = models.CASCADE,null=True)
    ans = models.CharField(max_length=20 , null=True)

class Score(models.Model):
    user = models.ForeignKey(UserInformation , on_delete = models.PROTECT , default = "User")
    group = models.ForeignKey(Group , on_delete = models.PROTECT)
    score = models.IntegerField()    