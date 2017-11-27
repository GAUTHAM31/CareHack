from django.conf.urls import url
from customer import views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

