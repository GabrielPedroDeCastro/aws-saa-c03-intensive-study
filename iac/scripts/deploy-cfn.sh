#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$script_dir/confirm-aws-target.sh"
template="${1:?uso: deploy-cfn.sh TEMPLATE STACK [REGION] [Key=Value ...]}"
stack="${2:?informe o nome da stack}"
region="${3:-us-east-1}"
confirm_aws_target "DEPLOY" "$region"
if [ "$#" -ge 3 ]; then
  shift 3
else
  shift 2
fi
args=(cloudformation deploy --template-file "$template" --stack-name "$stack" --region "$region" --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND --no-fail-on-empty-changeset)
if [ "$#" -gt 0 ]; then args+=(--parameter-overrides "$@"); fi
aws --profile "$AWS_PROFILE" "${args[@]}"
aws --profile "$AWS_PROFILE" cloudformation describe-stacks --stack-name "$stack" --region "$region" --query 'Stacks[0].Outputs' --output table
