# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_crops_query 1'] = {
    'data': {
        'crops': [
            {
                'cropName': 'Wheat',
                'cropNameHi': 'ghenhu',
                'crops': [
                ],
                'imageThumbnail': 'wheat.jpg',
                'quantity': 0.0,
                'receipts': 0
            }
        ]
    }
}
