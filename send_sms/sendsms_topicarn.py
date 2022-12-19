import boto3

# Create an SNS client
sns = boto3.client('sns')

# Set the phone number that you want to send the SMS message to
phone_number = '+1234567890'

# Set the message that you want to send in the SMS message
message = 'This is a test SMS message sent using the Amazon SNS service.'

# Set the topic ARN that the phone number is subscribed to
topic_arn = 'arn:aws:sns:us-east-1:123456789012:MyTopic'

# Send the SMS message
response = sns.publish(
    PhoneNumber=phone_number,
    Message=message,
    TopicArn=topic_arn
)

print(response)
