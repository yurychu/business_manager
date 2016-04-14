from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin


from .models import Purpose
from .forms import PurposeForm


class PurposesListView(ListView):
    model = Purpose


class PurposeCreateView(SuccessMessageMixin, CreateView):
    model = Purpose
    form_class = PurposeForm
    # success_url = '/purposes/'
    success_message = 'Новая цель успешно создана!'

    def get_form_kwargs(self):
        kwargs = super(PurposeCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PurposeUpdateView(SuccessMessageMixin, UpdateView):
    model = Purpose
    template_name_suffix = '_update_form'
    fields = ['title', 'description']
    success_message = 'Данные успешно отредактированы!'
