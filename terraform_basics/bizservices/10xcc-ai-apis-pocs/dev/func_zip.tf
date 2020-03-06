# zip up our source code for cloud_function
data "archive_file" "hello_world_zip" {
 type        = "zip"
 source_dir  = "${path.root}/../../../../gcp-basics/cloudfunctions/helloworld/"
 output_path = "${path.root}/helloworld.zip"
}

# create the storage bucket
resource "google_storage_bucket" "source_archive_bucket" {
 name   = "${module.new_project.project_id_out}-10xcc-gcf-archive-files"
 project = module.new_project.project_id_out
 force_destroy = true
}

# place the zip-ed code in the bucket
resource "google_storage_bucket_object" "hello_world_zip" {
 name   = "helloworld.zip"
 bucket = google_storage_bucket.source_archive_bucket.name
 source = "${path.root}/helloworld.zip"
}

# Test with hello world function deployment
resource "google_cloudfunctions_function" "hello_world_function" {
 name                  = "hello-world-function"
 description           = "Scheduled Hello World Function"
 available_memory_mb   = 256
 source_archive_bucket = google_storage_bucket.source_archive_bucket.name
 source_archive_object = google_storage_bucket_object.hello_world_zip.name
 timeout               = 60
 entry_point           = "hello_get"
 trigger_http          = true
 runtime               = "python37"
 project = module.new_project.project_id_out
}
