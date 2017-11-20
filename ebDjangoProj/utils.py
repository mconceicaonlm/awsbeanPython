from storages.backends.s3boto3 import S3Boto3Storage

StaticRootS3BotoStorage =lambda: S3Boto3Storage(location='static') # bucket name / static
MediaRootS3BotoStorages=lambda: S3Boto3Storage(location='media') # bucket name / media

#ProtectedRootS3BotoStorage = lambda: S3Boto3Storage (location = 'protected') # bucket name / protected