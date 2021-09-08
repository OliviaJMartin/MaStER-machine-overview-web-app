from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


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

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, context={
            'form': form,
            'Machine_Name': 'LA4',
        }, )

    def post(self, request):
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
                'Machine_Name': 'LA4',
            }, )


class status(LoginRequiredMixin, View):
    template = 'MachineStatus.html'
    login_url = '/login/'

    def get(self, request):
        return render(request, self.template, context={
                'Machine_Name': 'LA4',
                'Serial_No': '2459',
                'SW_Version': 'TB v2.5',
                'Machine_Status': 'Clinical With Limitations',
                'Current_Owner': 'Olivia Martin',
                'Start_Time': ''
            },)


class loggingout(View):
    template = 'Overview.html'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class update(View):
    template = 'UpdateStatus.html'

    def get(self, request):
        return render(request, self.template, context={
                'Machine_Name': 'LA4',
                'User': 'OlMartin',
            },)


class recentStatus(View):
    template = 'x'
