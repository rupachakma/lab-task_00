
from django.urls import path

from app import views

urlpatterns = [
    path('', views.signuppage,name="signuppage"),
    path('loginpage', views.loginpage,name="loginpage"),
    path('homepage', views.home, name="homepage"),
    path('addstudentpage', views.addstudentpage, name="addstudentpage"),
    path('editPage<int:id>', views.editPage, name="editPage"),
    path('updatestudentpage', views.updatestudentpage, name="updatestudentpage"),
    path('deletestudent<int:id>', views.deletestudent, name="deletestudent"),
]
