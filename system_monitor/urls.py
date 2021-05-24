
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from monitor_api.views import home_view, signup
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('app/signup/', signup, name='signup'),
    path('app/admin/', admin.site.urls),
    path('app/accounts/', include('django.contrib.auth.urls')),
    path('app/', home_view, name='home'),
    path('app/api/', include('monitor_api.urls', namespace='monitor_api')),
    ]

urlpatterns += staticfiles_urlpatterns()