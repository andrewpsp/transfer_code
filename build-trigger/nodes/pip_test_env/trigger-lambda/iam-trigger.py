resource "aws_iam_role" "iam-trigger" {
  name = "iam-trigger"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_lambda_function" "transfer-trigger" {
  filename         = "trigger_payload.zip"
  function_name    = "trigger-happy"
  role             = "${aws_iam_role.iam-trigger.arn}"
  handler          = "exports.trigg4r"
  source_code_hash = "${base64sha256(file("trigger_payload.zip"))}"
  runtime          = "python3.x"

  environment {
    variables = {
      demo = "entercloud engine"
    }
  }
}