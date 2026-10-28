$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$root = 'C:\Users\donal\tools\audit_toolchains'
New-Item -ItemType Directory -Force $root, "$root\dl" | Out-Null

# Erlang/OTP 27 portable zip + matching Elixir
gh release download OTP-27.3.4.19 --repo erlang/otp --pattern 'otp_win64_27.3.4.19.zip' --dir "$root\dl" --clobber
Expand-Archive "$root\dl\otp_win64_27.3.4.19.zip" "$root\erlang" -Force
gh release download v1.20.4 --repo elixir-lang/elixir --pattern 'elixir-otp-27.zip' --dir "$root\dl" --clobber
Expand-Archive "$root\dl\elixir-otp-27.zip" "$root\elixir" -Force

# Graphviz zip with checksum
$g = 'windows_10_cmake_Release_Graphviz-16.1.0-win64.zip'
$id = (Invoke-RestMethod 'https://gitlab.com/api/v4/projects/4207231/packages?package_name=graphviz-releases&per_page=1&order_by=created_at&sort=desc')[0].id
$u = "https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/16.1.0/$g"
Invoke-WebRequest $u -OutFile "$root\dl\$g"
Invoke-WebRequest "$u.sha256" -OutFile "$root\dl\$g.sha256"
$want = ((Get-Content "$root\dl\$g.sha256" -Raw) -split '\s+')[0].ToLower()
$have = (Get-FileHash "$root\dl\$g" -Algorithm SHA256).Hash.ToLower()
"graphviz sha256 match: $($want -eq $have)"
Expand-Archive "$root\dl\$g" "$root\graphviz" -Force

# .NET SDK into the same folder
Invoke-WebRequest 'https://dot.net/v1/dotnet-install.ps1' -OutFile "$root\dl\dotnet-install.ps1"
& "$root\dl\dotnet-install.ps1" -Channel STS -InstallDir "$root\dotnet" -NoPath

"--- versions"
Get-ChildItem "$root\erlang" -Recurse -Filter erl.exe | Select-Object -First 1 FullName
Get-ChildItem "$root\elixir\bin" -Name | Select-Object -First 6
Get-ChildItem "$root\graphviz" -Recurse -Filter dot.exe | Select-Object -First 1 FullName
& "$root\dotnet\dotnet.exe" --version
