from django.shortcuts import render


# Create your views here.
def workertable(request):
    return render(request,"MonitoringApp/workertable.html")