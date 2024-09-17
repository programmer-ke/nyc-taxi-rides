terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.1.0"
    }
  }
}

provider "google" {
  project = "ny-taxi-rides-435804"
  region  = "me-central1"
}


resource "google_storage_bucket" "demo-bucket" {
  name          = "demo-bucket-ny-taxi-rides-435804"
  location      = "me-central1"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
