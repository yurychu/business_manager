from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin


from .models import Purpose


class PurposesListView(ListView):
    model = Purpose


class PurposeCreateView(SuccessMessageMixin, CreateView):
    model = Purpose
    fields = ['title', 'description']
    # success_url = '/purposes/'
    success_message = 'Новая цель успешно создана!'
