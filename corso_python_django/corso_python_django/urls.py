from django.urls import include, path
from django.contrib import admin

from gamelibs.views import indovina_numero_web

urlpatterns = [
    # Examples:
    # url(r'^$', 'corso_python_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    path('gioco/indovina_numero', indovina_numero_web, name='indovina_numero_web')
]
