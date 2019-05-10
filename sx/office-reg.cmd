reg query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\OfficeSoftwareProtectionPlatform
pause
reg query HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Office\16.0\Common\OEM
pause
DISM /online /Get-ProvisionedAppxPackages |find "16000"
pause