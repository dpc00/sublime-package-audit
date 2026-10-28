$d = 'C:\Users\donal\tools\php-tools'
New-Item -ItemType Directory -Force $d | Out-Null
Invoke-WebRequest -Uri 'https://getcomposer.org/download/latest-stable/composer.phar' -OutFile "$d\composer.phar" -UseBasicParsing
$php = (Get-Command php).Source
"php: $php"
& $php -v | Select-Object -First 1
& $php -m | Select-String -Pattern 'openssl|mbstring|curl|zip|phar|json' | ForEach-Object { $_.Line }
$ini = Join-Path (Split-Path $php) 'php.ini'
"ini exists: $(Test-Path $ini)"
$env:COMPOSER_HOME = "$d\composer_home"
& $php "$d\composer.phar" global require "asm89/twig-lint" 2>&1 | Select-Object -Last 12
