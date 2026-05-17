$outFile = "$env:TEMP\innosetup.exe"
Write-Host "Downloading Inno Setup 6..."
Invoke-WebRequest -Uri "https://jrsoftware.org/download.php/is.exe" -OutFile $outFile -UseBasicParsing
Write-Host "Installing silently..."
Start-Process -FilePath $outFile -ArgumentList "/VERYSILENT", "/SUPPRESSMSGBOXES", "/NORESTART" -Wait
if (Test-Path "C:\Program Files (x86)\Inno Setup 6\ISCC.exe") {
    Write-Host "SUCCESS: Inno Setup 6 installed."
} else {
    Write-Host "ERROR: Not found at expected path."
    Get-ChildItem "C:\Program Files (x86)\" | Select-Object Name
}
