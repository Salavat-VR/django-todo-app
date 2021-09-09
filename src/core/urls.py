from django.conf.urls import url
from django.urls import path, include
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.index),

]