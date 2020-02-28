#!/usr/bin/env python3

#This file has some custom wrapper functions that work with GCP Cloud Storage Client APIs

# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = "cloudvisionapitut-268410-10xcc-python-basics-121"

def create_bucket(bucket_name):
    """Creates a new bucket."""
    # bucket_name = "your-new-bucket-name"
    # Client objest created using the default credentials for this project/env set by env variable GOOGLE_APPLICATION_CREDENTIALS

    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)

    print("Bucket {} created".format(bucket.name))

# Call the custom function create_bucket to create a new bucket
#create_bucket(bucket_name)

def list_buckets():
    """Lists all buckets."""

    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        print("Bucket name is : " + bucket.name)

# Call the custom function list_buckets
list_buckets()


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
        print("Blob: {}".format(blob.name))
        print("Bucket: {}".format(blob.bucket.name))
        print("Storage class: {}".format(blob.storage_class))
        print("ID: {}".format(blob.id))
        print("Size: {} bytes".format(blob.size))
        print("Updated: {}".format(blob.updated))
        print("Generation: {}".format(blob.generation))
        print("Metageneration: {}".format(blob.metageneration))
        print("Etag: {}".format(blob.etag))
        print("Owner: {}".format(blob.owner))
        print("Component count: {}".format(blob.component_count))
        print("Crc32c: {}".format(blob.crc32c))
        print("md5_hash: {}".format(blob.md5_hash))
        print("Cache-control: {}".format(blob.cache_control))
        print("Content-type: {}".format(blob.content_type))
        print("Content-disposition: {}".format(blob.content_disposition))
        print("Content-encoding: {}".format(blob.content_encoding))
        print("Content-language: {}".format(blob.content_language))
        print("Metadata: {}".format(blob.metadata))
        print("Temporary hold: ", "enabled" if blob.temporary_hold else "disabled")
        print(
            "Event based hold: ",
            "enabled" if blob.event_based_hold else "disabled",
        )
        if blob.retention_expiration_time:
            print(
                "retentionExpirationTime: {}".format(
                    blob.retention_expiration_time
                )
            )


# Set parameters to call upload_blob function that uploads a file to the bucket
source_file_name = "/Users/laks/Downloads/MeetingSMagora1.jpg"
destination_blob_name = "MeetingSMagora1.jpg"

upload_blob(bucket_name, source_file_name, destination_blob_name)
list_blobs(bucket_name)
