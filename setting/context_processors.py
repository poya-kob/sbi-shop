from .models import SiteSetting


def setting(request):
    """
    Return 'site setting' context variable
    """
    return {'setting': SiteSetting.objects.last()}
