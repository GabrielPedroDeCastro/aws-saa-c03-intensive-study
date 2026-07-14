[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)][string]$Bucket,
  [string]$Region = "us-east-1",
  [string]$Profile = "",
  [switch]$AutoApprove
)
$ErrorActionPreference = "Stop"
$target = & "$PSScriptRoot/confirm-aws-target.ps1" -Profile $Profile -Region $Region -Action EMPTY -AutoApprove:$AutoApprove
$Profile = $target.Profile
$common = @("--region", $Region, "--profile", $Profile)

# Remove objetos atuais e, em seguida, todas as versões/delete markers em lotes.
& aws s3 rm "s3://$Bucket" --recursive @common
if ($LASTEXITCODE -ne 0) { throw "Falha ao remover objetos atuais de $Bucket" }

do {
  $raw = & aws s3api list-object-versions --bucket $Bucket @common --output json
  if ($LASTEXITCODE -ne 0) { throw "Falha ao listar versões de $Bucket" }
  $listed = $raw | ConvertFrom-Json
  $objects = @()
  foreach ($item in @($listed.Versions) + @($listed.DeleteMarkers)) {
    if ($null -ne $item) {
      $objects += @{ Key = $item.Key; VersionId = $item.VersionId }
    }
  }
  if ($objects.Count -gt 0) {
    for ($offset = 0; $offset -lt $objects.Count; $offset += 1000) {
      $last = [Math]::Min($offset + 999, $objects.Count - 1)
      $batch = @($objects[$offset..$last])
      $payload = @{ Objects = $batch; Quiet = $true } | ConvertTo-Json -Depth 4 -Compress
      & aws s3api delete-objects --bucket $Bucket --delete $payload @common | Out-Null
      if ($LASTEXITCODE -ne 0) { throw "Falha ao remover versões de $Bucket" }
    }
  }
} while ($objects.Count -gt 0)

Write-Host "Bucket versionado $Bucket vazio."
