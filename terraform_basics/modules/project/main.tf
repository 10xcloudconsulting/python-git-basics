resource "random_id" "id" {
  byte_length = 4
  prefix      = var.project_name
}

resource "google_project" "project" {
  name            = "${var.project_name}"
  project_id      = random_id.id.hex
  billing_account = "${var.billing_account}"
  folder_id       = "${var.parent_folder_id}"
}

resource "google_project_service" "service" {
  for_each = toset([
    "compute.googleapis.com", "storage-component.googleapis.com", "pubsub.googleapis.com", "cloudfunctions.googleapis.com", "translate.googleapis.com", "vision.googleapis.com"
  ])

  service = each.key

  project = google_project.project.project_id
  disable_on_destroy = false
}
