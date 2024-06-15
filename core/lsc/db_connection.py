from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def check_and_create_db_collection(database_name, collection_name):
    try:
        client = MongoClient('mongodb://localhost:27017')
        client.admin.command('ping')
        print("Connection to MongoDB: ok")

        db_list = client.list_database_names()

        if database_name in db_list:
            db = client[database_name]
            print(f"The database '{database_name}' exists.")
        else:
            db = client[database_name]
            print(f"The database '{database_name}' did not exist and has been created.")

        collection_list = db.list_collection_names()

        if collection_name in collection_list:
            print(f"The collection '{collection_name}' exists in the database '{database_name}'.")
        else:
            db.create_collection(collection_name)
            print(
                f"The collection '{collection_name}' did not exist and has been created in the database '{database_name}'.")

    except ConnectionFailure:
        print("Connection to MongoDB failed")


# check_and_create_db_collection('LSCDb', 'systemcall')
