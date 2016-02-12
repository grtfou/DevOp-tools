import os
import sys

root = os.environ["LAMBDA_TASK_ROOT"]
sys.path.insert(0, root)

import boto3
from boto3.session import Session

ACTION = 'start'    # stop

def lambda_handler(event, context):
    session = Session(aws_access_key_id='your_key',
                      aws_secret_access_key='your_secret_key',
                      region_name="ap-northeast-1")

    ec2 = session.resource('ec2')

    if ACTION == 'start':
        ec2.instances.filter(InstanceIds=['i-example']).start()
    elif ACTION == 'stop':
        ec2.instances.filter(InstanceIds=['i-example']).stop()
    return True
