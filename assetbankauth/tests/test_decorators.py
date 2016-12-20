# -*- coding: utf-8 -*-
# (c) 2016 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com
from django.test.testcases import TestCase
from django.test.utils import override_settings
from mock.mock import patch

from assetbankauth.decorators import ensure_assetbank_authenticated_user_in_session
from assetbankauth.tests.utils import FakeRequest


@ensure_assetbank_authenticated_user_in_session()
def test_view(request):
    return "view"


class IsAssetbankAuthenticatedUserTests(TestCase):
    @override_settings(ASSETBANK_AUTH_ENABLED=False)
    def test_view_returned_if_assetbank_auth_disabled(self):
        self.assert_view_returned()

    @override_settings(ASSETBANK_AUTH_ENABLED=True)
    @patch('assetbankauth.decorators.authenticated_user_in_session', return_value=True)
    def test_view_returned_if_authenticated_user_in_session(self, mock_authenticated_user_in_session, ):
        self.assert_view_returned()

    @override_settings(ASSETBANK_AUTH_ENABLED=True)
    @patch('assetbankauth.decorators.authenticated_user_in_session', return_value=False)
    @patch('assetbankauth.decorators.authenticate_token_in_request', return_value=True)
    def test_view_returned_if_authenticate_token_in_request(self,
                                                            mock_authenticate_token_in_request,
                                                            mock_authenticated_user_in_session):
        self.assert_view_returned()

    @override_settings(ASSETBANK_AUTH_ENABLED=True)
    @patch('assetbankauth.decorators.authenticated_user_in_session', return_value=False)
    @patch('assetbankauth.decorators.authenticate_token_in_request', return_value=False)
    @patch('assetbankauth.decorators.assetbank_login_redirect', return_value='redirect')
    def test_redirect_returned_not_authenticated(self,
                                                 mock_assetbank_login_redirect,
                                                 mock_authenticate_token_in_request,
                                                 mock_authenticated_user_in_session):
        self.assert_redirect_returned()

    def assert_view_returned(self):
        self.assertEquals("view", test_view(FakeRequest()))

    def assert_redirect_returned(self):
        self.assertEquals("redirect", test_view(FakeRequest()))
