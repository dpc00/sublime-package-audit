"== all-users app packages matching codex|openai|muse|meta|sandbox =="
Get-AppxPackage -AllUsers | Where-Object { $_.Name -match 'codex|openai|muse|meta|sandbox' -or $_.PackageFullName -match 'codex|openai|muse' -or $_.Publisher -match 'openai|meta platforms|facebook' } | Select-Object Name,PackageFullName,Publisher | Format-List
"== provisioned packages =="
Get-AppxProvisionedPackage -Online | Where-Object { $_.DisplayName -match 'codex|openai|muse|meta' } | Select-Object DisplayName,PackageName | Format-List
"== count of all-users packages =="
(Get-AppxPackage -AllUsers).Count
"done"
