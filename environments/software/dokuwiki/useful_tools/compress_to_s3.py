#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @date        20160213
"""
Compress wiki file for backup
"""
import os
import configparser
from subprocess import call
from datetime import date

from boto3.session import Session

filename = "/work/mywiki/backup/{}".format(date.today())
# cmd = ("cd /work/mywiki/dokuwiki/data; "
#        "tar -zcv media pages -f /work/mywiki/backup/{}.tar.gz".format(date.today()))

# Read configure
config = configparser.ConfigParser()
config.read('aws.ini')
if 'AWS-S3' in config:
    conf = config['AWS-S3']
else:
    conf = {
        'AWS_KEY_ID': 'example',
        'AWS_SECRET_KEY': 'example',
        'REGION_NAME': 'example',
        'BUCKET_NAME': 'example'
    }

if 'FILE' in config:
    password = config['FILE']['PASSWORD']
else:
    password = 'example'
# -

cmd_list = (
    "cd /work/mywiki/dokuwiki/data; "
    "tar -zcv media pages -f /work/mywiki/backup/{}.tar.gz".format(date.today()),
    "cd /work/mywiki/dokuwiki/data; "
    "7za a -tzip -mem=AES256 -mx=9 -p{0} {1}.7z {1}.tar.gz".format(password, filename)
)

for cmd in cmd_list:
    print(cmd)
    call(cmd, shell=True)

"""
Upload to S3
"""
session = Session(aws_access_key_id=conf['AWS_KEY_ID'],
                  aws_secret_access_key=conf['AWS_SECRET_KEY'],
                  region_name=conf['REGION_NAME'])


s3 = session.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)

# upload
bucket = s3.Bucket(conf['BUCKET_NAME'])
upload_obj = '{}.7z'.format(filename)
target_key = '{}.7z'.format(date.today())
try:
    obj = bucket.Object(target_key)
    obj.upload_file(upload_obj)
except FileNotFoundError:
    print('cover file')
    with open(upload_obj, 'rb') as data:
        bucket.put_object(Key=target_key, Body=data)


# Delete old file
if os.path.exists(upload_obj):
    print('Delete 7z file')
    os.remove(upload_obj)

print('Upload S3 done')
