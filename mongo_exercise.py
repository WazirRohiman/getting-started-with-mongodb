from pymongo import MongoClient
user = 'root'
password = '---'
host = 'localhost'

#create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

#connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# select the 'training database
db = connection.training

#select the mongodb_glossary collection
collection = db.mongodb_glossary

#insert the documents 
#first create a list to inser the documents
glossary_list = [ 
    {"database":"a database contains collections"},

    {"collection":"a collection stores the documents"},

    {"document":"a document contains the data in the form of key value pairs."}
]

# insert the documents
db.collection.insert_many(glossary_list)

# query for all documents in 'training' database and 'mongodb_glossary' collection
docs = db.collection.find()

print("Printing the documents in the mongdb_glossary collection.")

for document in docs:
    print(document)

# close the server connecton
print("Closing the connection.")
connection.close()
