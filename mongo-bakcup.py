#!/usr/bin/python
import os, sys, datetime, json, pymongo, subprocess
from pymongo import MongoClient
host = "localhost" ##Database Server
dirName = "/mnt/"  ##Path of backup directory
now  = datetime.datetime.now()
date = (now.strftime("%Y%m%d"))
client = MongoClient('localhost', 27017)
val = client.list_database_names()
os.chdir(dirName)
os.mkdir(date)
for database in val:
    print(database)
    print (client[database].list_collection_names())
    col = (client[database].list_collection_names())
    print(date)
    os.chdir(dirName)
    os.chdir(date)
    os.mkdir(database)
    #import ipdb;ipdb.set_trace();
    for collection in col:
        command = "mongoexport --host {} --db {} --collection {} --pretty --out {}/{}.json".format(host,database,collection,database,collection)
        os.system(command)
