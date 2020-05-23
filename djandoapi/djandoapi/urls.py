from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

import courses.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(courses.urls)),
]
