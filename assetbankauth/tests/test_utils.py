# -*- coding: utf-8 -*-
# (c) 2016 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com
from django.test.testcases import TestCase
from django.test.utils import override_settings

from assetbankauth.tests.utils import FakeRequest, KNOWN_TOKEN, KNOWN_AUTH_KEY, KNOWN_ASSETBANK_USER_ID, KNOWN_ASSETBANK_USERNAME, KNOWN_ASSETBANK_USER_GROUPS
from assetbankauth.utils import assetbank_login_redirect, authenticated_user_in_session, ASSETBANK_USER_SESSION_VARIABLE_NAME, \
    get_authenticated_user_in_session, \
    authenticate_token_in_request, TOKEN_PARAMETER_NAME


class AssetbankLoginRedirectTests(TestCase):
    @override_settings(ASSETBANK_URL='http://assetbank.test')
    @override_settings(ASSETBANK_LOG_OUT_AFTER_AUTH='true')
    def test_expected_redirect_constructed(self):
        self.assertEquals('http://assetbank.test/action/secureLinkToApp?redirect=http%3A//my.app&logOutAfterAuth=true',
                          assetbank_login_redirect(FakeRequest(current_url='http://my.app'))['Location'])


class AuthenticatedUserInSessionTests(TestCase):
    def test_authenticated_user_in_session_false_when_no_user_in_session(self):
        self.assertFalse(authenticated_user_in_session(FakeRequest()))

    def test_authenticated_user_in_session_true_when_user_in_session(self):
        self.assertTrue(authenticated_user_in_session(FakeRequest(session={ASSETBANK_USER_SESSION_VARIABLE_NAME: 'dummy-user'})))


class GetAuthenticatedUserInSessionTests(TestCase):
    def test_get_authenticated_user_in_session_none_when_no_user_in_session(self):
        self.assertEquals(None, get_authenticated_user_in_session(FakeRequest()))

    def test_get_authenticated_user_in_session_returns_user_when_user_in_session(self):
        self.assertEquals('dummy-user',
                          get_authenticated_user_in_session(FakeRequest(session={ASSETBANK_USER_SESSION_VARIABLE_NAME: 'dummy-user'})))


class AuthenticateTokenInRequestTests(TestCase):
    def test_authenticate_token_in_request_false_if_no_token_in_request(self):
        self.assertFalse(authenticate_token_in_request(FakeRequest()))

    @override_settings(ASSETBANK_AUTH_TOKEN_KEY=KNOWN_AUTH_KEY)
    def test_authenticate_token_in_request_true_if_valid_token_in_request(self):
        self.assertTrue(authenticate_token_in_request(FakeRequest(get={TOKEN_PARAMETER_NAME: KNOWN_TOKEN})))

    @override_settings(ASSETBANK_AUTH_TOKEN_KEY=KNOWN_AUTH_KEY)
    def test_authenticate_token_in_request_puts_user_in_request(self):
        request = FakeRequest(get={TOKEN_PARAMETER_NAME: KNOWN_TOKEN})
        authenticate_token_in_request(request)
        assetbank_user = request.session[ASSETBANK_USER_SESSION_VARIABLE_NAME]

        self.assertEquals(assetbank_user.id, KNOWN_ASSETBANK_USER_ID)
        self.assertEquals(assetbank_user.username, KNOWN_ASSETBANK_USERNAME)
        self.assertTrue(sorted(assetbank_user.group_ids), sorted(KNOWN_ASSETBANK_USER_GROUPS))
