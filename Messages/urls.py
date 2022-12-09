from django.urls import path ,include
from . import views
from rest_framework.routers import DefaultRouter
from Messages.views import *

router = DefaultRouter()
router.register('Message', list_posts,basename='list_posts')


urlpatterns = [

    path('',include(router.urls)),
   
]