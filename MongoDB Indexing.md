    Let us insert a lot of documents into the newly created collection.
    This should take around 3 minutes, so please be patient.
    The code given below will insert 200000 documents into the ‘bigdata’ collection.
    Each document would have a field named account_no which is a simple auto increment number.
    And a field named balance which is a randomly generated number, to simulate the bank balance for the account.
    
```
use training
for (i=1;i<=200000;i++){print(i);db.bigdata.insert({"account_no":i,"balance":Math.round(Math.random()*1000000)})}
```

Count to check if all documents were inserted
```
db.bigdata.count()
```

Let us run a query and find out how much time it takes to complete.
Let us query for the details of account number 58982.
We will make use of the explain function to find the time taken to run the query in milliseconds
```
db.bigdata.find({"account_no":58982}).explain("executionStats").executionStats.executionTimeMillis
```
Took 113 milliseconds

Before you create an index, choose the field you wish to create an index on. It is usually the field that you query most. In the case below we'll be creating an index on the 'account_no'
```
db.bigdata.createIndex({"account_no":1})
```

To get a list of the indexes in the bigdata collection, run the following command
```
db.bigdata.getIndexes()
```

Since we create an index on the 'account_no' when you run the above command to get the list of indexes, you should see an index called ```account_no_1```

Now let's run a query and find out how much time it takes to complete, using an index.

Let us query for the details of account number 69271

```
db.bigdata.find({"account_no":69271}).explain("executionStats").executionStats.executionTimeMillis
```
Took 0 millisecond

Now delete the index we create earlier
```
db.bigdata.dropIndex({"account_no":1})
```
