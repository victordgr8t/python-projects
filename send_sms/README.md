SEND TEXT MESSAGES USING AMAZON SNS & PYTHON (Boto3)


In this mini project, I wrote a python script on how to send SMS messages to a phone number using Python and the AWS SDK for Python (Boto3).

Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2.


Prerequisites
Before you begin, make sure you have the following:

An AWS account. If you don't have one, you can create one for free at aws.amazon.com.
Python 3.10.9 or latest version. You can check your Python version by running the following command: python -V
The AWS CLI (Command Line Interface) installed and configured on your machine.
Setting up Amazon CLI

The AWS Command Line Interface (CLI) is a unified tool used to manage your AWS services. With the AWS CLI, you can control multiple AWS services from the command line, and automate them through scripts.


To set up the AWS CLI on your machine, follow these steps:
Install Python 3.10.9 or latest version. You can check your Python version by running the following command:
$ python3 --version

Install pip, the Python package manager. You can install pip by running the following command:
$ python3 -m ensurepip

Install the AWS CLI. You can install the AWS CLI by running the following command:
$ pip3 install awscli


Configure the AWS CLI. You can configure the AWS CLI by running the aws configure command and following the prompts. You will need to provide your AWS access key and secret key, as well as the default region and output format. You can obtain your access key and secret key by signing in to the AWS Management Console and navigating to the IAM (Identity and Access Management) dashboard.

After you have installed and configured the AWS CLI, you can use it to manage your AWS resources from the command line. For example, to list all the S3 buckets in your account, you can use the command:
$ aws s3 ls


Setting up Amazon SNS
To send an SMS message using Amazon SNS, you need to set up in several ways. 
Find below two steps to setup Amazon SNS.


Step 1

login to your aws account,
then type in sns on the search bar.
Click menu bar on the left
Scroll down to Mobile then click 'Text messaging (SMS)'
Scroll down and click add phone number.
Add your phone number and select a language the verification message will be sent in, then add phone number.
Input the verification code and then click verify phone number If done correctly you should see your number as verified below
Image description

Step 2

Sign in to the AWS Management Console and navigate to the Amazon SNS dashboard.
Click the Create topic button.
Enter a Topic name and a Display name for your topic, and then click the Create topic button.
In the Subscriptions tab, click the Create subscription button.
Select SMS as the Protocol and enter the phone number that you want to subscribe to the topic.
Click the Create subscription button to subscribe the phone number to the topic.
Sending SMS messages with Python



Now that you have set up an SNS topic and subscribed a phone number to the topic, you can use Python and the Boto3 library to send SMS messages to the phone number.

First, install the Boto3 library by running the following command:
$ pip3 install boto3

Next, create a Python script and import the boto3 library. Then, create an SNS client using the following code:

import boto3
sns_client = boto3.client('sns')


create three variables one for phone number and the other for message. Add the contents of your message and the actual phone number that will receive the message in the defined variables.

phone_number = '+1234567890'
message = "This is a test message sent from Nnamdi using Amazon SNS and python."
# Set the topic ARN that the phone number is subscribed to
topic_arn = 'arn:aws:sns:us-east-1:123456789012:MyTopic'


To send an SMS message, you can use the publish() method of the client object. The publish() method requires the following parameters:

PhoneNumber: The phone number to which you want to send the SMS message.
Message: The content of the SMS message.
TopicArn: A unique identifier for a topic in the Amazon Simple Notification Service (SNS). A topic is a logical access point and communication channel for allowing messages to be published to subscribing endpoints or clients.

Here is an example of how to send an SMS message using the publish() method:

# Send the SMS message
response = sns.publish(
    PhoneNumber=phone_number,
    Message=message,
    TopicArn=topic_arn
)


Next and final step print out the code which will notify you a response if the message fails or sends successfully. It will also display the message ID

print(f"Message sent! Message ID: {response['MessageId']}")
This will send the SMS message to the phone number that is subscribed to the specified SNS topic.



Note that the phone number that you are sending the SMS message to must be subscribed to the SNS topic that you are specifying in the TopicArn parameter.

Alternatively you can choose to send to the verified number I showed you earlier and take out the SNS TopicArn line of code like below

phone_number = '+1234567890'  # add recipients phone number here
message = "Test Message from nnamdi"  # add message here


response = sns_client.publish(
    PhoneNumber=phone_number,
    Message=message
)


NB: The number we verified is in the SMS Sandbox in US East(North Virginia) region. When in the sandbox, you can only deliver SMS to the sandbox destination phone numbers you have verified.
When your account is moved out of the sandbox, these restrictions are removed, and you can send SMS messages to any recipient.
To move your account out of the sandbox click the link to get detailed steps from https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox-moving-to-production.html

I hope this helps! Let me know if you have any questions
