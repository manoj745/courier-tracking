from django import contrib
from django.contrib import admin
from django.urls import path,include
from  .import views 
from django.contrib.auth import views  as auth_views
urlpatterns = [
      

       #path("login1/", views.user_login, name='login'),
       # path("login/", auth_views.LoginView.as_view(), name='login'),
        # path("logged_out/", auth_views.LogoutView.as_view(), name='logout'),
       #password change
      # path("password_change/", auth_views.PasswordChangeView.as_view(), name='password_change'),
       #path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
       #reset password
      # path("password_reset/", auth_views.PasswordResetView.as_view(), name='password_reset'),
      # path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
       ##path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
path('', views.dashboard, name='dashboard'),
path('',include('django.contrib.auth.urls')),
path("register/", views.register, name='register'),
path("edit/", views.edit, name='edit'),
path("index/", views.index, name='app'),
path("about/", views.about, name='about'),
path("services/", views.services, name='services'),
path("contact/", views.contact, name='contact'),
path("order/", views.order, name='order'),
path("submit/", views.submit, name='submit'),
path("appointment/", views.appointment, name='appointment'),
path("search/", views.search, name='search'),
]
