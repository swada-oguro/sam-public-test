import json

# import requests


def lambda_handler(event, context):
    
    
    # アクセスキーを直接書く！！！！！
    aws_access_key_id = "Aaaee4DMreaereH3Y5B4AAJQ"
    aws_secret_access_key = "dttee7VffyrerereIOTCreeereEnqMDZfy2EZ5eeRp"

    print(aws_access_key_id)
    print(aws_secret_access_key)
    
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }

# main
if __name__ == "__main__":
    
    print("test")
    
    lambda_handler(None, None)

