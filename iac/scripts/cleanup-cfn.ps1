[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)][string]$StackName,
  [string]$Region = "us-east-1",
  [string]$Profile = "",
  [switch]$AutoApprove
)
$ErrorActionPreference = "Stop"
$target = & "$PSScriptRoot/confirm-aws-target.ps1" -Profile $Profile -Region $Region -Action DESTROY -AutoApprove:$AutoApprove
$Profile = $target.Profile
$common = @("--region", $Region, "--profile", $Profile)
& aws cloudformation delete-stack --stack-name $StackName @common
if ($LASTEXITCODE -ne 0) { throw "Não foi possível iniciar a exclusão de $StackName" }
& aws cloudformation wait stack-delete-complete --stack-name $StackName @common
if ($LASTEXITCODE -ne 0) { throw "A exclusão falhou; consulte os eventos da stack" }
Write-Host "Stack $StackName removida."
