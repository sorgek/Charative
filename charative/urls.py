from django.conf.urls import url
from charative import views
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index, name='index'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^edituser/', views.edituser, name='edituser'),
    #url(r'^',  views.indexredirect, name='indexredirect'),
]