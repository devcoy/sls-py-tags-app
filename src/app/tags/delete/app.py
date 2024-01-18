import json
import logging


def lambda_handler(event, context):
    try:
        logging.info(f"event: {event}")
        data = {
            "data": None,
            "message": "Hello World from DELETE tags lambda function!",
        }

        return {"statusCode": 200, "body": json.dumps(data)}
    except Exception as e:
        logging.error(format(e))
        return {"statusCode": 500, "body": {"message": json.dumps(e)}}
