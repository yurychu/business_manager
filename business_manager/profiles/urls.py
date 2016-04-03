from django.conf.urls import url
from . import views


urlpatterns = [
    url(regex=r'^register/$',
        view=views.create_user,
        name='create_user'),
]
