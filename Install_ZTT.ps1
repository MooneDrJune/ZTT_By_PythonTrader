$destinationpath = "$env:USERPROFILE\ZerodhaTradeTerminal"
mkdir $destinationpath
$url = 'https://github.com/MooneDrJune/ZTT_By_PythonTrader/releases/download/V.0.3/ZerodhaTradeTerminal.zip'
$tmp = New-TemporaryFile | Rename-Item -NewName { $_ -replace 'tmp$', 'zip' } –PassThru
Invoke-WebRequest -OutFile $tmp $url
Microsoft.PowerShell.Archive\Expand-Archive -Path $tmp -DestinationPath $destinationpath -Force -PassThru
$tmp | Remove-Item

write-output "Creating ZerodhaTradeTerminal Icon on Desktop"

$SourceFilePath = "$env:USERPROFILE\ZerodhaTradeTerminal\python.exe"
$ArgumentsToSourceExe = "Zerodha_Trade_Terminal_V3_001.py"
$ShortcutPath = "$env:USERPROFILE\Desktop\ZerodhaTradeTerminal.lnk"
$WScriptObj = New-Object -ComObject ("WScript.Shell")
$shortcut = $WscriptObj.CreateShortcut($ShortcutPath)
$Shortcut.IconLocation = "$env:USERPROFILE\ZerodhaTradeTerminal\PythonTrader.ico"
$shortcut.TargetPath = $SourceFilePath
$Shortcut.Arguments = $ArgumentsToSourceExe
$Shortcut.WorkingDirectory = "$env:USERPROFILE\ZerodhaTradeTerminal"
$shortcut.WindowStyle = 1
$ShortCut.Hotkey = "CTRL+ALT+SHIFT+Z";
$shortcut.Save()
