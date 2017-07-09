#!/bin/bash 
aws lambda create-function \
 --region us-west-1 \
 --function-name post-action-trigger-action-1 \
 --zip-file fileb: //home/ubuntu/build-trigger/build-trigger.zip \ 
 --role arn:aws:iam::building8:service-role/lambda_function_role  \
 --handler lambda_function.lambda_handler \
 --runtime python3.5 \
 --timeout 15 \
 --memory-size 256
