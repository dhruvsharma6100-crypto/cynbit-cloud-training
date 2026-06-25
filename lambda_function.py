def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Cloud'
    }

if __name__ == "__main__":
    result = lambda_handler({}, {})
    print(result)