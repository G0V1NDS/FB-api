from django.conf.urls import include, url
from django.contrib import admin
import ImgUpload

urlpatterns = [
    # Examples:
    url(r'^$', 'ImgUpload.views.index', name='index'),
    url(r'^photos/', 'ImgUpload.views.photos', name='photos'),
]
