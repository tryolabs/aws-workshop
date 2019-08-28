import psycopg2
import json
import boto3

client = boto3.client('ssm')

db_host = client.get_parameter(
    Name='/prod/api/DATABASE_HOST')['Parameter']['Value']
db_name = client.get_parameter(
    Name='/prod/api/DATABASE_NAME')['Parameter']['Value']
db_user = client.get_parameter(
    Name='/prod/api/DATABASE_USER')['Parameter']['Value']
db_pass = client.get_parameter(
    Name='/prod/api/DATABASE_PASSWORD', WithDecryption=True)['Parameter']['Value']

db_port = 5432


def create_conn():
    conn = None
    try:
        conn = psycopg2.connect("dbname={} user={} host={} password={}".format(
            db_name, db_user, db_host, db_pass))
    except:
        print("Cannot connect.")
    return conn


def fetch(conn, query):
    result = []
    print("Now executing: {}".format(query))
    cursor = conn.cursor()
    cursor.execute(query)
    raw = cursor.fetchall()
    for line in raw:
        result.append(line)
    return result


def lambda_handler(event, context):

    print(event)

    if 'query' in event.keys():
        query = event['query']
    else:
        query = ''

    query_cmd = "select * from articles_article where title like '%"+query+"%'"

    print(query_cmd)

    conn = create_conn()

    result = fetch(conn, query_cmd)
    conn.close()

    return {
        'statusCode': 200,
        'body': str(result)
    }
