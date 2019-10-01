from django.shortcuts import render
from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from .forms import LoginForm


def login(request):
    providers = []
    for provider in get_providers():
        # social_app속성은 provider에는 없는 속성입니다.
    try:
    provider.social_app = SocialApp.objects.get(
        provider=provider.id, sites=settings.SITE_ID)
    except SocialApp.DoesNotExist:
    provider.social_app = None
    providers.append(provider)
    return auth_login(request,
                      authentication_form=LoginForm,
                      template_name='accounts/login_form.html',
                      extra_context={'providers': providers})
