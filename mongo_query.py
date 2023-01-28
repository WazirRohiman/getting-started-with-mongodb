from pymongo import MongoClient
user = 'root'
password = '---'
host = 'localhost'

#create connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

#connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# select the training database
db = connection.training

# select the python collection
collection = db.python

# create a sample document

doc = {"lab":"Accessing mongodb using python", "Subject":"No SQL Databases"}

# insert a sample document

print("Inserting a document into collection")
db.collection.insert_one(doc)

# query for all documents in 'training' database and 'python' colelction
docs = db.collection.find()

print("Printing the documents in the collection")

for document in docs:
    print(document)

#close the connection
print("Closing the connection")

connection.close()