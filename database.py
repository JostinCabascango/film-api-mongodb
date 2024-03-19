from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def create_mongo_connection():
    uri = "mongodb+srv://2023jostincabascango:LNAJ29OWRUrYPhfN@cluster0.rl34b4p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = None
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        client = None
    return client


def test_connection():
    client = create_mongo_connection()
    if client is not None:
        print("Connection successful!")
    else:
        print("Connection failed!")


test_connection()


def list_collections():
    client = create_mongo_connection()
    if client is not None:
        database_name = 'Films'
        db = client[database_name]
        collections = db.list_collection_names()
        print(collections)
    else:
        print("Connection failed!")


list_collections()
