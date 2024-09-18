variable "bq_dataset_name" {
  description = "Bigquery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My storage bucket name"
  default     = "demo-bucket-ny-taxi-rides-435804"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

variable "location" {
  description = "project location"
  default     = "me-central1"
}

variable "project" {
  description = "project"
  default     = "ny-taxi-rides-435804"
}
