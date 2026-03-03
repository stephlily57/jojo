param(
    [Parameter(Mandatory=$true)]
    [string]$ScriptPath
)

if (-not (Test-Path $ScriptPath)) {
    Write-Error "Script path not found: $ScriptPath"
    exit 1
}

$action = "powershell -NoProfile -ExecutionPolicy Bypass -File `"$ScriptPath`""

Write-Host "Creating scheduled task 'GitAutosave' to run every 5 minutes..."
schtasks /Create /SC MINUTE /MO 5 /TN "GitAutosave" /TR $action /F
if ($LASTEXITCODE -eq 0) { Write-Host "Task created." } else { Write-Host "Failed to create task." }

Write-Host "If you prefer to run continuously, start the script in a persistent shell instead."
