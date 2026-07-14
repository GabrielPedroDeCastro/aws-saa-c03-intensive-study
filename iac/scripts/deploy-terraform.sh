#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$script_dir/confirm-aws-target.sh"
directory="${1:?uso: deploy-terraform.sh DIRETORIO [REGION]}"
region="${2:-us-east-1}"
confirm_aws_target "DEPLOY" "$region"
terraform -chdir="$directory" init
terraform -chdir="$directory" fmt -check
terraform -chdir="$directory" validate
terraform -chdir="$directory" apply -var="aws_region=$region"
terraform -chdir="$directory" output
