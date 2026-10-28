$d = 'C:\Users\donal\tools\php-tools'
$env:PHPRC = $d
$env:COMPOSER_HOME = "$d\composer_home"
$php = (Get-Command php).Source
& $php -m | Select-String -Pattern 'openssl|mbstring|curl|zip' | ForEach-Object { $_.Line }
& $php "$d\composer.phar" global require "asm89/twig-lint" 2>&1 | Select-Object -Last 14
Get-ChildItem "$d\composer_home\vendor\bin" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Name
