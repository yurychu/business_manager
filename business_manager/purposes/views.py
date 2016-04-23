from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Purpose
from .forms import PurposeForm


class PurposesListView(LoginRequiredMixin, ListView):
    model = Purpose
    login_url = reverse_lazy('registration:login')


class PurposeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Purpose
    form_class = PurposeForm
    login_url = reverse_lazy('registration:login')
    success_url = reverse_lazy('purposes:list')
    success_message = 'Новая цель успешно создана!'

    def get_form_kwargs(self):
        kwargs = super(PurposeCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        purpose = form.save(commit=False)
        purpose.user = self.request.user
        purpose.save()
        super(PurposeCreateView, self).form_valid(form)
        return HttpResponseRedirect(self.success_url)


class PurposeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Purpose
    template_name_suffix = '_update_form'
    fields = ['title', 'description']
    success_message = 'Данные успешно отредактированы!'
    login_url = reverse_lazy('registration:login')
