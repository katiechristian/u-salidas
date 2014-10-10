from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'salidas.views.home', name='home'),
    url(r'^new_application', 'salidas.views.new_application', name='new_application'),
    url(r'^formulario_test', 'salidas.views.formulario_test', name='formulario_test'),

    # Django's admin site
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)