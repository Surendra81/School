from django.contrib import admin
from .models import School, Question, Choice
# Register your models here.

admin.site.register(School)
admin.site.register(Question)
admin.site.register(Choice)