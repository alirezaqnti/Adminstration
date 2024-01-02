from core.settings import MEDIA_URL


def Con(request):
    try:
        INACTIVE = request.session['INACTIVE']
    except:
        INACTIVE = False
    print("INACTIVE",INACTIVE)
    context = {
        'MEDIA_URL': MEDIA_URL,
        'INACTIVE':INACTIVE
    }
    return context