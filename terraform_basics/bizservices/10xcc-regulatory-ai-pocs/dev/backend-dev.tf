# No external variables allowed in the Terraform backend block. Values have to be hardcoded.

terraform {
 backend "gcs" {
   bucket  = "tenxcc-terraform-admin-host"
   prefix  = "terraform_basics/bizservices/10xcc-regulatory-ai-pocs/dev1"
 }
}
