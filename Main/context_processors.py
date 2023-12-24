from core.settings import MEDIA_URL


def Con(request):
    context = {
        'MEDIA_URL': MEDIA_URL
    }
    return context