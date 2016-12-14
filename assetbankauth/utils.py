# -*- coding: utf-8 -*-
# (c) 2016 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com
import base64
import urllib
import xml.etree.ElementTree as ET

from Crypto.Cipher import AES
from django.conf import settings
from django.http.response import HttpResponseRedirect

from assetbankauth.models import AssetBankUser

TOKEN_PARAMETER_NAME = 'token'

ASSETBANK_USER_SESSION_VARIABLE_NAME = 'authenticated_assetbank_user'


def assetbank_login_redirect(request):
    ab_login_url = '%s/action/secureLinkToApp?redirect=%s&logOutAfterAuth=%s' % (
        settings.ASSETBANK_URL,
        urllib.quote(request.build_absolute_uri()),
        'true' if settings.ASSETBANK_LOG_OUT_AFTER_AUTH else 'false')
    return HttpResponseRedirect(ab_login_url)


def authenticated_user_in_session(request):
    if ASSETBANK_USER_SESSION_VARIABLE_NAME in request.session:
        return True
    return False


def get_authenticated_user_in_session(request):
    if ASSETBANK_USER_SESSION_VARIABLE_NAME in request.session:
        return request.session[ASSETBANK_USER_SESSION_VARIABLE_NAME]
    return None


def authenticate_token_in_request(request):
    token = request.GET.get(TOKEN_PARAMETER_NAME, False)
    if token:
        initialization_vector, text = _decode_token(token)
        user_details_xml = _decrypt_user_details(initialization_vector, text)
        request.session[ASSETBANK_USER_SESSION_VARIABLE_NAME] = _assetbank_user_from_user_details_xml(user_details_xml)

        return True
    return False


def _assetbank_user_from_user_details_xml(user_details_xml):
    root = ET.fromstring(user_details_xml)
    assetbank_user_id = int(root.findall('id')[0].text)
    assetbank_username = root.findall('username')[0].text
    group_ids = []
    for group_id in root.findall('groupIds'):
        group_ids.append(int(group_id.text))

    return AssetBankUser(assetbank_user_id, assetbank_username, group_ids)


def _decrypt_user_details(iv, encrypted_user_details):
    decoded_encrypted_user_details = base64.b64decode(encrypted_user_details)
    key = base64.b64decode(settings.ASSETBANK_AUTH_TOKEN_KEY)
    iv = base64.b64decode(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv[:16])
    user_details_bytes = _unpad(cipher.decrypt(decoded_encrypted_user_details))
    return user_details_bytes


def _decode_token(token):
    token_decoded = base64.b64decode(token)
    root = ET.fromstring(token_decoded)
    initialization_vector = root.findall('initializationVector')[0].text
    text = root.findall('text')[0].text
    return initialization_vector, text


def _unpad(s):
    return s[0:-ord(s[-1])]
