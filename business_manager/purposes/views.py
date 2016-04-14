from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin


from .models import Purpose


class PurposesListView(ListView):
    model = Purpose


class PurposeCreateView(SuccessMessageMixin, CreateView):
    model = Purpose
    fields = ['title', 'description']
    # success_url = '/purposes/'
    success_message = 'Новая цель успешно создана!'


class PurposeUpdateView(SuccessMessageMixin, UpdateView):
    model = Purpose
    template_name_suffix = '_update_form'
    fields = ['title', 'description']
    success_message = 'Данные успешно отредактированы!'