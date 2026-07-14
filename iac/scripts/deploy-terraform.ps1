[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)][string]$Directory,
  [string]$Region = "us-east-1",
  [string]$Profile = "",
  [switch]$AutoApprove
)
$ErrorActionPreference = "Stop"
$target = & "$PSScriptRoot/confirm-aws-target.ps1" -Profile $Profile -Region $Region -Action DEPLOY -AutoApprove:$AutoApprove
$Profile = $target.Profile
$env:AWS_PROFILE = $Profile
terraform "-chdir=$Directory" init
if ($LASTEXITCODE -ne 0) { throw "terraform init falhou" }
terraform "-chdir=$Directory" fmt -check
if ($LASTEXITCODE -ne 0) { throw "terraform fmt -check falhou" }
terraform "-chdir=$Directory" validate
if ($LASTEXITCODE -ne 0) { throw "terraform validate falhou" }
$args = @("-chdir=$Directory", "apply", "-var=aws_region=$Region")
if ($AutoApprove) { $args += "-auto-approve" }
terraform @args
if ($LASTEXITCODE -ne 0) { throw "terraform apply falhou" }
terraform "-chdir=$Directory" output
