# S3 Multipart Uploads Size Calculator

This Python script calculates the total size of all aborted multipart uploads in a specified AWS S3 bucket. It uses the `boto3` library to interact with the AWS S3 service and `argparse` for command-line argument parsing.

## Features

- Calculates the total size of aborted multipart uploads in a specified S3 bucket.
- Supports specifying the AWS profile and bucket name as command-line arguments.
- Converts the total size from bytes to a more readable format (KB, MB, GB, TB).

## Prerequisites

- Python 3.6 or higher
- AWS CLI configured with the necessary permissions to list multipart uploads and parts in the specified S3 bucket.
- `boto3` library installed. If not installed, you can install it using pip:

 ```bash
 pip install boto3
 ```

## Usage

To run the script, use the following command:

```bash
python calculate_multipart_uploads_size.py --bucket your-bucket-name --profile your-profile-name
```

Replace `your-bucket-name` with the name of your S3 bucket and `your-profile-name` with the name of the AWS profile you wish to use.
