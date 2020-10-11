#!/usr/bin/env bash
aws configure --profile staging set $region
aws configure --profile staging set $aws_access_key_id
aws configure --profile staging set $aws_secret_access_key
