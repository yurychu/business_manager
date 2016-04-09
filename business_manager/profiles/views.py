from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm


class RegisterFormView(View):
    form_class = UserCreationForm
    template_name = 'profiles/profile_register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})
