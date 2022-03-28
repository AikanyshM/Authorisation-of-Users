from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth_app.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('logout/', auth_views.LogoutView.as_view()),
    path('password_reset/',auth_views.PasswordResetConfirmView.as_view(template_name='confirm_reset.html')),
    path('change_password/', auth_views.PasswordChangeDoneView.as_view(template_name='confirm_change.html')),

]
