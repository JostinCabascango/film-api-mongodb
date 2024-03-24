from pymongo.errors import PyMongoError
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB database connection URI.
MONGO_URI = ("mongodb+srv://2023jostincabascango:LNAJ29OWRUrYPhfN@cluster0.rl34b4p.mongodb.net/?retryWrites=true&w"
             "=majority&appName=Cluster0")


def create_mongo_connection():
    """
       Establishes a connection with the MongoDB database.
       :return: A MongoClient instance if the connection was successful, None otherwise.
       """
    client = None
    try:
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        client.admin.command('ping')
    except PyMongoError as e:
        # If an error occurs, the connection is closed.
        if client is not None:
            client.close()
        client = None
    return client
