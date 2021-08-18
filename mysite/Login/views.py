from django.shortcuts import render, redirect


def index(request):
    return render(request, "Login.html")  # relative url


# def redirect_overview(request):
#     return redirect(request, "Overview.html")


# def redirect_machinestatus(request):
#     return redirect(request, "MachineStatus.html")
