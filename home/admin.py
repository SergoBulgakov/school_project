from django.contrib import admin

# Register your models here.
from .models import Profile, Project, Project_defense, Content_point

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Project_defense)
admin.site.register(Content_point)