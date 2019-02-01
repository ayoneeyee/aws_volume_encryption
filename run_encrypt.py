#!/bin/bash
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId]' --output text | while read line;
do
  ./volume_encryption.py -i $line -r us-east-1
Done
