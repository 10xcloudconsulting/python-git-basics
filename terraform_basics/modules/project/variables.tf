variable "project_name" {
  description = "Project name for the project to be created"
  default = "Default-Project"
}

variable "billing_account" {
  description = "Billing account to which this project will be linked to"
}
variable "org_id" {
  description = "Organization Id under which the project may be created. If parent_folder_id provided project created under this folder"
}

variable "parent_folder_id" {
  description = "Folder Id of the folder in which this project will be created"
}

variable "region" {
  description = "Default GCP Region in which resources of this project will be created within"
  default = "us-central1"
}
