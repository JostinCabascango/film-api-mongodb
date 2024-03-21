from pymongo.errors import PyMongoError
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# URI de conexión a la base de datos de MongoDB.
MONGO_URI = ("mongodb+srv://2023jostincabascango:LNAJ29OWRUrYPhfN@cluster0.rl34b4p.mongodb.net/?retryWrites=true&w"
             "=majority&appName=Cluster0")


def create_mongo_connection():
    """
    Crea la conexión con la base de datos de MongoDB.
    :return:  Una instancia de MongoClient si la conexión fue exitosa, None en caso contrario.
    """
    client = None
    try:
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        client.admin.command('ping')
    except PyMongoError as e:
        # Si se produce un error, se cierra la conexión.
        if client is not None:
            client.close()
        client = None
    return client
