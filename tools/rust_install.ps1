$dl = 'C:\Users\donal\tools\rust_dl'
New-Item -ItemType Directory -Force $dl | Out-Null
Invoke-WebRequest -Uri 'https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe' -OutFile "$dl\rustup-init.exe" -UseBasicParsing
& "$dl\rustup-init.exe" -y --default-toolchain stable --profile minimal 2>&1 | Select-Object -Last 15
$env:Path = "$env:USERPROFILE\.cargo\bin;" + $env:Path
rustc --version
cargo --version
rustup toolchain install nightly --profile minimal --component rust-src 2>&1 | Select-Object -Last 8
rustup toolchain list
