Write-Host "Installing lightweight model..."
ollama pull qwen2.5-coder:1.5b

Write-Host "Creating fast autocomplete model..."
@"
FROM qwen2.5-coder:1.5b
PARAMETER num_ctx 1024
PARAMETER num_thread 4
PARAMETER temperature 0.1
"@ | Out-File Modelfile-fast -Encoding ascii

ollama create qwen-fast -f Modelfile-fast

Write-Host "Creating analysis model..."
@"
FROM qwen2.5-coder:1.5b
PARAMETER num_ctx 4096
PARAMETER num_thread 6
PARAMETER temperature 0.2
"@ | Out-File Modelfile-brain -Encoding ascii

ollama create qwen-brain -f Modelfile-brain

Write-Host "Restarting Ollama..."
taskkill /IM ollama.exe /F 2>$null
Start-Process ollama serve

Write-Host "Setting high priority..."
Start-Sleep -Seconds 3
wmic process where name="ollama.exe" CALL setpriority "high priority"

Write-Host "Creating Continue config..."
$continuePath = "$env:USERPROFILE\.continue"
New-Item -ItemType Directory -Force -Path $continuePath

@"
{
  "models": [
    {
      "title": "Qwen Brain",
      "provider": "ollama",
      "model": "qwen-brain"
    }
  ],
  "autocompleteModel": {
    "provider": "ollama",
    "model": "qwen-fast"
  }
}
"@ | Out-File "$continuePath\config.json" -Encoding ascii

Write-Host "DONE. Restart Cursor."