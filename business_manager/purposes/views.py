from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin


from .models import Purpose
from .forms import PurposeForm


class PurposesListView(ListView):
    model = Purpose


class PurposeCreateView(SuccessMessageMixin, CreateView):
    model = Purpose
    form_class = PurposeForm
    success_url = '/purposes/'
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


class PurposeUpdateView(SuccessMessageMixin, UpdateView):
    model = Purpose
    template_name_suffix = '_update_form'
    fields = ['title', 'description']
    success_message = 'Данные успешно отредактированы!'
