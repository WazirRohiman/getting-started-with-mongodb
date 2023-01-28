Start the MongDB server and connect to the client
Use the following command to build a database called training and insert the sample data into the collections 'marks'
```
use training
db.marks.insert({"name":"Ramesh","subject":"maths","marks":87})
db.marks.insert({"name":"Ramesh","subject":"english","marks":59})
db.marks.insert({"name":"Ramesh","subject":"science","marks":77})
db.marks.insert({"name":"Rav","subject":"maths","marks":62})
db.marks.insert({"name":"Rav","subject":"english","marks":83})
db.marks.insert({"name":"Rav","subject":"science","marks":71})
db.marks.insert({"name":"Alison","subject":"maths","marks":84})
db.marks.insert({"name":"Alison","subject":"english","marks":82})
db.marks.insert({"name":"Alison","subject":"science","marks":86})
db.marks.insert({"name":"Steve","subject":"maths","marks":81})
db.marks.insert({"name":"Steve","subject":"english","marks":89})
db.marks.insert({"name":"Steve","subject":"science","marks":77})
db.marks.insert({"name":"Jan","subject":"english","marks":0,"reason":"absent"})
```

Print only two documents from the 'marks' collection
```
use training
db.marks.aggregate([{"$limit":2}])
```

Use the ```$sort``` command to sort the output 

In assending order: 
```
db.marks.aggregate([{"$sort":{"marks":1}}])
```

In descending order:
```
db.marks.aggregate([{"$sort":{"marks":-1}}])
```

**Aggregation usually involves using more than one operator.
A pipeline consists of one or more operators declared inside an array.
The operators are comma separated.
Mongodb executes the first operator in the pipeline and sends its output to the next operator.**

Create a two stage pipeline that answers the question “What are the top 2 marks?”

```
db.marks.aggregate([
{"$sort":{"marks":-1}},
{"$limit":2}
]}
```

**The operator $group by, along with operators like $sum, $avg, $min, $max, allows us to perform grouping operations.**

This aggregation pipeline below prints the average marks across all subjects

```$subject``` or ```$marks``` are referencing to the fields

```%group``` refers to the aggregator 'group by'
"average" is what we want to call the ouput field as
```$avg``` is the average aggregator

```
db.marks.aggregate([
{
  "%group":{
        "_id":"$subject", "average":{"$avg":"$marks"}
            }
}
])
```
The output format of the above command will look like this 

```
{ "_id" : "english", "average" : 62.6 }
{ "_id" : "science", "average" : 77.75 }
{ "_id" : "maths", "average" : 78.5 }
```

The above query is equivalent to the SQL query below
```
SELECT subject, average(marks)
FROM marks
GROUP BY subject
```

---------------------------------------------------------------------------------------------------

** To answer the question “Who are the top 2 students by average marks?” **
The steps are as follows

Write the aggregator pipeline: 
- To find the average marks per students
- sort the output based on average marks in descending order
- limit the output to two documents

```
db.marks.aggregate([
{
  "$group":{
      "_id":"$name",
      "average":{"$avg":"$marks"}
      }
},
{
   "$sort":{"average":-1}
},
{
   "$limit":2
}
])
```

The output will be as followed

```
{ "_id" : "Alison", "average" : 84 }
{ "_id" : "Steve", "average" : 82.33333333333333 }
```

-------------------------------------------------------------------------------------------------------
To find the max marks score in each subjects
```
db.marks.aggregate([
    {
        "$group":{"_id":"$subject","max_marks":{"$max":"$marks"}}
    }
])
```

To find the min marks by each students
```
db.marks.aggregate([
{
  "$group":{"_id":"$name","min_marks":{"$min":"$marks"}}
 }
 ])
```

To find the two subject based on average marks
```
db.marks.aggregate([
{
  "$group":{
      "_id":"$subject",
      "average":{"$avg":"$marks"}
      }
},
{
   "$sort":{"average":-1}
},
{
   "$limit":2
}
])
```

Exit the cli
```
exit
```
 

