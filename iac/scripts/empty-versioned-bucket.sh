#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$script_dir/confirm-aws-target.sh"

bucket="${1:?uso: empty-versioned-bucket.sh BUCKET [REGION]}"
region="${2:-us-east-1}"
confirm_aws_target "EMPTY" "$region"

aws --profile "$AWS_PROFILE" s3 rm "s3://$bucket" --recursive --region "$region"

delete_version_rows() {
  local query="${1:?consulta obrigatória}"
  local rows
  rows="$(aws --profile "$AWS_PROFILE" s3api list-object-versions --bucket "$bucket" --region "$region" --query "$query" --output text)"
  if [ -z "$rows" ] || [ "$rows" = "None" ]; then
    return 0
  fi
  while IFS=$'\t' read -r key version_id; do
    if [ -n "$key" ] && [ "$key" != "None" ]; then
      aws --profile "$AWS_PROFILE" s3api delete-object --bucket "$bucket" --key "$key" --version-id "$version_id" --region "$region" >/dev/null
    fi
  done <<< "$rows"
}

delete_version_rows 'Versions[].[Key,VersionId]'
delete_version_rows 'DeleteMarkers[].[Key,VersionId]'
printf 'Bucket versionado %s vazio.\n' "$bucket"
