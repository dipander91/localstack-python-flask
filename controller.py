import boto3
import config
import logging
 
# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

boto3.setup_default_session(profile_name=config.AWS_PROFILE)

#DynamoDB client as per the environment. In case of local development, ddb_client to use localstack dynamodb.
try: 
    if config.APP_ENVIRONMENT == 'local':
        
        ddb_client = boto3.client(
            'dynamodb',
            region_name=config.AWS_REGION,
            endpoint_url=config.ENDPOINT_URL)
    else:
        ddb_client = boto3.client(
            'dynamodb',
            region_name=config.AWS_REGION)
except Exception:
    print("DynamoDB client error in controller")  

def add_employee(id, name, city, age):
   response = ddb_client.put_item(
       TableName=config.DDB_TABLE_NAME,
       Item={'employeeId':{'S':id},
             'name':{'S':name},
             'city':{'S':city},
             'age':{'S':age}
             }
   )
   return response

def get_employee(id):
#    response = ddb_client.get_item(
#        TableName=config.DDB_TABLE_NAME,
#        Key={'employeeId':{'S':id}}
#    )
   response = ddb_client.query(
    TableName=config.DDB_TABLE_NAME,
    KeyConditionExpression='employeeId = :employeeId',
    ExpressionAttributeValues={
        ':employeeId': {'S': id}
    }
    )
   results = {}
   count = response['Count']
   for i in range(0, count):
        globals()['emp_list_' + str(i)] = []
        globals()['emp_list_' + str(i)].append(response['Items'][i]['employeeId']['S'])
        globals()['emp_list_' + str(i)].append(response['Items'][i]['name']['S'])
        globals()['emp_list_' + str(i)].append(response['Items'][i]['city']['S'])
        globals()['emp_list_' + str(i)].append(response['Items'][i]['age']['S'])
        results[i]=globals()['emp_list_' + str(i)]
   return results

#get_employee('133')

def list_tables():
    response = ddb_client.list_tables()
    return response