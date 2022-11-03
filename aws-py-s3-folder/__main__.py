from argparse import Namespace
from ensurepip import version
import json

from pulumi import export, Config
from pulumi_aws import s3
import os

import pulumi
stack_name = pulumi.get_stack()

tags = {
    "env": "dev",
    "change": "super",
}

web_bucket = s3.Bucket(f"{stack_name}",
    tags=tags
    )

bucket_name = web_bucket.id

# Export the name of the bucket
export('bucket_name', web_bucket.id)


