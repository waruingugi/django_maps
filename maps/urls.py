from maps import views
from django.conf.urls import url

urlpatterns = [
    url(r'^plotting', views.plotting, name='plotting'),
]
