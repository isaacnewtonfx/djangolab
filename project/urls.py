from django.urls import include,path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from app_api import views 

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'contacts', views.ContactViewSet)

#handler404 = 'app_homepage.views.showError404'
#handler500 = 'app_homepage.views.showError500'

urlpatterns = [
    path('api/', include(router.urls)),   
    path('api/', include('app_api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', include('app_homepage.urls')),
    path('users/', include('app_users.urls')),
    path('captcha/', include('captcha.urls')), 
    path('contacts/', include('app_contacts.urls')),
    path('password_reset_recover/', include('password_reset.urls')),  
    path('geodjango/', include('app_geodjango.urls')),
    path('tasks/', include('app_tasks.urls')),
    path('chat/', include('app_chat.urls')),
    path('admin/', admin.site.urls),
    
] 

if settings.DEBUG == True:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)