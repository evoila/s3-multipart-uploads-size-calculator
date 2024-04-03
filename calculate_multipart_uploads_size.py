import boto3
import argparse


def calculate_aborted_multipart_uploads_size(
    bucket_name: str, profile_name: str
) -> int:
    # Create a session with the specified profile
    session = boto3.Session(profile_name=profile_name)

    s3 = session.client("s3")
    paginator = s3.get_paginator("list_multipart_uploads")
    total_size = 0

    for page in paginator.paginate(Bucket=bucket_name):
        for upload in page.get("Uploads", []):
            upload_id = upload["UploadId"]
            key = upload["Key"]

            parts_paginator = s3.get_paginator("list_parts")
            for parts_page in parts_paginator.paginate(
                Bucket=bucket_name, Key=key, UploadId=upload_id
            ):
                for part in parts_page.get("Parts", []):
                    total_size += part["Size"]

    return total_size

def convert_bytes(size: int) -> str:
    for x in ["bytes", "KB", "MB", "GB", "TB"]:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0
    return size


# Set up command-line argument parsing
parser = argparse.ArgumentParser(
    description="Calculate the total size of all aborted multipart uploads in a specified S3 bucket."
)
parser.add_argument(
    "--bucket", required=True, type=str, help="The name of the S3 bucket."
)
parser.add_argument(
    "--profile",
    default="default",
    type=str,
    help='The AWS profile to use. Defaults to "default".',
)

args = parser.parse_args()

# Use the provided arguments
bucket_name = args.bucket
profile_name = args.profile

total_size_bytes = calculate_aborted_multipart_uploads_size(bucket_name, profile_name)
total_size_readable = convert_bytes(total_size_bytes)
print(
    f"Total size of aborted multipart uploads in {bucket_name}: {total_size_readable}"
)
