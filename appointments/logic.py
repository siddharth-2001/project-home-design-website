from .models import Appointment

def duplicate_checker(phone):
    check = list(Appointment.objects.filter(phone = phone, completed = False))
    if len(check) == 0:
        return False
    else:
        return True