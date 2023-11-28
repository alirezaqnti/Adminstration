# from django.shortcuts import render
import random
import string
from datetime import datetime


def RandInt(prefix):
    d = datetime.now().strftime("%Y%S")
    return f"{prefix}-{d}{str(random.randint(1000,9999))}"


def RandString():
    letters = string.ascii_uppercase
    result_str = "".join(random.choice(letters) for i in range(6))
    return result_str

