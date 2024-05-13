from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

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
    subject = models.TextField('Subject',max_length=100) #предмет
    link_project = models.CharField(max_length=200)
    link_annex = models.CharField(max_length=200)
    link_review = models.CharField(max_length=200)
    teacher_point = models.BooleanField() #доп балл от руководителя
    date = models.DateField() #дедлайн


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.theme


    # def get_absolute_url(self):
    #     """
    #     Returns the url to access a particular book instance.
    #     """
    #     return reverse('book-detail', args=[str(self.id)])