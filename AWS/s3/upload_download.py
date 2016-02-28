#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @date        160212
"""
Upload and download file from S3
"""
import configparser

from boto3.session import Session

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
# -

session = Session(aws_access_key_id=conf['AWS_KEY_ID'],
                  aws_secret_access_key=conf['AWS_SECRET_KEY'],
                  region_name=conf['REGION_NAME'])


s3 = session.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)

# upload
bucket = s3.Bucket(conf['BUCKET_NAME'])
upload_obj = '中文.txt'
target_key = 'test.txt'
try:
    obj = bucket.Object(target_key)
    obj.upload_file(upload_obj)
except FileNotFoundError:
    print('cover file')
    with open(upload_obj, 'rb') as data:
        bucket.put_object(Key=target_key, Body=data)

# download
new_filename = '我的新中文.txt'
try:
    obj = bucket.Object(target_key)
    obj.download_file(new_filename)
except FileNotFoundError:
    print('File Not Found')
print('done')
