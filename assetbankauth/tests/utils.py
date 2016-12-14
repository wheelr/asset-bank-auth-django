# -*- coding: utf-8 -*-
# (c) 2016 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com

KNOWN_AUTH_KEY = 'RXhhbXBsZUFFU0VuY0tleQ=='
# The follow token was encrypted by Asset Bank with the above auth key and when decoded and decrypted
# should give a user with the known values below
KNOWN_TOKEN = 'PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxBdXRoZW50aWNhdGlvblRva2VuPjxpbml0aWFsaXphdGlvblZlY3Rvcj5MQVRNRUs0Z01MS1J1SXVMR2dmVVFRPT08L2luaXRpYWxpemF0aW9uVmVjdG9yPjx0ZXh0Pi95QXgxd21VaUNqcUVXNmZ4eWE2Y3VoQS9iMzBvMHJNc2huZkRtUlk5SU5mWEwyNGFpYnR3T2w4ZnRwM1B5QUs3WDZnVFZxMkVlSlJ3K0gwbk9xNnI5WHIzN0VMbHZpODBDbWRmUCsrMU52VXlRenpNcEYwdUkvQkhBTSs0WUpmZkljR0tSeVY4MS9BYWpMTExmbE5TKzZHdkoyaHFTWml4Zi9kcTNjRExuZ1Z1MFZ1VDl4TDF5UFBJcDN6eXBaV25rNzdQWlZZdDljUzZTbzMvbEw1SXNsUVZqTUlKQ3ZaU2wwMndjSzdVM0k9PC90ZXh0PjwvQXV0aGVudGljYXRpb25Ub2tlbj4='
KNOWN_ASSETBANK_USERNAME = 'testuser'
KNOWN_ASSETBANK_USER_ID = 4
KNOWN_ASSETBANK_USER_GROUPS = [1, 3]


class FakeRequest(object):
    def __init__(self, user=None, path='', current_url='', session=False, get=False):
        self.user = user
        self.path = path

        if not session:
            self.session = {}
        else:
            self.session = session
        self.COOKIES = {}

        if not get:
            self.GET = {}
        else:
            self.GET = get

        self.POST = {}
        self.REQUEST = {}
        self.current_url = current_url

    def get_full_path(self):
        return self.path

    def build_absolute_uri(self):
        return self.current_url
