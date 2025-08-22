from django.urls import path,include
from . import views,user_views,advisor_views

urlpatterns = [
path('',views.home,name="home"),
path('contact/',views.contact_us,name='contact_us'),
path('about/',views.about_us,name='about_us'),
path('feedback/',user_views.user_feedback,name='user_feedback'),
path('login/',user_views.user_login,name='user_login'),
path('registration/',user_views.user_registration,name='user_registration'),
path('user_home/',user_views.user_home,name='user_home'),
path('user_logout/',user_views.user_logout,name='user_logout'),
path('views_services/',views.views_services,name='views_services'),
path('views_advisors/',views.views_advisors,name='views_advisors'),
path('user_advisors/',user_views.user_advisors,name='user_advisors'),
path('upload_document/',user_views.upload_document,name='upload_document'),
path('user_edit_profile/',user_views.user_edit_profile,name='user_edit_profile'),
path("advisor_login/",advisor_views.advisor_login,name='advisor_login'), 
path("advisor_home/",advisor_views.advisor_home,name='advisor_home'), 
path("download_document/",advisor_views.download_document,name='download_document'),
path('advisor_logout/',advisor_views.advisor_logout,name='advisor_logout')
]


   