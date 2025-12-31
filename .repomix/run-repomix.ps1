# run-repomix.ps1

Write-Host "🚀 Starting Repomix Packing Process..." -ForegroundColor Cyan

# Check if repomix is available in PATH
if (Get-Command "repomix" -ErrorAction SilentlyContinue) {
    try {
        # Execute the command
        repomix --config custom-repomix.config.json
        
        Write-Host "`n✅ Repomix completed successfully." -ForegroundColor Green
    }
    catch {
        Write-Host "`n❌ An error occurred during execution." -ForegroundColor Red
        Write-Error $_
    }
}
else {
    Write-Host "❌ Error: 'repomix' command not found. Ensure it is installed globally (npm i -g repomix)." -ForegroundColor Red
}

# Optional: Pause if double-clicked to read output
if ($Host.Name -eq "ConsoleHost") {
    Read-Host -Prompt "Press Enter to exit"
}