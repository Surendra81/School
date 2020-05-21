from django.urls import path
from .views import SchoolView
app = 'firstapp'

urlpatterns = [
    path('',SchoolView.as_view(), name = 'school_view'),
]
