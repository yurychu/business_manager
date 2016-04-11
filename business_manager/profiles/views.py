from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


class RegisterUserFormView(View):
    form_class = UserCreationForm
    template_name = 'profiles/profile_create_user.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})
