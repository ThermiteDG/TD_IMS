$currentPath = $MyInvocation.MyCommand.Path 
$parent = Split-Path -Path $currentPath -parent
$test = $parent+'\Banan.png'
Write-Output $test
Set-ItemProperty -path 'HKCU:ControlPanel/Desktop' -name WallPaper -value $test
do {RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters, 1, True Start-Process "https://youtu.be/42JCu9jWmY0"} while ($true)