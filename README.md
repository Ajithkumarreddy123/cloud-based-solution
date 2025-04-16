# 🧠 AWS Image Recognition Pipeline (S3 + Lambda + Rekognition + DynamoDB)

This project demonstrates an automated image recognition workflow using AWS services. When an image is uploaded to **Amazon S3**, it triggers a **Lambda function** that uses **Amazon Rekognition** to analyze the image. The detected labels and their confidence scores are then stored in **Amazon DynamoDB**.

---

## 🚀 Features

- 📤 Upload images to S3
- ⚡ Automatically triggers AWS Lambda
- 🔍 Detects image labels using Rekognition
- 🗂️ Stores results in DynamoDB

---

## 🧱 Architecture

[S3 Bucket] ---> (Trigger) ---> [Lambda Function] ---> [Rekognition] | v [DynamoDB Table]


---

## 🛠️ AWS Services Used

- **Amazon S3** – To store uploaded images
- **AWS Lambda** – To process images and invoke Rekognition
- **Amazon Rekognition** – To detect labels in the image
- **Amazon DynamoDB** – To store the detected labels and metadata

---

## 🔄 How It Works

1. ✅ A user uploads an image to an **S3 bucket**.
2. ⚡ An **S3 event** triggers the **Lambda function**.
3. 🧠 Lambda uses **Rekognition** to analyze the image and extract labels.
4. 🗃️ The labels and their confidence scores are saved to **DynamoDB**.

---

## 🗂️ DynamoDB Table Schema

| Attribute   | Type   | Description                        |
|-------------|--------|------------------------------------|
| ImageName   | String | Name of the uploaded image         |
| Label       | String | Detected label (e.g., 'Dog')       |
| Confidence  | Number | Confidence score (e.g., 98.7)      |

---

## ⚙️ Setup Instructions

1. **Create an S3 Bucket**
   - Enable event notifications for `ObjectCreated`.

2. **Create a DynamoDB Table**
   - Partition key: `ImageName` (String)

3. **Create and Deploy a Lambda Function**
   - Set the S3 bucket as the trigger.
   - Add IAM permissions for:
     - `s3:GetObject`
     - `rekognition:DetectLabels`
     - `dynamodb:PutItem`

4. **Test the Flow**
   - Upload an image to S3.
   - Check DynamoDB for the recognized labels.

---
# For help or queries feel free to reach out me through mail ajithbhumireddy30@gmail.com
Let me know if you need the full Lambda code or a CloudFormation/CDK deployment template!
