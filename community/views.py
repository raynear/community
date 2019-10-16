from django.http import JsonResponse
from django.middleware.csrf import get_token

# Create your views here.


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})
