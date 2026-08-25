Get-ChildItem "$PSScriptRoot\..\datasets" -Directory | ForEach-Object {
    Push-Location $_.FullName
    python compose.py
    Pop-Location
}
