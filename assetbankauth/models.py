# -*- coding: utf-8 -*-
# (c) 2016 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com

from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class AssetBankUser(object):
    id = None
    username = ''
    group_ids = []

    def __init__(self, user_id, username, group_ids):
        self.id = user_id
        self.username = username
        self.group_ids = group_ids

    def __str__(self):
        return 'Asset Bank User: %s : %s' % (id)

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return 1  # instances always return the same hash value
