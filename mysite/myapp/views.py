from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import User
from time import gmtime, strftime

import datetime


class startup(View):
    def get(self, request):
        request.session['LA1_status'] = 'Fully Serviceable (Clinical)'
        request.session['LA2_status'] = 'Fully Serviceable (Clinical)'
        request.session['LA4_status'] = 'Fully Serviceable (Clinical)'
        request.session['CT_status'] = 'Fully Serviceable (Clinical)'
        request.session['Brachytherapy_status'] = 'Fully Serviceable (Clinical)'

        request.session['LA1_currentUser'] = 'Test Ing'
        request.session['LA2_currentUser'] = 'Test Ing'
        request.session['LA4_currentUser'] = 'Test Ing'
        request.session['CT_currentUser'] = 'Test Ing'
        request.session['Brachytherapy_currentUser'] = 'Test Ing'

        request.session['LA1_time'] = 'n/a'
        request.session['LA2_time'] = 'n/a'
        request.session['LA4_time'] = 'n/a'
        request.session['CT_time'] = 'n/a'
        request.session['Brachytherapy_time'] = 'n/a'

        return HttpResponseRedirect('/overview/')


class overview(View):
    template = 'Overview.html'

    def get(self, request):
        LA1_status = request.session.get('LA1_status')
        LA2_status = request.session.get('LA2_status')
        LA4_status = request.session.get('LA4_status')
        CT_status = request.session.get('CT_status')
        Brachytherapy_status = request.session.get('Brachytherapy_status')

        LA1_currentUser = request.session.get('LA1_currentUser')
        LA2_currentUser = request.session.get('LA2_currentUser')
        LA4_currentUser = request.session.get('LA4_currentUser')
        CT_currentUser = request.session.get('CT_currentUser')
        Brachytherapy_currentUser = request.session.get('Brachytherapy_currentUser')

        LA1_time = request.session.get('LA1_time')
        LA2_time = request.session.get('LA2_time')
        LA4_time = request.session.get('LA4_time')
        CT_time = request.session.get('CT_time')
        Brachytherapy_time = request.session.get('Brachytherapy_time')

        request.session['loggedIn'] = False
        return render(request, self.template,
                      context={
                          'LA1_status': LA1_status,
                          'LA2_status': LA2_status,
                          'LA4_status': LA4_status,
                          'CT_status': CT_status,
                          'Brachy_status': Brachytherapy_status,
                          'LA1_user': LA1_currentUser,
                          'LA2_user': LA2_currentUser,
                          'LA4_user': LA4_currentUser,
                          'CT_user': CT_currentUser,
                          'Brachy_user': Brachytherapy_currentUser,
                          'LA1_time': LA1_time,
                          'LA2_time': LA2_time,
                          'LA4_time': LA4_time,
                          'CT_time': CT_time,
                          'Brachy_time': Brachytherapy_time,
                      },
                      )


class loggingin(View):
    template = 'Login.html'

    def get(self, request, machine):
        form = AuthenticationForm()
        request.session['machineChosen'] = machine
        request.session['loggedIn'] = False

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
            request.session['loggedIn'] = True
            login(request, user)
            request.session['currentUsersName'] = user.first_name + ' ' + user.last_name
            return HttpResponseRedirect('/machinestatus/')
        else:
            return HttpResponseRedirect('/overview/')


class status(LoginRequiredMixin, View):
    template = 'MachineStatus.html'
    login_url = '/login/'

    # database_status = MachineStatus.objects.filter(machineid=Machine_Name)

    def get(self, request):
        loggedIn = request.session.get("loggedIn")

        if not loggedIn:
            return HttpResponseRedirect('/login/')

        machine = request.session.get("machineChosen")
        if machine == 'LA1':
            statusUser = request.session.get("LA1_currentUser")
            statusTime = request.session.get("LA1_time")
        elif machine == 'LA2':
            statusUser = request.session.get("LA2_currentUser")
            statusTime = request.session.get("LA2_time")
        elif machine == 'LA3':
            statusUser = request.session.get("LA4_currentUser")
            statusTime = request.session.get("LA4_time")
        elif machine == 'CT':
            statusUser = request.session.get("CT_currentUser")
            statusTime = request.session.get("CT_time")
        else:
            statusUser = request.session.get("Brachytherapy_currentUser")
            statusTime = request.session.get("Brachytherapy_time")

        return render(request, self.template, context={
            'Machine_Name': machine,
            'Serial_No': '2459',
            'SW_Version': 'TB v2.5',
            'Machine_Status': 'Clinical With Limitations',
            'Current_Owner': statusUser,
            'Start_Time': statusTime,
            'Database_Status': '',  # self.database_status,
        }, )


class loggingout(View):
    def get(self, request):  # needs a self.variable to be allowed
        logout(request)
        request.session['loggedIn'] = False
        return HttpResponseRedirect('/')


class update(View):
    template = 'UpdateStatus.html'
    time = datetime.datetime.now()

    def get(self, request):
        currentUsersName = request.session.get('currentUsersName')
        machine = request.session.get("machineChosen")
        return render(request, self.template, context={
            'Machine_Name': machine,
            'User': currentUsersName,
        }, )

    def post(self, request):
        machine = request.session.get("machineChosen")

        status_ = request.POST['status']
        if status_ == 'Select status':
            return HttpResponseRedirect('/updatestatus/')

        description = request.POST['description']
        comments = request.POST['multiLineInput']
        user = request.session.get('currentUsersName')
        time = str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))

        if machine == 'LA1':
            request.session['LA1_status'] = status_
            request.session['LA1_description'] = description
            request.session['LA1_comment'] = comments
            request.session['LA1_currentUser'] = user
            request.session['LA1_time'] = time
        elif machine == 'LA2':
            request.session['LA2_status'] = status_
            request.session['LA2_description'] = description
            request.session['LA2_comment'] = comments
            request.session['LA2_currentUser'] = user
            request.session['LA2_time'] = time
        elif machine == 'LA4':
            request.session['LA4_status'] = status_
            request.session['LA4_description'] = description
            request.session['LA4_comment'] = comments
            request.session['LA4_currentUser'] = user
            request.session['LA4_time'] = time
        elif machine == 'CT':
            request.session['CT_status'] = status_
            request.session['CT_description'] = description
            request.session['CT_comment'] = comments
            request.session['CT_currentUser'] = user
            request.session['CT_time'] = time
        elif machine == 'Brachytherapy':
            request.session['Brachytherapy_status'] = status_
            request.session['Brachytherapy_description'] = description
            request.session['Brachytherapy_comment'] = comments
            request.session['Brachytherapy_currentUser'] = user
            request.session['Brachytherapy_time'] = time

        return HttpResponseRedirect('/checking/')


class checking(View):
    template = 'checkingValues.html'

    def get(self, request):
        LA1_status = request.session.get('LA1_status')
        LA2_status = request.session.get('LA2_status')
        LA4_status = request.session.get('LA4_status')
        CT_status = request.session.get('CT_status')
        Brachytherapy_status = request.session.get('Brachytherapy_status')

        LA1_currentUser = request.session.get('LA1_currentUser')
        LA2_currentUser = request.session.get('LA2_currentUser')
        LA4_currentUser = request.session.get('LA4_currentUser')
        CT_currentUser = request.session.get('CT_currentUser')
        Brachytherapy_currentUser = request.session.get('Brachytherapy_currentUser')

        LA1_time = request.session.get('LA1_time')
        LA2_time = request.session.get('LA2_time')
        LA4_time = request.session.get('LA4_time')
        CT_time = request.session.get('CT_time')
        Brachytherapy_time = request.session.get('Brachytherapy_time')

        request.session['loggedIn'] = False
        return render(request, self.template,
                      context={
                          'LA1_status': LA1_status,
                          'LA2_status': LA2_status,
                          'LA4_status': LA4_status,
                          'CT_status': CT_status,
                          'Brachy_status': Brachytherapy_status,
                          'LA1_user': LA1_currentUser,
                          'LA2_user': LA2_currentUser,
                          'LA4_user': LA4_currentUser,
                          'CT_user': CT_currentUser,
                          'Brachy_user': Brachytherapy_currentUser,
                          'LA1_time': LA1_time,
                          'LA2_time': LA2_time,
                          'LA4_time': LA4_time,
                          'CT_time': CT_time,
                          'Brachy_time': Brachytherapy_time,
                      },
                      )