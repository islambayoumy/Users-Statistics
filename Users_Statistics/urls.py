from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stats/', include('stats.urls', namespace='stats', app_name='stats'))
]
