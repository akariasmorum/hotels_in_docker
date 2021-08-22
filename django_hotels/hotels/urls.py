from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'', views.index, name='root'),
]