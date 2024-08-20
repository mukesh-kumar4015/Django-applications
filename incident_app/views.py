from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from incident_app.models import Incident
from api.utility import update_incident_data, create_incident_data, create_user


@login_required(login_url='/login/')
def home(request):
    incidents = Incident.objects.filter(user_id=request.user.id)
    return render(request, 'incident_app/home.html', {'incidents': incidents})


def user_login(request):
    if request.method == "POST":
        login_cred = request.POST.dict()
        user = authenticate(username=login_cred['user'], password=login_cred['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home/')
    return render(request, 'incident_app/login.html')


def user_register(request):
    if request.method == "POST":
        data = request.POST.dict()
        profile = {}
        print('user data: ', data)
        profile.update({'country': data['country'],
                        'city': data['city'],
                        'phone': data['phone'],
                        'pin': data['pin'],
                        'address': data['address']
                        })
        data.update({'profile': profile})
        create_user(data)
        return HttpResponseRedirect('/login/')
    return render(request, 'incident_app/registration.html')


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def forget_password(request):
    if request.method == "POST":
        data = request.POST.dict()
        print("this is post data: ", data)
        try:
            User.objects.get(email=data['email'])
        except:
            return JsonResponse({'msg': 'invalid email'})

    return render(request, 'incident_app/forget_password.html')


def create_incident(request):
    if request.method == "POST":
        data = request.POST.dict()
        print("this is post data: ", data)
        create_incident_data(request, data)
        return HttpResponseRedirect('/home/')
    return render(request, 'incident_app/create_incident.html')


def update_incident(request, incident_id=None):
    if request.method == "POST":
        data = request.POST.dict()
        print("this is post data: ", data)
        update_incident_data(data)
        return HttpResponseRedirect('/home/')
    else:
        incident = Incident.objects.get(incident_id=incident_id)
        return render(request, 'incident_app/update_incident.html', {'incident': incident})
