data "google_iam_trigger" "admin" {
  binding {
    role = "roles/compute.instanceAdmin"

    members = [
      "serviceAccount:entercloud@entercloud-engine.iam.gserviceaccount.com",
    ]
  }

  binding {
    role = "roles/storage.objectViewer"

    members = [
      "user:andrewpsp@google.com",
    ]
  }
}