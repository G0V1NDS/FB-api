from django.conf.urls import include, url
from django.contrib import admin
import ImgUpload

urlpatterns = [
    # Examples:
    # url(r'^$', 'ImageUpload.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^FB/', include('ImgUpload.urls', namespace='index')),
]
