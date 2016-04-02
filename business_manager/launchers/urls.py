from django.conf.urls import url

from .views import home_page

urlpatterns = [
    url(regex=r'^$',
        view=home_page,
        name='home_page')
]
