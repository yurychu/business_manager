from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^$',
        view=views.PurposesListView.as_view(),
        name='list'),
    url(regex=r'^add$',
        view=views.PurposeCreateView.as_view(),
        name='create')
]
