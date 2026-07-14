#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$script_dir/confirm-aws-target.sh"
directory="${1:?uso: cleanup-terraform.sh DIRETORIO [REGION]}"
region="${2:-us-east-1}"
confirm_aws_target "DESTROY" "$region"
terraform -chdir="$directory" destroy -var="aws_region=$region"
