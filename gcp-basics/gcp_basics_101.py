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
buckets = storage_client.list_buckets()
print(buckets)

for bucket in buckets:
    print(bucket.name)
    print(type(bucket))

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    #bucket_name = "your-bucket-name"
    #source_file_name = "/Users/laks/Downloads/MeetingSMagora1.jpg"
    #destination_blob_name = "MeetingSMagora1.jpg"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print("File {} uploaded to {}.".format(source_file_name, destination_blob_name))

def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print("Blob is : " + blob.name)

# Set parameters to call upload_blob function that uploads a file to the bucket
source_file_name = "/Users/laks/Downloads/MeetingSMagora1.jpg"
destination_blob_name = "MeetingSMagora1.jpg"

upload_blob(bucket_name, source_file_name, destination_blob_name)
list_blobs(bucket_name)
