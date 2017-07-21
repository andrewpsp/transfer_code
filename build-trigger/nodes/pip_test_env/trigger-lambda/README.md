
arn - The Amazon Resource Name (ARN) identifying your Lambda Function.

qualified_arn - The Amazon Resource Name (ARN) identifying your Lambda Function Version (if versioning is enabled via publish = true).

invoke_arn - The ARN to be used for invoking Lambda Function from API Gateway - to be used in aws_api_gateway_integration's uri

version - Latest published version of your Lambda Function.

last_modified - The date this resource was last modified.

kms_key_arn - (Optional) The ARN for the KMS encryption key.

source_code_hash - Base64-encoded representation of raw SHA-256 sum of the zip file provided either via filename or s3_* parameters.
»
