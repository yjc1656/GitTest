from django.conf.urls import url
from contract_excel import views
urlpatterns = [
    url(r'^hs_info$', views.hs_info),
    url(r'^hs_code$', views.hs_code),
    url(r'^hs_info_new$', views.hs_info_new),
    url(r'^hs_code_new$', views.hs_code_new),
]
