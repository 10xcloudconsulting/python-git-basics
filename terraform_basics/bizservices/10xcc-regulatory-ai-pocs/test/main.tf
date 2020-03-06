variable "billing_account" {}
variable "org_id" {}
variable "project_name" {}
variable "parent_folder_id" {}
variable "region" {}

provider "google" {
  region = var.region
}

module "new_project" {
  source  = "../../../../terraform_basics/modules/project"
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

output "project_id" {
    value = "${module.new_project.project_id_out}"
}
