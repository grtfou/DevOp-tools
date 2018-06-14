"""
This is an example for
remote updated your new public ip to setting of security group ingress
for 80 port.

Before run this script, you need:
  * You have one security group (note the group id)
  * Created one AWS IAM users for this services
  * Bind policies to this user
    - ec2:RevokeSecurityGroupIngress
    - ec2:AuthorizeSecurityGroupIngress
"""

import os
import sys
import json
import urllib
import urllib.request as rq

from boto3.session import Session
from botocore.exceptions import ClientError

AWS_KEY_ID = ''
AWS_SECRET_KEY = ''
REGION_NAME = ''
SECURITY_GROUP = ''
FILENAME = 'public_ip.txt'


def get_public_ip():
    url = 'https://httpbin.org/ip'
    public_ip = ''
    try:
        with rq.urlopen(url) as r:
            result = json.loads(r.read())
            public_ip = result.get('origin', public_ip)

    except json.decoder.JSONDecodeError:
        print('Parse JSON format Error.')
        sys.exit()
    except urllib.error.URLError:
        print('Connect to {} fail.'.format(url))
        sys.exit()

    return public_ip


def update_ip():
    session = Session(aws_access_key_id=AWS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_KEY,
                      region_name=REGION_NAME)

    ec2 = session.client('ec2')

    try:
        # Delete old ip
        previous_ip = ''
        if not os.path.exists(FILENAME):
            print(f'Not found {FILENAME}')
            with open(FILENAME, 'w'):
                pass
        else:
            with open(FILENAME, 'r') as ii:
                previous_ip = ii.read()

            if previous_ip:
                response = ec2.revoke_security_group_ingress(
                    GroupId=SECURITY_GROUP,
                    IpPermissions=[
                        {
                            'IpProtocol': 'tcp',
                            'FromPort': 80,
                            'ToPort': 80,
                            'IpRanges': [
                                {
                                    'CidrIp': previous_ip + "/32"
                                },
                            ],
                        },
                    ]
                )
                print(response)

        # Create new ip
        new_ip = get_public_ip()
        with open('public_ip.txt', 'w') as oo:
            oo.write(new_ip)

        data = ec2.authorize_security_group_ingress(
            GroupId=SECURITY_GROUP,
            IpPermissions=[
                {'IpProtocol': 'tcp',
                 'FromPort': 80,
                 'ToPort': 80,
                 'IpRanges': [{
                     'CidrIp': new_ip + '/32',
                     'Description': 'New settings'
                 }]
                 }
            ])
        print('Ingress Successfully Set {}'.format(data))
    except ClientError as e:
        print(e)


if __name__ == '__main__':
    update_ip()
