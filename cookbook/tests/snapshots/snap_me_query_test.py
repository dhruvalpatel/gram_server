# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_me_query 1'] = {
    'data': {
        'me': {
            'email': 'dhruval@gmail.com',
            'username': 'dhruval'
        }
    }
}
