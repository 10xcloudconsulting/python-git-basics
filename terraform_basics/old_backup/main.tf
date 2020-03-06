variable "billing_account" {}
variable "org_id" {}

provider "google" {
  region = "us-central1"
}

module "new_project" {
  source  = "./modules/project"

  billing_account = var.billing_account
  org_id = var.org_id

  project_name="test-proj-terra-2-"
  parent_folder_id="183873486743"
  region="us-central1"
}
