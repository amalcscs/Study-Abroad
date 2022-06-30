
from django.contrib import admin
from django.urls import re_path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path
from app import views


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.DocumentOfficer_dashboard, name='DocumentOfficer_dashboard'),
    re_path(r'^DocumentOfficer_index$', views.DocumentOfficer_index, name='DocumentOfficer_index'),
    re_path(r'^DocumentOfficer_CurrentLeads_table$', views.DocumentOfficer_CurrentLeads_table, name='DocumentOfficer_CurrentLeads_table'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
