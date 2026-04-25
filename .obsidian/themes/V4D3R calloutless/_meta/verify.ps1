$c = [System.IO.File]::ReadAllText("D:\10_pur3v4d3r's-vault\.obsidian\themes\V4D3R Crimson\theme.css")
$open = ([regex]::Matches($c, '\{')).Count
$close = ([regex]::Matches($c, '\}')).Count
Write-Host "Open braces: $open"
Write-Host "Close braces: $close"
Write-Host "Balance: $($open - $close)"
$lines = $c -split "`n"
Write-Host "Total lines: $($lines.Count)"
Write-Host "Terminal marker present: $($c.Contains('END OF FILE: theme.css'))"
