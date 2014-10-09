from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'salidas.views.home', name='home'),
    url(r'^new_application', 'salidas.views.new_application', name='new_application'),
    url(r'^application_detail', 'salidas.views.application_detail', name='application_detail'),
    url(r'^days_validation', 'salidas.views.days_validation', name='days_validation'),
    url(r'^finance_validation', 'salidas.views.finance_validation', name='finance_validation'),
    url(r'^index', 'salidas.views.index', name='index'),
    # Django's admin site
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)