# To deploy the image processing function with a Cloud Storage trigger
# gcloud functions deploy ocr-extract --runtime python37 --trigger-bucket YOUR_IMAGE_BUCKET_NAME --entry-point process_image

resource "google_cloudfunctions_function" "ocr_extract" {
 name                  = "ocr-extract"
 description           = "Image Processing Function with a Storage Trigger"
 available_memory_mb   = 256
 source_archive_bucket = google_storage_bucket.source_archive_bucket.name
 source_archive_object = google_storage_bucket_object.ocr_app_tf_zip.name
 timeout               = 60
 entry_point           = "process_image"
 runtime               = "python37"
 project               = module.new_project.project_id_out

 event_trigger{
  event_type = "google.storage.object.finalize"
  resource   = "${module.new_project.project_id_out}-10xcc-gcf-ocr-images"
 }
}

# To deploy the text translation function with a Cloud Pub/Sub trigger
# gcloud functions deploy ocr-translate --runtime python37 --trigger-topic YOUR_TRANSLATE_TOPIC_NAME --entry-point translate_text

resource "google_cloudfunctions_function" "ocr_translate" {
 name                  = "ocr-translate"
 description           = "Text Translation Function with a Pub/Sub Trigger"
 available_memory_mb   = 256
 source_archive_bucket = google_storage_bucket.source_archive_bucket.name
 source_archive_object = google_storage_bucket_object.ocr_app_tf_zip.name
 timeout               = 60
 entry_point           = "translate_text"
 runtime               = "python37"
 project               = module.new_project.project_id_out

 event_trigger{
  event_type = "google.pubsub.topic.publish"
  resource   = "projects/${module.new_project.project_id_out}/topics/${module.new_project.project_id_out}-topic-gcf-ocr-translate"
 }
}

# To deploy the function that saves results to Cloud Storage with a Cloud Pub/Sub trigger
# gcloud functions deploy ocr-save --runtime python37 --trigger-topic YOUR_RESULT_TOPIC_NAME --entry-point save_result

resource "google_cloudfunctions_function" "ocr_save" {
 name                  = "ocr-save"
 description           = "Function saving results to Cloud Storage with a Pub/Sub Trigger"
 available_memory_mb   = 256
 source_archive_bucket = google_storage_bucket.source_archive_bucket.name
 source_archive_object = google_storage_bucket_object.ocr_app_tf_zip.name
 timeout               = 60
 entry_point           = "save_result"
 runtime               = "python37"
 project               = module.new_project.project_id_out

 event_trigger{
  event_type = "google.pubsub.topic.publish"
  resource   = "projects/${module.new_project.project_id_out}/topics/${module.new_project.project_id_out}-topic-gcf-ocr-results"
 }
}
