from django.urls import include,path, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework import routers
from app_api import views 

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'usersapi', views.UserViewSet)
router.register(r'contactsapi', views.ContactViewSet)

#handler404 = 'app_homepage.views.showError404'
#handler500 = 'app_homepage.views.showError500'

urlpatterns = [
    path('api/', include(router.urls)),   
    path('api/', include('app_api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('home/', include('app_homepage.urls')),
    path('users/', include('app_users.urls')),
    path('captcha/', include('captcha.urls')), 
    path('contacts/', include('app_contacts.urls')),
    path('password_reset_recover/', include('password_reset.urls')),  
    path('geodjango/', include('app_geodjango.urls')),
    path('tasks/', include('app_tasks.urls')),
    path('chat/', include('app_chat.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^.*', TemplateView.as_view(template_name='react.html')),
    
] 

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)