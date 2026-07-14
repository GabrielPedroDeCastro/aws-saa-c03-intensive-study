[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)][string]$Directory,
  [string]$Region = "us-east-1",
  [string]$Profile = "",
  [switch]$AutoApprove
)
$ErrorActionPreference = "Stop"
$target = & "$PSScriptRoot/confirm-aws-target.ps1" -Profile $Profile -Region $Region -Action DESTROY -AutoApprove:$AutoApprove
$Profile = $target.Profile
$env:AWS_PROFILE = $Profile
$args = @("-chdir=$Directory", "destroy", "-var=aws_region=$Region")
if ($AutoApprove) { $args += "-auto-approve" }
terraform @args
if ($LASTEXITCODE -ne 0) { throw "terraform destroy falhou" }
