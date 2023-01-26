Starting the MongoDB server
```
start_mongo
```

Copy the command that appears in the terminal. It will contain the username and password in the following format
```
mongo -u <username> -p <password> --authenticationDatabase admin local
```

Use the command above (with your username and password) to connect to mongodb client in the terminal

Once connected, you can find the version using the following command
```
db.version()
```

Use the following command to list the database
```
show dbs
```

The following command will create a new database named 'training'. If a database named 'training' already exists, it will start using it.
```
use training
```

The following command will create a collection name 'mycollection' inside the 'training' database
```
db.createCollection("mycollection")
```

Print the list of collections in the current database
```
show collections
```

The command below will insert a JSON document into the collection. The format is as follows
```
db.<collection_name>.insert(<JSON documentation>)
```
Example:
```
db.mycollection.insert({"color":"white","Example":"Milk"})
```

Use the following command to count the number of documents in the collection(in this case in the collection 'mycollection')
```
db.mycollection.count()
```

The following command lists all the documents in the collection mycollection

Notice that mongodb automatically adds an '_id' field to every document in order to uniquely identify the document.
```
db.mycollection.find()
