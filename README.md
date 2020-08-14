# aws-respice

aws-respice refreshes Amazon QuickSight SPICE Datasets.

## Description

AWS Services what to be called are below.

- AWS Lambda
- Amazon QuickSight

## Install

This app is created to be deployed by AWS SAM(Serverless Application Model).

To install the AWS SAM CLI, see following pages.

[Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

```bash
git clone https://github.com/tosh223/aws-respice.git
cd ./aws-respice
sam build
sam deploy --guided
```

## Usage

Call a Lambda function 'respice' with event like below.

```json
{
    "DataSetId": "your-DataSetId"
}
```

QuickSight DataSetId is shown by the following aws-cli command.

```bash
aws quicksight list-data-sets --aws-account-id "your-AccountId"
```
