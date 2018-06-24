from django.urls import include,path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#handler404 = 'app_homepage.views.showError404'
#handler500 = 'app_homepage.views.showError500'

urlpatterns = [
    path('', include('app_homepage.urls')),
    path('users/', include('app_users.urls')),
    path('captcha/', include('captcha.urls')), 
    path('contacts/', include('app_contacts.urls')),
    path('password_reset_recover/', include('password_reset.urls')),  
    path('services/', include('app_services.urls')),
    path('world/', include('app_world.urls')),
    path('test/', include('app_test.urls')),
    path('admin/', admin.site.urls),
] 

if settings.DEBUG == True:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)