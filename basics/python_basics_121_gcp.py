#!/usr/bin/env python3

#This file explores some basics for using GCP

# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = "cloudvisionapitut-268410-10xcc-python-basics-121"

# Creates the new bucket
#bucket = storage_client.create_bucket(bucket_name)

#print("Bucket {} created.".format(bucket.name))

# List the buckets
buckets = list(storage_client.list_buckets())
print(buckets)
