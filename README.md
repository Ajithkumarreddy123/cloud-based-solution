# 🧠 AWS Image Recognition Pipeline (S3 + Lambda + Rekognition + DynamoDB)

This project implements an automated pipeline where an image uploaded to **Amazon S3** triggers an **AWS Lambda** function. The function uses **Amazon Rekognition** to analyze the image and stores the detected labels in **Amazon DynamoDB**.

---

## 🚀 Features

- 📤 Upload image to S3
- ⚡ Trigger Lambda on S3 `ObjectCreated` event
- 🔍 Analyze image with Rekognition
- 🗂️ Store labels and confidence scores in DynamoDB

---

## 🛠️ Architecture

```text
[S3 Bucket] ---> (Trigger) ---> [Lambda Function] ---> [Rekognition API]
                                                           |
                                                           v
                                                  [DynamoDB Table]
----

###⚙️ Services Used
Amazon S3 – Stores uploaded images

AWS Lambda – Executes backend logic

Amazon Rekognition – Detects labels in images

Amazon DynamoDB – Stores label results with metadata
------

### 🔧 How It Works
✅ Upload an image to a specified S3 bucket.

⚡ An S3 event triggers the Lambda function.

🧠 Lambda calls Rekognition to detect image labels.

🗂️ The result is formatted and saved into a DynamoDB table.
