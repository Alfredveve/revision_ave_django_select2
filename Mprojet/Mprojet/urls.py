from django.contrib import admin
from django.urls import path
from blog.views import index, addBlog

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('create/', addBlog, name='create'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                 document_root=settings.MEDIA_ROOT)
