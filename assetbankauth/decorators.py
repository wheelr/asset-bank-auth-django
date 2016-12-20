# -*- coding: utf-8 -*-
# (c) 2016 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com
from functools import wraps

from django.conf import settings
from django.utils.decorators import available_attrs

from assetbankauth.utils import authenticate_token_in_request, assetbank_login_redirect, authenticated_user_in_session


def ensure_assetbank_authenticated_user_in_session():
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if not settings.ASSETBANK_AUTH_ENABLED or authenticated_user_in_session(request) or authenticate_token_in_request(request):
                return view_func(request, *args, **kwargs)
            else:
                return assetbank_login_redirect(request)

        return _wrapped_view

    return decorator
