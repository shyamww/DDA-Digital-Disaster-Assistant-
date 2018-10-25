
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import UserForm
from django.views.generic import View


class UserFormView(View):
    form_class = UserForm
    template_name = 'account/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return user object if credentials are correct

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('home')

        return render(request, self.template_name, {'form': form})




