$pythonProgramPath = "C:\Program Files\Python311\python.exe"
Set-Location -Path "C:\Users\Weste095\Documents\repos\emilywes\synergy-dataset\datasets"
Get-ChildItem -Directory | ForEach-Object {
	Set-Location -Path "$($_.FullName)"
    & $pythonProgramPath "compose.py"
}

Set-Location -Path "C:\Users\Weste095\Documents\repos\emilywes\synergy-dataset\scripts"
