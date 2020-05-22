from django.urls import path
from .views import SchoolView
from .views import SchoolCreate
app = 'firstapp'

urlpatterns = [
    path('',SchoolView.as_view(), name = 'school_view'),
    path('create/',SchoolCreate.as_view(), name = 'create_school'),

]
