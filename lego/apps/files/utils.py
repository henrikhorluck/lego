from django.conf import settings
from django.shortcuts import resolve_url

from .models import File
from .storage import storage


def prepare_file_upload(key, user, public):
    """
    Create instructions for the client on how to upload a new file. This functions returns two
    values, the first one is the url the file should be uploaded to and the secound value is a
    dict with additional fields the client need to attach to the upload request.
    """
    file = File.create_file(key, user, public)
    url = resolve_url("api:v1:file-upload-success", file.key)
    redirect_url = f"{settings.SERVER_URL}{url}"
    signed_post = storage.generate_upload_url(file.bucket, file.key, redirect_url)

    return file.key, signed_post["url"], signed_post["fields"], file.get_file_token()
