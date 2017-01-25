# -*- coding: utf-8 -*-
#
# This file is part of CERN Analysis Preservation Framework.
# Copyright (C) 2017 CERN.
#
# CERN Analysis Preservation Framework is free software; you can redistribute
# it and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Analysis Preservation Framework is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CERN Analysis Preservation Framework; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.


"""CAP Deposit loaders."""

import requests
from flask import request


def attach_file_from_url(record, field):
    """Attach file from url speficied in given field."""
    source = field.get('source')
    if source and source.get('preserved') and source.get('url'):
        key = source.get('url').split('/')[-1]
        field['key'] = key
        if key not in record.files:
            record.files[key] = requests.get(
                source.get('url'), stream=True).raw
            record.files[key]['source'] = source.get('url')
            # TODO record.files[key]['references'] = []
            field['version_id'] = str(record.files[key].version_id)


def json_v1_loader(data=None):
    """Load data from request and process URLs."""
    data = data or request.json

    if request and request.view_args.get('pid_value'):
        _, record = request.view_args.get('pid_value').data

        for measurement in data.get('main_measurements', []):
            if 'code_base' in measurement:
                attach_file_from_url(record, measurement['code_base'])
            for n_tuple in measurement.get('n_tuple', []):
                if 'user_code' in n_tuple:
                    attach_file_from_url(record, n_tuple['user_code'])

    return data
