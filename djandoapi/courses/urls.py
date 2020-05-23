from django.conf.urls import url
from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('courses', views.CourseView)

urlpatterns = [
    path('', include(router.urls)),
    url(r'', include(router.urls))
]