#!/usr/bin/env python3
"""Log stats
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.01:27017')
    nginx_collection = client.logs.nginx

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    path = "path"
    status = "/status"

    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")

    for value in methods:
        count = nginx_collection.count_documents({"method": value})
        print(f"\tmethod {value}: {count}")
    print(f"{nginx_collection.count_documents({path: status})} status check")
    print("IPs:")
    print(nginx_collection.count_documents({"ip": {"$regex": "^[0-9]"}}))
