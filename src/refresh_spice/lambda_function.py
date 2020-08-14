import os
import logging

import boto3

# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# get env
ACCOUNT_ID = os.environ.get('ACCOUNT_ID')

# boto3 session
session = boto3.Session()
qs = session.client('quicksight')

def lambda_handler(event, context):
    """
    指定されたQuickSight SPICEデータセットに対して更新リクエストを送信する

    Parameters
    ----------
    event : json
        トリガーイベント情報
    context : json
        実行環境情報
    
    Returns
    ----------
    response : json
        更新処理リクエスト結果
    """
    try:
        logger.info('Check the latest ingestion')
        dataset_id = event['DataSetId']
        response = qs.list_ingestions(DataSetId=dataset_id, AwsAccountId=ACCOUNT_ID, MaxResults=1)
        ingestion_status = response['Ingestions'][0]['IngestionStatus']
        logger.info('ingestion_status: %s', ingestion_status)

        if ingestion_status in ['COMPLETED', 'FAILED']:
            logger.info('Create a ingestion')
            response = qs.create_ingestion(DataSetId=dataset_id, IngestionId=context.aws_request_id, AwsAccountId=ACCOUNT_ID)
            ingestion_status = response['IngestionStatus']
            logger.info('ingestion_status: %s', ingestion_status)

        return {
            "StatusCode": response['Status'],
            "IngestionStatus": ingestion_status
        }

    except Exception as e:
        logger.exception(e, exc_info=False)
        raise e
