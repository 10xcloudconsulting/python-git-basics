variable "billing_account" {}
variable "org_id" {}
variable "project_name" {}
variable "parent_folder_id" {}
variable "region" {}

provider "google" {
  region = "us-central1"
}

module "new_project" {
  source  = "/Users/laks/python-git-basics/terraform_basics/modules/project"

  billing_account = var.billing_account
  org_id = var.org_id

  project_name = var.project_name
  parent_folder_id = var.parent_folder_id
  region = var.region
}

resource "google_storage_bucket" "image-store" {
  name     = "${module.new_project.project_id_out}-10xcc-gcf-ocr-images"
  location = "EU"
  project = module.new_project.project_id_out
  force_destroy = true
}

resource "google_storage_bucket" "text-store" {
  name     = "${module.new_project.project_id_out}-10xcc-gcf-ocr-texts"
  location = "EU"
  project = module.new_project.project_id_out
  force_destroy = true
}

resource "google_pubsub_topic" "topic_gcf_ocr_results" {
  name     = "${module.new_project.project_id_out}-topic-gcf-ocr-results"
  project = module.new_project.project_id_out
}

resource "google_pubsub_topic" "gcf_gcf_ocr_translate" {
  name = "${module.new_project.project_id_out}-topic-gcf-ocr-translate"
  project = module.new_project.project_id_out

}

# zip up our source code for cloud_function
data "archive_file" "hello_world_zip" {
 type        = "zip"
 source_dir  = "${path.root}/../../../../gcp-basics/cloudfunctions/helloworld/"
 output_path = "${path.root}/helloworld.zip"
}

# zip up our source code for cloud_functions - ocr app
data "archive_file" "ocr_app_tf_zip" {
 type        = "zip"
 source_dir  = "${path.root}/../../../../gcp-basics/cloudfunctions/ocr/ocr_app_tf"
 output_path = "${path.root}/ocr_app_tf.zip"
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
 bucket = "${google_storage_bucket.source_archive_bucket.name}"
 source = "${path.root}/helloworld.zip"
}

# place the zip-ed code of ocr_app_tf in the bucket
resource "google_storage_bucket_object" "ocr_app_tf_zip" {
 name   = "ocr_app_tf.zip"
 bucket = "${google_storage_bucket.source_archive_bucket.name}"
 source = "${path.root}/ocr_app_tf.zip"
}

resource "google_cloudfunctions_function" "hello_world_function" {
 name                  = "hello-world-function"
 description           = "Scheduled Hello World Function"
 available_memory_mb   = 256
 source_archive_bucket = "${google_storage_bucket.source_archive_bucket.name}"
 source_archive_object = "${google_storage_bucket_object.hello_world_zip.name}"
 timeout               = 60
 entry_point           = "hello_get"
 trigger_http          = true
 runtime               = "python37"
 project = module.new_project.project_id_out
}

output "project_id" {
    value = "${module.new_project.project_id_out}"
}
