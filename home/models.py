from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    patronymic = models.CharField(max_length=30, null=True)
    school_class = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=True)
    olympiad = models.BooleanField(null=True)
    achievment = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Project(models.Model):
    
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4) #id проекта

    student = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="Student") #связь с учеником
    teacher = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="Teacher") #связь с научным руководителем

    theme = models.CharField(max_length=200) #тема проекта
    subject = models.CharField(max_length=100) #предмет
    link_project = models.CharField(max_length=200)
    link_annex = models.CharField(max_length=200)
    link_review = models.CharField(max_length=200)
    teacher_point = models.BooleanField() #доп балл от руководителя
    date = models.DateField() #дедлайн


    def __str__(self):
        return self.theme
    

class Project_defense(models.Model):
    
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4) #id 

    project = models.ForeignKey(Project,on_delete=models.SET_NULL,null=True,related_name="Project_project_defense") #связь с проектом
    exspert1 = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="Expert1_project_defense") 
    exspert2 = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="Expert2_project_defense") 
    exspert3 = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="Expert3_project_defense") #связь с 3 экспертами

    date = models.DateField() #дата защиты
    
    measure1exspert1 = models.SmallIntegerField # оценка 1 критерия 1 экспертом
    measure1exspert2 = models.SmallIntegerField # оценка 1 критерия 2 экспертом
    measure1exspert3 = models.SmallIntegerField # оценка 1 критерия 3 экспертом
    measure2exspert1 = models.SmallIntegerField # оценка 2 критерия 1 экспертом
    measure2exspert2 = models.SmallIntegerField # оценка 2 критерия 2 экспертом
    measure2exspert3 = models.SmallIntegerField # оценка 2 критерия 3 экспертом
    measure3exspert1 = models.SmallIntegerField # оценка 3 критерия 1 экспертом
    measure3exspert2 = models.SmallIntegerField # оценка 3 критерия 2 экспертом
    measure3exspert3 = models.SmallIntegerField # оценка 3 критерия 3 экспертом
    link_call = models.CharField(max_length=200) # ссылка на конференцию


    def __str__(self):
        return self.project.theme


    # def get_absolute_url(self):
    #     """
    #     Returns the url to access a particular book instance.
    #     """
    #     return reverse('book-detail', args=[str(self.id)])

class Content_point(models.Model):
    
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4) #id проекта

    project = models.ForeignKey(Project,on_delete=models.SET_NULL,null=True,related_name="Project_content_points") #связь с проектом
    exspert = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="Expert_content_points") #связь с экспертом

    date = models.DateField() #дата оценивания

    measure1 = models.SmallIntegerField
    measure2 = models.SmallIntegerField
    measure3 = models.SmallIntegerField
    measure4 = models.SmallIntegerField
    measure5 = models.SmallIntegerField
    measure6 = models.SmallIntegerField
    measure7 = models.SmallIntegerField
    measure8 = models.SmallIntegerField
    measure9 = models.SmallIntegerField #оценки по 9 критериям

    link_anti_plagiarism = models.CharField(max_length=200) # ссылка на антиплагиат


    def __str__(self):
        return self.project.theme