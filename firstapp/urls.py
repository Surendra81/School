from django.urls import path
from . import views
app = 'firstapp'

urlpatterns = [
    # path('',views.SchoolView.as_view(), name = 'school_view'),
    # path('create/',SchoolCreate.as_view(), name = 'create_school'),
    path('index/',views.index, name = 'index-view'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
