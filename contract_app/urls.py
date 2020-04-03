from django.conf.urls import url
from contract_app import views
urlpatterns = [
    url(r'^index$', views.index),
    url(r'^register$', views.register),
    url(r'^register_check$', views.register_check),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^reset$', views.reset),
]
