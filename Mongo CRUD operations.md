#Different ways of querying documents

Count documents - counting the number of docs in collection 'languages'
```
db.languages.count()
```

List first document in collection
```
db.languages.findOne()
```

List all documents in collection
```
db.languages.find()
```

List first 3 documents in collection
```
db.languages.find().limit(3)
```

Query for 'Python' languages
```
db.languages.find({"name":"python"})
```

Query for 'object oriented' languages
```
db.languages.find({"name":"python"})
```


##List only specific fields.

##Using a projection document you can specify what fields we wish to see or skip in the output.

This command lists all the documents with only name field in the output.
```
db.languages.find({},{"name":1})
```

Sample output for the above
```
{ "_id" : ObjectId("63d29d67634977027e408e99"), "name" : "java" }
{ "_id" : ObjectId("63d29d67634977027e408e9a"), "name" : "python" }
{ "_id" : ObjectId("63d29d67634977027e408e9b"), "name" : "scala" }
{ "_id" : ObjectId("63d29d67634977027e408e9c"), "name" : "c" }
{ "_id" : ObjectId("63d29d6a634977027e408e9d"), "name" : "c++" }
```

This command lists all the documents without the name field in the output.
```
db.languages.find({},{"name":0})
```

Sample output for the above
```
{ "_id" : ObjectId("63d29d67634977027e408e99"), "type" : "object oriented" }
{ "_id" : ObjectId("63d29d67634977027e408e9a"), "type" : "general purpose" }
{ "_id" : ObjectId("63d29d67634977027e408e9b"), "type" : "functional" }
{ "_id" : ObjectId("63d29d67634977027e408e9c"), "type" : "procedural" }
{ "_id" : ObjectId("63d29d6a634977027e408e9d"), "type" : "object oriented" }
```

This command lists all the “object oriented” languages with only “name” field in the output.
```
db.languages.find({"type":"object oriented"},{"name":1})
```

Sample output for the above command
```
{ "_id" : ObjectId("63d29d67634977027e408e99"), "name" : "java" }
{ "_id" : ObjectId("63d29d6a634977027e408e9d"), "name" : "c++" }
```

---------------------------------------------------------------------------------------------------------------------------------------
#Updating Documents

The ‘updateMany’ command is used to update documents in a mongodb collection, and it has the following generic syntax.
```
db.<collection name>.updateMany({<what documents to find},{$set:{<what fields to set>}})
```

If ```{}``` is used then it's all documents to find

Let's add a field description with value programming language to all the documents
```
db.languages.updateMany({},{$set{"description":"programming language"}})
```

Set the creater for python language (I.e the document for the python language
```
db.languages.updateMany({"name":"python"},{$set:{"creator":"Guido van Rossum"}})
```

Set a field named compiled with a value true for all the object oriented languages
```
db.languages.updateMany({"type":"object oriented"},{$set:{"compiled":true}})
```

------------------------------------------------------------------------------------------------------------------------------------
#Delete document

To delete the 'sacla' language document
```
db.languages.remove({"name":"scala"})
```

To delete the object oriented languages
```
db.languages.remove({"type":"scala"})
```

To delete all documents in the collection
```
db.languages.remove({})
```

