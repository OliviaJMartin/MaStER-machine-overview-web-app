from django.shortcuts import render


def overview(request):
    return render(request, "Overview.html")


def login(request):
    return render(request, "Login.html")


def status(request):
    return render(request, "MachineStatus.html")


def update(request):
    return render(request, "UpdateStatus.html")
