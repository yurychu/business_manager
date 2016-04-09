from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(regex=r'^register/$',
        view=views.RegisterUserFormView.as_view(),
        name='register'),
]
