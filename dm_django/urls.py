"""
URL configuration for dm_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path #url() is deplicated in Django 3.0. See details https://stackoverflow.com/questions/70319606/importerror-cannot-import-name-url-from-django-conf-urls-after-upgrading-to
from dm_django import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.views.static import serve 
from django.views.generic import TemplateView
from dm_django import main_views

app_name = "dm_django"

urlpatterns = [

    #robots.txt path section
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),

    #admin path section
    path('admin/', admin.site.urls),

    #app path section
    path('', include('dm_portfolio.urls', namespace="dm_portfolio")),

    re_path(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
    #account app path section
    re_path(r'^api/', include('accounts.urls')),

    #dm_jango path section
    path('', main_views.MainView.as_view(), name="home"),
	path('contact/', main_views.ContactView.as_view(), name="contact"),
    path('blog/', main_views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', main_views.BlogDetailView.as_view(), name="blog"),

]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

