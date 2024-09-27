import json
import boto3
import requests

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # Extract command from Discord webhook
    command = event['body']
    
    # Change this to your EC2 instance ID
    instance_id = 'i-xxxxxxxxxxxxxxxxx'
    
    if 'start' in command:
        ec2.start_instances(InstanceIds=[instance_id])
        response_message = f"Started EC2 instance: {instance_id}"
    elif 'stop' in command:
        ec2.stop_instances(InstanceIds=[instance_id])
        response_message = f"Stopped EC2 instance: {instance_id}"
    else:
        response_message = "Unknown command. Use 'start' or 'stop'."

    # Respond back to Discord (optional)
    requests.post(
        'YOUR_DISCORD_WEBHOOK_URL',
        json={'content': response_message}
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response_message)
    }
