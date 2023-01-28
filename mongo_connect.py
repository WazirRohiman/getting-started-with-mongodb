#import mongoclient from pymongo class
from pymongo import MongoClient
user = 'root'
password = '---'
host = 'localhost'

#create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

#connect to the mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

#get database list
print("getting list of databases")
dbs = connection.list_database_names()

#print the database names
#iterate throug the dbs list

for db in dbs:
    print(db)

#close the connection to the server
print("Closing the connection to the mongodb server")
connection.close()
