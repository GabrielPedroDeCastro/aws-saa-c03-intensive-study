#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$script_dir/confirm-aws-target.sh"
stack="${1:?uso: cleanup-cfn.sh STACK [REGION]}"
region="${2:-us-east-1}"
confirm_aws_target "DESTROY" "$region"
aws --profile "$AWS_PROFILE" cloudformation delete-stack --stack-name "$stack" --region "$region"
aws --profile "$AWS_PROFILE" cloudformation wait stack-delete-complete --stack-name "$stack" --region "$region"
echo "Stack $stack removida."
