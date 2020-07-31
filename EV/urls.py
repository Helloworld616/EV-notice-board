from django.contrib import admin
from django.urls import path, include
import accounts.views
import Main.views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.views.index, name='index'),
    path('new/', Main.views.new, name="new"),
    path('registration/register/', accounts.views.register, name="register"),
    path('registration/', include('django.contrib.auth.urls')),
    path('registration/login/', auth_views.LoginView.as_view(), {'template_name':'registration/login.html'}, name="login"),
    path('index/<int:pk>', Main.views.index, name = "index"),
    path('detail/<int:pk>', Main.views.detail, name = "detail"),
    path('edit/<int:pk>', Main.views.edit, name="edit"),
    path('detail/<int:pk>/delete', Main.views.delete, name="delete"),
    path('detail/<int:pk>/comment/<int:comment_pk>/delete/', Main.views.delete_comment,name="delete_comment"),
    path('tagadd/<int:pk>', Main.views.tag_add, name="tag_add"),
    path('tag', Main.views.tag_home, name="tag_home"),
    path('hashtag/<int:pk>', Main.views.tag_detail, name="tag_detail"),
    path('detail/<int:pk>/tag/<int:tag_pk>/delete', Main.views.tag_delete, name="tag_delete"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)