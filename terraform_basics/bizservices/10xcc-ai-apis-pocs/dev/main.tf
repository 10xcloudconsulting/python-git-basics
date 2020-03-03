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
