$lib = 'D:\st_portable_4200\Data\Lib\python38'
$items = Get-ChildItem $lib | Where-Object { $_.Name -match '^(urllib3|idna|certifi|charset_normalizer)' -or $_.Name -eq 'bin' }
$paths = $items | ForEach-Object { $_.FullName }
"removing: " + (($items | ForEach-Object { $_.Name }) -join ', ')
& 'C:\Users\donal\.claude\skills\recycle-delete\recycle.ps1' @paths
python -m pip install --no-deps --only-binary=:all: --python-version 3.8 --implementation cp --abi cp38 --platform win_amd64 --platform any --target $lib "urllib3<2" "idna<3.11" "certifi" "charset_normalizer<3.5" 2>&1 | Select-Object -Last 3
Get-ChildItem $lib -Directory -Name | Where-Object { $_ -match 'urllib3|idna|certifi|charset' }
