import boto3

# Set up the SNS client
sns = boto3.client('sns')

# Set the message content
# Replace with the recipient's phone number
phone_number = '+1234567890'  # add recipients phone number here
message = "Test Message from nnamdi"  # add message here

# Send the message
response = sns.publish(
    PhoneNumber=phone_number,
    Message=message
)

print(f"Message sent! Message ID: {response['MessageId']}")
