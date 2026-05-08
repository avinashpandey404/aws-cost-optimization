import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    # Get EC2 instance information

    instances = ec2.describe_instances()

    for reservation in instances['Reservations']:

        for instance in reservation['Instances']:

            instance_id = instance['InstanceId']

            state = instance['State']['Name']

            # Stop running EC2 instances

            if state == 'running':

                print(f"Stopping instance: {instance_id}")

                ec2.stop_instances(
                    InstanceIds=[instance_id]
                )

    # Get EBS volume information

    volumes = ec2.describe_volumes()

    for volume in volumes['Volumes']:

        # Check unattached volumes

        if len(volume['Attachments']) == 0:

            volume_id = volume['VolumeId']

            print(f"Deleting volume: {volume_id}")

            ec2.delete_volume(
                VolumeId=volume_id
            )

    return {
        'statusCode': 200,
        'body': 'AWS Cost Optimization Completed'
    }
