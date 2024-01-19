import json
import logging
import os

import boto3


def request_by_lambda_invoke(lambda_name, payload, invocation_type):
    lambda_client = boto3.client("lambda", region_name="us-east-1")

    try:
        response = lambda_client.invoke(
            FunctionName=lambda_name,
            InvocationType=invocation_type,  # or 'Event' for asynchronous
            Payload=json.dumps(
                {"key": "value"}
            ),  # data to send to the Lambda function
        )

        return json.loads(response["Payload"].read())
    except Exception as e:
        logging.error(e)

        raise e


def lambda_handler(event, context):
    logging.info(f"event: {event}")

    try:
        update_task_function = os.getenv("UPDATE_TASK_FUNCTION")
        res = request_by_lambda_invoke(
            update_task_function, "", "RequestResponse"
        )
        data = {
            "data": json.dumps(res),
            "message": "Hello World from CREATE tags lambda function!",
        }

        return {"statusCode": 200, "body": json.dumps(data)}
    except Exception as e:
        # logging.error(format(e))
        return {"statusCode": 500, "body": {"message": e}}
