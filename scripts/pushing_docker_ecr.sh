#!/usr/bin/env bash
aws_access_key_id = $AWS_ACCESS_KEY_ID
aws_secret_access_key = $AWS_SECRET_ACCESS_KEY


$(aws ecr get-login --region $AWS_DEFAULT_REGION --no-include-email)
echo "Tag Step"
docker tag bigmart $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/bigmart_docker_ecr
echo "Push Docker to ECR"
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/bigmart_docker_ecr

