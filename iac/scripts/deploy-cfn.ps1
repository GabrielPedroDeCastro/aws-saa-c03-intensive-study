[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)][string]$Template,
  [Parameter(Mandatory = $true)][string]$StackName,
  [string]$Region = "us-east-1",
  [string]$Profile = "",
  [string[]]$Parameters = @(),
  [switch]$AutoApprove
)
$ErrorActionPreference = "Stop"
$target = & "$PSScriptRoot/confirm-aws-target.ps1" -Profile $Profile -Region $Region -Action DEPLOY -AutoApprove:$AutoApprove
$Profile = $target.Profile
$awsArgs = @("cloudformation", "deploy", "--template-file", $Template, "--stack-name", $StackName, "--region", $Region, "--capabilities", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND", "--no-fail-on-empty-changeset")
$awsArgs += @("--profile", $Profile)
if ($Parameters.Count -gt 0) { $awsArgs += "--parameter-overrides"; $awsArgs += $Parameters }
& aws @awsArgs
if ($LASTEXITCODE -ne 0) { throw "Falha no deploy da stack $StackName" }
$describeArgs = @("cloudformation", "describe-stacks", "--stack-name", $StackName, "--region", $Region, "--query", "Stacks[0].Outputs", "--output", "table")
$describeArgs += @("--profile", $Profile)
& aws @describeArgs
if ($LASTEXITCODE -ne 0) { throw "Falha ao consultar outputs da stack $StackName" }
