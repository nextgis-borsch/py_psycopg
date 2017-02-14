#!/usr/bin/env python
# -*- coding: utf-8 -*-

# {
#     "info": {
#         "maintainer": null,
#         "docs_url": "http://pythonhosted.org/psycopg2/",
#         "requires_python": null,
#         "maintainer_email": null,
#         "cheesecake_code_kwalitee_id": null,
#         "keywords": null,
#         "package_url": "http://pypi.python.org/pypi/psycopg2",
#         "author": "Federico Di Gregorio",
#         "author_email": "fog@initd.org",
#         "download_url": "http://initd.org/psycopg/tarballs/PSYCOPG-2-6/psycopg2-2.6.2.tar.gz",
#         "platform": "any",
#         "version": "2.6.2",

import sys
import os
import json

version = '0.0.0'
download_url = ''

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

    version = data['info']['version']
    download_url = data['info']['download_url']
    date = data['releases'][version][0]['upload_time'].replace('T', ' ')

    version_file_name = os.path.join(os.path.dirname(sys.argv[1]), 'version.str')
    version_file = open(version_file_name, 'w')
    version_file.write("%s\n%s" % (version, date))
    version_file.close()

print download_url + ';' + version
