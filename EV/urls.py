from django.contrib import admin
from django.urls import path, include
import accounts.views
import Main.views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.views.index, name='index'),
    path('new/', Main.views.new, name="new"),
    path('registration/register/', accounts.views.register, name="register"),
    path('registration/', include('django.contrib.auth.urls')),
    path('registration/login/', auth_views.LoginView.as_view(), {'template_name':'registration/login.html'}, name="login"),

]
