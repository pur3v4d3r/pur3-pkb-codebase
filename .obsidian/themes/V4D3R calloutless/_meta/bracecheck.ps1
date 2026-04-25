$file = "D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\theme.css"
$content = Get-Content $file -Raw -Encoding UTF8
$open = ([regex]::Matches($content, '\{')).Count
$close = ([regex]::Matches($content, '\}')).Count
Write-Host "Open braces: $open"
Write-Host "Close braces: $close"
Write-Host "Balance: $($open - $close)"
