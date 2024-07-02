from django.contrib import admin
from django.urls import path
from blog.views import index, addBlog, listblog, modifierblog

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('create/', addBlog, name='create'),
    path('table/', listblog, name='table'),
    path('modifier/<int:pk>', modifierblog, name='modifier'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                 document_root=settings.MEDIA_ROOT)
