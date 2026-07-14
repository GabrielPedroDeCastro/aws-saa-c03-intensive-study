#!/usr/bin/env bash

confirm_aws_target() {
  local action="${1:?ação obrigatória}"
  local region="${2:?região obrigatória}"
  : "${AWS_PROFILE:?Defina AWS_PROFILE com o perfil da conta sandbox antes de continuar}"

  local identity
  identity="$(aws sts get-caller-identity --profile "$AWS_PROFILE" --query '[Account,Arn]' --output text)"
  printf 'AWS alvo: %s | Region=%s | Profile=%s\n' "$identity" "$region" "$AWS_PROFILE"

  if [ "${LAB_AUTO_APPROVE:-0}" != "1" ]; then
    if [ ! -t 0 ]; then
      printf 'Confirmação interativa indisponível. Revise a conta e use LAB_AUTO_APPROVE=1 somente se for intencional.\n' >&2
      return 1
    fi
    local confirmation
    read -r -p "Digite $action para confirmar esta conta/região: " confirmation
    if [ "$confirmation" != "$action" ]; then
      printf 'Operação cancelada: confirmação não corresponde a %s.\n' "$action" >&2
      return 1
    fi
  fi
}
