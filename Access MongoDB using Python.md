Install the pymongo driver to access mongodb from python
```
python3 -m pip install pymongo
```

If you are using another environment, check with installation process for the specific environment. You can use the anaconda navigator and powershell to install to install pymongo if it's not already installed

Once completed start the mongodb server
```
start_mongo
```

Note down the Mongodb username and password for later use

Create a python program called mongo_connect.py to connect to mongodb

Execute the python file to connect
```
python3 mongo_connect.py
```

The output should be as follows
```
Connecting to mongodb server
getting list of databases
admin
config
local
Closing the connection to the mongodb server
```



