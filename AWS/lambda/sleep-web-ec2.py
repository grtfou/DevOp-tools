"""
Stop a EC2 instance and release ip.

Then set Router 53 to local.
"""

import os
import sys

root = os.environ["LAMBDA_TASK_ROOT"]
sys.path.insert(0, root)

import boto3
from boto3.session import Session

AWS_KEY_ID = 'YourIAMID'
AWS_SECRET_KEY = 'YourIAMSecretKey'

INSTANCE_ID = 'i-example'
REGION_NAME = 'YourEC2Region'

HOSTED_ZONE_ID = 'YourRouter53ZoneID'
RECORD_NAME = 'your.web.domain'


def lambda_handler(event, context):
    session = Session(aws_access_key_id=AWS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_KEY,
                      region_name=REGION_NAME)

    ec2 = session.resource('ec2')
    instance = ec2.Instance(INSTANCE_ID)

    client = boto3.client('ec2')

    # don't keep ip
    myinstance_ip = client.describe_addresses(
        PublicIps=[instance.public_ip_address])

    ip_allocation_id = myinstance_ip['Addresses'][0]['AllocationId']

    client.release_address(
        AllocationId=ip_allocation_id
    )

    # set Router 53
    client_r53 = boto3.client('route53')

    client_r53.change_resource_record_sets(
        HostedZoneId=HOSTED_ZONE_ID,
        ChangeBatch={
            'Comment': 'release ip',
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': RECORD_NAME,
                        'Type': 'A',
                        'TTL': 300,
                        'ResourceRecords': [
                            {
                                'Value': '127.0.0.1'
                            }
                        ]
                    }
                },
            ]
        }
    )

    # stop instance
    instance.stop()
    return True
