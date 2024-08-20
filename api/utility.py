from incident_app.models import Incident, UserProfile
from datetime import datetime
import random
from django.contrib.auth.models import User


def validate_incident_id(incident_id):
    if Incident.objects.filter(incident_id=incident_id).exists():
        return True
    return False


def get_incident_id():
    year = datetime.now().year
    while True:
        random_num = random.randrange(10000, 99999)
        incident_id = 'RMG' + str(random_num) + str(year)
        if not validate_incident_id(incident_id):
            return incident_id


def update_user_info(user, data):
    try:
        email = data.get('email', None)
        if email is not None:
            user.email = email
        user.save()
        user_profile, created = UserProfile.objects.get_or_create(user_id=user.id)
        phone = data['profile'].get('phone', None)
        if phone is not None:
            user_profile.phone = phone

        pin = data['profile'].get('pin', None)
        if pin is not None:
            user_profile.pin = pin

        address = data['profile'].get('address', None)
        if address is not None:
            user_profile.address = address

        city = data['profile'].get('city', None)
        if city is not None:
            user_profile.city = city

        country = data['profile'].get('country', None)
        if country is not None:
            user_profile.country = country

        user_profile.save()
        return True, None
    except Exception as e:
        return False, str(e)


def create_incident_data(request, data):
    incident_id = get_incident_id()
    user = request.user
    incident = Incident.objects.create(incident_id=incident_id,
                                       incident_type=data['type'],
                                       incident_details=data['details'],
                                       priority=data['priority'],
                                       incident_status=data['status'],
                                       user=user
                                       )
    incident.save()


def update_incident_data(data):
    incident = Incident.objects.get(incident_id=data['incident_id'])
    incident_type = data.get('type', None)
    if incident_type:
        incident.incident_type = incident_type

    incident_details = data.get('details', None)
    if incident_details:
        incident.incident_details = incident_details

    priority = data.get('priority', None)
    if priority:
        incident.priority = priority

    incident_status = data.get('status', None)
    if incident_status:
        incident.incident_status = incident_status

    incident.save()


def create_user(data):
    try:
        user = User.objects.create_user(data['email'], data['email'], data['password'])
        try:
            user.username = data['email']
        except:
            pass
        try:
            user.first_name = data['first_name']
        except:
            pass
        try:
            user.last_name = data['last_name']
        except:
            pass
        user.save()
        res = update_user_info(user, data)
        if res[0]:
            return True, None
        else:
            return res
    except Exception as e:
        return False, str(e)
