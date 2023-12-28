# from django.shortcuts import render
import random
import string
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from kavenegar import KavenegarAPI

from . import models

try:
    from core.Private import KAVENEGAR_API_KEY
except:
    KAVENEGAR_API_KEY = ""


def RandInt(prefix):
    d = datetime.now().strftime("%Y%S")
    return f"{prefix}-{d}{str(random.randint(1000,9999))}"


def RandString():
    letters = string.ascii_uppercase
    result_str = "".join(random.choice(letters) for i in range(6))
    return result_str

def CreateNewPermission(Model,Code,Name):
    content_type = ContentType.objects.get_for_model(Model) 
    permission = Permission.objects.create(
        codename=Code,
        name=Name,
        content_type=content_type,
    )
    return permission

def get_user_group_names(self):
    gp = self.groups.all()
    arr = []
    for item in gp:
        arr.append(item.name)
    print(arr)
    return arr

User.add_to_class('get_user_group_names',get_user_group_names)


# region Send SMS
# send a single token sms
def SendSMS(data):
    try:
        api = KavenegarAPI(KAVENEGAR_API_KEY)
        params = {
            "receptor": data["Phone"],
            "template": data["template"],
        }
        try:
            params["token"] = data["token"]
        except:
            pass

        try:
            params["token2"] = data["token2"]
        except:
            pass

        try:
            params["token3"] = data["token3"]
        except:
            pass

        try:
            params["token10"] = data["token10"]
        except:
            pass
        try:
            params["token20"] = data["token20"]
        except:
            pass

        response = api.verify_lookup(params)
    except Exception as e:
        print(e)


# endregion

# region Code
# functions:
# ایجاد یک کد ۶ رقمی برای اعتبار سنجی تلفن همراه
# ورودی ها:
# شماره تلفن همراه
# خروجی :
# کد ۶ رقمی


def Code(phone):
    co = models.CodeReg()
    co.Phone = phone
    co.save()
    number = co.Code
    template = "AdminstrationCodeVerification"
    data = {
        "template": template,
        "token": number,
        "Phone": phone,
    }
    SendSMS(data)
    return number


# endregion
