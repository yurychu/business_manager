from django.conf.urls import url
from . import views


urlpatterns = [
    url(regex=r'^register/$',
        view=views.RegisterFormView.as_view(),
        name='register'),
]
