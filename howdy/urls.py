from django.conf.urls import url
from howdy import views


urlpatterns = [
    url(r'^$',views.show),
    url(r'^$', views.url_name)
]