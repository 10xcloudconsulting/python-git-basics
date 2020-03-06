terraform {
 backend "gcs" {
   bucket  = "tenxcc-terraform-admin-host"
   prefix  = "terraform/state"
 }
}
