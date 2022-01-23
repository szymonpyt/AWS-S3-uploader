from password import bucket_name, access_key_id, secret_access_key
from boto3.s3.transfer import S3Transfer
import boto3
import os
from time import sleep


# make connection to bucket
aws_client = boto3.client("s3", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
transfer = S3Transfer(aws_client)
# path to catalog on desktop
src = "/Users/user/Desktop/AWS/"
# check if dir not empty
if len(os.listdir(src)) != 0:
    for file in os.listdir(src):
        # file_path = Enter path to local file here,
        file_path = src + file
        # file_upload_key = store it in this folder using this filename in the s3 bucket
        file_upload_key = str(file)
        # bucket_name = enter bucket name here
        transfer.upload_file(file_path, bucket_name, file_upload_key)
        # remove file after uploading
        os.remove(file_path)
else:
    print("Empty")
    sleep(2)
