from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('templates/NGO1stpage/',views.home),
    path('templates/NGOAboutus/',views.about),
    path('templates/NGOissuespage/',views.issues),
    path('templates/NGOFund/',views.fund),
    path('templates/NGOCareers/',views.career),
    path('templates/NGOContactus/',views.contactus),
    path('templates/NGOThankyoupage/',views.thankyou),
    path('templates/NGOVolunteer/',views.volunteer),
    path('templates/NGOAdoptpage/',views.adopt),
    path('templates/SOS/', views.sos_submit),
    path('templates/NGOAdoptform/',views.adoption),
    path('templates/NGODonatepage/',views.donate),
    path('templates/NGOAdoptreqpage/',views.adoptreq)
]