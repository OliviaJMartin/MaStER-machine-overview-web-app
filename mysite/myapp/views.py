from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


class overview(View):
    template = 'Overview.html'

    def get(self, request):
        return render(request, self.template)


class loggingin(View):
    template = 'Login.html'

    def get(self, request):
        form = AuthenticationForm()
        machine = request.session.get('machine', 'LA1')
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/machinestatus/')
        else:
            return render(request, self.template, {'form': form})


class status(LoginRequiredMixin, View):
    template = 'MachineStatus.html'
    login_url = '/login/'

    def get(self, request):
        return render(request, self.template)


class loggingout(View):
    template = 'Overview.html'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class update(View):
    template = 'UpdateStatus.html'

    def get(self, request):
        return render(request, self.template)
