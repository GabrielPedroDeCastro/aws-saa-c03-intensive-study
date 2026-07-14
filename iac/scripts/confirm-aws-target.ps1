[CmdletBinding()]
param(
  [string]$Profile = "",
  [string]$Region = "us-east-1",
  [Parameter(Mandatory = $true)][ValidateSet("DEPLOY", "DESTROY", "EMPTY")][string]$Action,
  [switch]$AutoApprove
)
$ErrorActionPreference = "Stop"

$effectiveProfile = if ($Profile) { $Profile } else { $env:AWS_PROFILE }
if (-not $effectiveProfile) {
  throw "Perfil AWS obrigatório. Informe -Profile ou defina AWS_PROFILE para a conta sandbox."
}

$raw = & aws sts get-caller-identity --profile $effectiveProfile --output json
if ($LASTEXITCODE -ne 0) { throw "Não foi possível validar o perfil AWS '$effectiveProfile'." }
$identity = $raw | ConvertFrom-Json
Write-Host "AWS alvo: Account=$($identity.Account) | Arn=$($identity.Arn) | Region=$Region | Profile=$effectiveProfile"

if (-not $AutoApprove) {
  $confirmation = Read-Host "Digite $Action para confirmar esta conta/região"
  if ($confirmation -cne $Action) { throw "Operação cancelada: confirmação não corresponde a $Action." }
}

[pscustomobject]@{
  Profile = $effectiveProfile
  Account = $identity.Account
  Arn = $identity.Arn
  Region = $Region
}
