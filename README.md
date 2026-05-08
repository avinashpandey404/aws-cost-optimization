# 🚀 AWS Cost Optimization Automation using AWS Lambda & Boto3

# 📌 Project Introduction

This project focuses on automating AWS resource monitoring and cost optimization using AWS Lambda, Python (Boto3), Amazon EventBridge, IAM Roles & Policies, EC2, EBS, and CloudWatch Logs.

The main goal of this project was to automatically identify:

- Idle EC2 instances
- Unused EC2 instances
- Unattached EBS volumes

and automatically perform cleanup actions such as:

- Stopping unnecessary EC2 instances
- Deleting unattached EBS volumes

to reduce unnecessary AWS cloud costs.

This project demonstrates:

- Serverless automation
- Infrastructure monitoring
- AWS resource management
- Cloud cost optimization
- Least privilege IAM security

---

# 🏗️ Project Architecture

```text
            Amazon EventBridge
                   ↓
         (Scheduled Trigger Rule)
                   ↓
              AWS Lambda
                   ↓
          Python Boto3 Script
                   ↓
        ┌────────────────────┐
        │                    │
        ↓                    ↓
    Amazon EC2          Amazon EBS
        ↓                    ↓
 Stop Idle EC2      Delete Unattached EBS
        ↓                    ↓
         AWS Cost Optimization
                   ↓
         CloudWatch Logs
```

---

# 🔄 Complete Workflow

```text
EventBridge Scheduled Rule
              ↓
Triggers Lambda Function
              ↓
Lambda Executes Python Script
              ↓
Boto3 Connects to AWS APIs
              ↓
Checks EC2 Instance Status
              ↓
Stops Unused EC2 Instances
              ↓
Checks EBS Volume Attachments
              ↓
Deletes Unattached EBS Volumes
              ↓
Stores Logs in CloudWatch Logs
              ↓
AWS Cloud Cost Reduced
```

---

# 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| AWS Lambda | Serverless automation |
| Amazon EC2 | Virtual servers |
| Amazon EBS | Block storage |
| Amazon EventBridge | Scheduled trigger |
| CloudWatch Logs | Monitoring & logs |
| IAM Roles & Policies | Secure permissions |
| Boto3 | AWS SDK for Python |

---

# 🎯 Project Goal

The main goal of this project was to reduce unnecessary AWS cloud billing by automatically monitoring and cleaning unused AWS resources.

---

# 📁 Project Structure

```text
aws-cost-optimization/
│
├── lambda_function.py
├── least-privilege-policy.json
└── README.md
```

---

# 🚀 STEP 1 — Understand the Problem

# 🔍 Why This Project Was Needed?

In real companies and cloud environments, developers often:

- Launch EC2 instances for testing
- Forget to stop EC2 instances
- Delete EC2 but forget EBS volumes
- Leave unused resources running

Even if resources are not being used, AWS still charges money for them.

---

# 🔍 Real Industry Scenario

```text
Developer launches EC2 server
              ↓
Testing completed
              ↓
Developer forgets to stop EC2
              ↓
AWS billing continues
```

This creates unnecessary cloud costs.

---

# 🎯 Solution

Automate resource monitoring and cleanup using:

- AWS Lambda
- EventBridge
- Python Boto3
- IAM security policies

---

# 🎯 Interview Answer

```text
This project was created to automate AWS resource cleanup and reduce unnecessary cloud costs by identifying idle EC2 instances and unattached EBS volumes using AWS Lambda and Python Boto3 automation.
```

---

# 🚀 STEP 2 — Understand AWS Lambda

# 🔍 What is AWS Lambda?

AWS Lambda is a serverless compute service provided by AWS.

Serverless means:

```text
No server management required
```

AWS automatically handles:

- Infrastructure
- Scaling
- Availability
- Runtime environment
- Server management

---

# 🔍 Why We Used Lambda?

Without Lambda:

- Need EC2 server running 24/7
- Manual script execution required
- More infrastructure management
- Additional AWS cost

With Lambda:

- Fully serverless
- Automatic execution
- Low cost
- Automatic scaling
- Easy automation

---

# 🔍 Lambda Workflow

```text
EventBridge Trigger
        ↓
Starts Lambda Function
        ↓
Lambda Executes Python Script
        ↓
Boto3 Calls AWS APIs
        ↓
EC2 & EBS Managed Automatically
```

---

# 🎯 Interview Question

## Q1. Why Lambda used in this project?

```text
AWS Lambda was used for serverless automation to automatically monitor and clean unused AWS resources without managing servers.
```

---

# 🚀 STEP 3 — Understand Source Clearly

# 🔍 What is Lambda Source?

Source means:

```text
Which AWS service triggers Lambda?
```

---

# ✅ In This Project

The source was:

```text
Amazon EventBridge
```

because EventBridge automatically triggered Lambda on a schedule.

---

# 🔍 Example

```text
Every day at specific time
        ↓
EventBridge triggers Lambda
```

---

# 🎯 Important Understanding

Source ONLY means:

```text
Who starts Lambda execution?
```

---

# 🚀 STEP 4 — Understand Services Lambda Interacted With

After Lambda started execution, it interacted with:

- Amazon EC2
- Amazon EBS

using Python Boto3 APIs.

---

# 🔍 What Lambda Did With EC2?

The Lambda function:

- Read EC2 instance details
- Checked running instance status
- Identified unused instances
- Stopped unnecessary EC2 instances

---

# 🔍 What Lambda Did With EBS?

The Lambda function:

- Checked EBS volume attachment status
- Identified unattached EBS volumes
- Deleted unused EBS storage

---

# 🚀 STEP 5 — Understand Lambda Destination Properly

# 🔍 Official AWS Meaning of Destination

Destination means:

```text
Where Lambda sends execution results after completion
```

---

# ✅ In This Project

Lambda execution logs were stored inside:

```text
Amazon CloudWatch Logs
```

---

# 🔍 Why CloudWatch Logs Used?

CloudWatch Logs stores:

- Lambda logs
- Errors
- Print statements
- Debugging information
- Monitoring information

---

# 🔍 Final Understanding

| Component | In Your Project |
|---|---|
| Source | Amazon EventBridge |
| Lambda interacted with | EC2 & EBS |
| Destination | CloudWatch Logs |

---

# 🎯 Best Interview Answer

```text
In my project, Amazon EventBridge acted as the Lambda trigger source by running the function on a schedule. The Lambda function then used Python Boto3 to interact with EC2 and EBS services for cost optimization tasks. Lambda execution logs were stored in CloudWatch Logs for monitoring and troubleshooting.
```

---

# 🚀 STEP 6 — Understand IAM Role

# 🔍 What is IAM Role?

IAM Role is an AWS identity that provides temporary permissions to AWS services.

In this project:

```text
Lambda needed permissions to access AWS resources
```

---

# 🔍 Why IAM Role Needed?

Without IAM permissions:

- Lambda cannot access EC2
- Lambda cannot access EBS
- Lambda cannot write logs

AWS blocks all actions by default for security reasons.

---

# 🔐 Principle of Least Privilege

# 🔍 What is Least Privilege?

Least privilege means:

```text
Give only required permissions, nothing extra
```

---

# 🔍 Why Least Privilege Important?

Provides:

- Better security
- Controlled access
- Reduced security risk
- Prevents unnecessary permissions

---

# 🚀 STEP 7 — Create IAM Role

Go to:

```text
IAM → Roles → Create Role
```

---

# 🔹 Trusted Entity

Choose:

```text
AWS Service
```

---

# 🔹 Use Case

Choose:

```text
Lambda
```

---

# 🔹 Role Name

```text
lambda-cost-optimization-role
```

---

# 🚀 STEP 8 — Create Least Privilege IAM Policy

# 🔍 Why Custom IAM Policy?

Using:

```text
AmazonEC2FullAccess
```

gives too many permissions.

Best practice:

```text
Use least privilege custom policy
```

---

# 📄 least-privilege-policy.json

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:StopInstances",
        "ec2:DescribeVolumes",
        "ec2:DeleteVolume"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
```

---

# 🔍 Policy Deep Explanation

| Permission | Purpose |
|---|---|
| DescribeInstances | Read EC2 information |
| StopInstances | Stop unused EC2 |
| DescribeVolumes | Read EBS information |
| DeleteVolume | Delete unattached EBS |
| CloudWatch Logs permissions | Store Lambda logs |

---

# 🚀 STEP 9 — Attach Policy to IAM Role

Attach custom policy to:

```text
lambda-cost-optimization-role
```

---

# 🚀 STEP 10 — Create Lambda Function

Go to:

```text
AWS Console → Lambda → Create Function
```

---

# 🔹 Select

```text
Author from scratch
```

---

# 🔹 Configuration

| Setting | Value |
|---|---|
| Function Name | aws-cost-optimizer |
| Runtime | Python 3.12 |
| Architecture | x86_64 |

---

# 🔹 Execution Role

Choose:

```text
Use existing role
```

Select:

```text
lambda-cost-optimization-role
```

---

# 🚀 STEP 11 — Understand Boto3

# 🔍 What is Boto3?

Boto3 is AWS SDK for Python.

It allows Python code to communicate with AWS services programmatically.

---

# 🔍 Why Boto3 Used?

Using Boto3 we can:

- Stop EC2 instances
- Delete EBS volumes
- Read AWS resources
- Automate AWS infrastructure

---

# 🎯 Interview Question

## Q1. What is Boto3?

```text
Boto3 is the AWS SDK for Python used to automate and manage AWS services programmatically.
```

---

# 🚀 STEP 12 — Write Lambda Function Code

# 📄 lambda_function.py

```python
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
```

---

# 🔍 Deep Code Explanation

# import boto3

Imports AWS SDK for Python.

---

# boto3.client('ec2')

Creates EC2 API client connection.

---

# describe_instances()

Fetches EC2 instance details.

---

# stop_instances()

Stops EC2 instances automatically.

---

# describe_volumes()

Fetches EBS volume details.

---

# delete_volume()

Deletes unattached EBS volumes.

---

# 🚀 STEP 13 — Deploy Lambda Code

Paste code inside Lambda console.

Click:

```text
Deploy
```

---

# 🚀 STEP 14 — Test Lambda Function

Click:

```text
Test
```

---

# 🔹 Create Test Event

```json
{}
```

---

# 🔹 Run Test

---

# 🔍 Expected Output

```text
Stopping instance: i-xxxxxxxx
Deleting volume: vol-xxxxxxxx
```

---

# 🚨 Common Errors & Fixes

| Error | Reason | Fix |
|---|---|---|
| AccessDenied | Missing IAM permission | Attach correct policy |
| Lambda timeout | Script running too long | Increase timeout |
| VolumeInUse | EBS attached to EC2 | Skip attached volumes |
| ClientError | Wrong AWS region | Verify AWS region |
| Rate exceeded | Too many API calls | Reduce execution frequency |

---

# 🚀 STEP 15 — Create EventBridge Scheduled Rule

Go to:

```text
Amazon EventBridge → Rules → Create Rule
```

---

# 🔹 Rule Type

```text
Schedule
```

---

# 🔹 Schedule Expression

Example:

```text
rate(1 day)
```

---

# 🔍 Meaning

Runs Lambda:

```text
Every 1 day automatically
```

---

# 🔹 Target

Choose:

```text
Lambda Function
```

Select:

```text
aws-cost-optimizer
```

---

# 🚀 STEP 16 — Verify Automation

# 🔹 Check EC2

Unused EC2 instances should stop automatically.

---

# 🔹 Check EBS

Unattached EBS volumes should delete automatically.

---

# 🔹 Check Logs

Go to:

```text
CloudWatch → Log Groups
```

---

# 🔍 Why Logs Important?

Logs help debug:

- Permission issues
- Runtime failures
- API failures
- Execution problems

---

# 🎯 Detailed Explanation of Project Features

# 🖥️ Automated Detection of Unused EC2 Instances

The automation continuously checks EC2 instances to identify servers that are:

- Idle
- Running unnecessarily
- Underutilized
- Not actively being used

---

# 🔍 Why This Important?

Running EC2 instances continuously increases AWS billing even when servers are unused.

Automation helps reduce unnecessary cloud spending.

---

# 💾 Identification and Cleanup of Unattached EBS Volumes

Sometimes EC2 instances are deleted but EBS volumes remain.

Unused EBS volumes still generate AWS charges.

The automation identifies unattached EBS volumes and deletes them automatically.

---

# ⚡ Serverless Automation using AWS Lambda

AWS Lambda was used to automate infrastructure cleanup without managing servers.

Benefits:

- Fully serverless
- Automatic scaling
- Lower cost
- High availability
- Easy automation

---

# ⏰ Scheduled Monitoring using EventBridge

EventBridge automatically triggers Lambda on schedule.

Example schedules:

```text
Every 1 hour
Every 1 day
Every week
```

---

# 🔐 Secure Access Management using IAM Roles & Policies

IAM Roles & Policies securely control Lambda permissions.

The project followed:

```text
Principle of Least Privilege
```

to provide only required permissions.

---

# 🎯 Important Interview Questions

# Q1. Why Lambda used in this project?

```text
Lambda was used for serverless automation to automatically monitor and clean unused AWS resources.
```

---

# Q2. Why EventBridge used?

```text
EventBridge was used to schedule automatic Lambda execution.
```

---

# Q3. Why Least Privilege important?

```text
Least privilege improves security by providing only required permissions to Lambda.
```

---

# Q4. What problem does this project solve?

```text
This project reduces unnecessary AWS cloud costs by automatically stopping unused EC2 instances and deleting unattached EBS volumes.
```

---

# 🧠 Key Learnings

Through this project I learned:

- AWS Lambda
- Python Boto3
- IAM Security
- Least Privilege Access
- EventBridge Scheduling
- EC2 Automation
- EBS Cleanup
- CloudWatch Monitoring
- Serverless Architecture
- AWS Cost Optimization
- Infrastructure Automation
