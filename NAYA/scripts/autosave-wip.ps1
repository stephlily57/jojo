#!/usr/bin/env pwsh
# Autosave script: stages, commits, and pushes current work to remote branch 'wip-autosave'
# Usage: run manually or via scheduled task.

try {
    $repo = git rev-parse --show-toplevel 2>$null
}
catch {
    $repo = $null
}
if (-not $repo) {
    Write-Error "Not inside a git repository. Run this script from inside your repo."
    exit 1
}

Set-Location $repo

# Stage everything
git add -A

# Check if there is anything staged
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    $msg = "WIP autosave " + (Get-Date -Format o)
    git commit -m $msg 2>$null || Write-Host "Nothing to commit or commit failed."

    # Push current HEAD to remote branch wip-autosave (does not change local branch)
    git push origin HEAD:wip-autosave 2>&1 | ForEach-Object { Write-Host $_ }
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Push failed — configure SSH keys or a PAT for non-interactive pushes."
        exit 2
    }
    else {
        Write-Host "Autosave pushed to origin/wip-autosave"
    }
}
else {
    Write-Host "No staged changes — nothing to do."
}
