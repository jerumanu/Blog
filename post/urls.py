from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.mypost, name='home'),
    
    path('upload/', views.upload, name = 'upload-post'),
    path('update/<int:post_id>', views.update_post  ),
    path('delete/<int:post_id>', views.delete_post),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
