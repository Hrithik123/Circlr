from django.urls import path

from . import views
app_name = "polls"
urlpatterns = [
    path('',views.index,name="index"),
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name="vote"),
    path('questions/', views.questions , name='questions'),
    path('choices/', views.choices, name='choices'),
    path('savechoices/', views.savechoices, name='savechoices'),
    path('sendmail/',views.endpoll,name='endpoll'),
]