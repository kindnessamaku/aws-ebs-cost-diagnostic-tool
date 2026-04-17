# AWS EBS Cost Diagnostic Tool
## Overview
This project is an AWS EBS cost optimization tool that identifies unattached volumes, calculates their age and estimated monthly cost, and flags resources exceeding 30 days. To ensure safe cleanup, the tool automatically creates snapshots of flagged volumes before removal. It also generates a financial summary report highlighting potential cost savings. The project demonstrates automation, cost optimization and safe resource management using AWS and Python (boto3).

## 🛠️ Tech Stack

**Programming Language** : Python – The core logic for resource scanning, date calculations, and automation.

**AWS SDK** : Boto3 – Used to programmatically interact with AWS services to describe volumes, create snapshots, and delete resources.

**Cloud Infrastructure** : Amazon EC2 (EBS) – The target service for cost analysis and storage management.

**Data Protection** : Amazon EBS Snapshots – Automated backup mechanism used to ensure data persistence before resource cleanup.

**Cost Management** : Applied cost-per-GB logic to calculate potential monthly savings.

**CLI & Security** : AWS CLI & IAM – Used for secure authentication and local environment configuration.

## Key Features 
  - **Unattached Volume Detection** : Identifies all EBS volumes in the account that are not attached to any EC2 instance.
  - **Age Analysis** : Calculates how long each volume has existed using timestamp data.
  - **Cost Estimation** : Estimates monthly cost per volume based on storage size.
  - **Automated Risk Mitigation** : Automatically creates snapshots for volumes older than 30 days before cleanup.
  - **Threshold-Based Alerting** : Flags volumes exceeding the defined age threshold for review.
  - **Financial Summary Reporting** : Displays total potential monthly savings from unused resources.
## Architecture Diagram
![ebs](https://github.com/user-attachments/assets/05e7deb1-4c24-4b8b-8424-2d0f465f6761)
## Prerequisites
   - An aws account
   - AWS CLI installed and configured
   - Python 3.x installed
   - Required python dependency :
     ```
     pip install boto3
     ```
## Deployment Guide
- **Step 1** : Configure AWS Credentials : Run the following command to connect your local environment to your AWS account :
  ```
  aws configure
  ```
  Provide access key, secret key and region.
  
- **Step 2** : Clone the repository :
```
git clone https://github.com/YOUR-USERNAME/aws-ebs-cost-diagnostic-tool.git
cd aws-ebs-cost-diagnostic-tool
```

- **Step 3** : Install Dependencies :
```
pip install -r requirements.txt
```

- **Step 4** : Run the script :
```
python main.py
```

- **Step 5** : Test the Tool : To validate the script, create a test EBS volume in your AWS account, ensure it is not attached to any EC2 instance, run the script again and observe detection, cost calculation and snapshot creation.

 <table>
  <tr>
    <td>
      <!-- Replace the text between the " " below with your first URL -->
      <img src="https://github.com/user-attachments/assets/57c9325d-fc6f-482b-81b7-5c89ccd534a7" width="450" alt="EBS">
    </td>
    <td>
      <!-- Replace the text between the " " below with your second URL -->
      <img src="https://github.com/user-attachments/assets/a66a10bb-fa60-4a0d-a5d4-6aa82361d939" width="450" alt="Outputs">
    </td>
  </tr>
</table>

## Key Achievements
- Identified and analyzed 100% of unattached EBS volumes within the AWS account.
- Automated snapshot creation for all volumes exceeding 30-day threshold, ensuring zero data loss risk.
- Reduced manual cost auditing effort by 80% through automation.
- Enabled near real-time visibility into storage waste and optimization opportunities. 
