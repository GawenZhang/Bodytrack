from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)
    email = models.EmailField(blank=True, null=True)
    age = models.IntegerField()

    registration_date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=gender_choices, blank=True, null=True)

class Department(models.Model):
    title = models.CharField(max_length=16)


# # #新建数据########  insert into
# Department.objects.create(title="销售部")
# UserInfo.objects.create(name="wupeiqi",password="123",age=19)

