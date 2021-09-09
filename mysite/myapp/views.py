from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import *
import datetime


class overview(View):
    template = 'Overview.html'

    def get(self, request):
        # la1_status = models.Machinestatus.status.all()
        #
        # for i in la1_status:
        #     # request.session['LA1_status'] = i.Status
        #     print(i.Status)
        return render(request, self.template,
                      context={
                          'LA1_status': 'On Service / PMI',
                          'LA2_status': 'Fully Serviceable',
                          'LA4_status': 'Clinical With Limitations',
                          'CT_status': 'Unserviceable',
                          'Brachy_status': 'Fully Serviceable',
                          'LA1_user': 'Testing',
                          'LA2_user': 'Checking',
                          'LA4_user': 'Checking',
                          'CT_user': 'Testing',
                          'Brachy_user': 'OlMartin',
                          'LA1_time': '08:00',
                          'LA2_time': '09:00',
                          'LA4_time': '10:00',
                          'CT_time': '11:00',
                          'Brachy_time': '12:00',
                      },
                      )


class loggingin(View):
    template = 'Login.html'

    def get(self, request, machine):
        form = AuthenticationForm()
        request.session['machineChosen'] = machine

        return render(request, self.template, context={
            'form': form,
            'Machine_Name': machine,
        }, )

    def post(self, request, machine):
        request.session['machineChosen'] = machine
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/machinestatus/')
        else:
            return render(request, self.template, context={
                'form': form,
                'Machine_Name': machine,
            }, )


class status(LoginRequiredMixin, View):
    template = 'MachineStatus.html'
    login_url = '/login/'

    # database_status = MachineStatus.objects.filter(machineid=Machine_Name)

    def get(self, request):
        machine = request.session.get("machineChosen")
        return render(request, self.template, context={
            'Machine_Name': machine,
            'Serial_No': '2459',
            'SW_Version': 'TB v2.5',
            'Machine_Status': 'Clinical With Limitations',
            'Current_Owner': 'Olivia Martin',
            'Start_Time': '',
            'Database_Status': '',  # self.database_status,
        }, )


class loggingout(View):
    def get(self, request):  # needs a self.variable to be allowed
        logout(request)
        return HttpResponseRedirect('/')


class update(View):
    template = 'UpdateStatus.html'
    time = datetime.datetime.now()

    def get(self, request, buttonChoice='get'):
        machine = request.session.get("machineChosen")
        return render(request, self.template, context={
            'Machine_Name': machine,
            'User': 'OlMartin',
        }, )

    def post(self, request, buttonChoice='post'):
        machine = request.session.get("machineChosen")

        machine_status = machine + "_status"
        machine_description = machine + "_description"
        machine_comment = machine + "_comment"

        status_ = request.POST['status']
        request.session[machine_status] = status_

        description = request.POST['description']
        request.session[machine_description] = description

        comments = request.POST['multiLineInput']
        request.session[machine_comment] = comments

        return HttpResponseRedirect('/machinestatus/')


