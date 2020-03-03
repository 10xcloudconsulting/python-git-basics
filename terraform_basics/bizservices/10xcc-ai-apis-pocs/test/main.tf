variable "billing_account" {}
variable "project_name" {}
variable "parent_folder_id" {}
variable "region" {}

provider "google" {
  region = "us-central1"
}

module "new_project" {
  source  = "/Users/laks/python-git-basics/terraform_basics/modules/project"

  org_id = "" # Organization Id required if project is to be created under the Organization rather than a Folder

  billing_account = var.billing_account
  project_name = var.project_name
  parent_folder_id = var.parent_folder_id
  region = var.region
}
