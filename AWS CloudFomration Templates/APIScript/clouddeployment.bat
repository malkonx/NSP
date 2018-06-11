@echo off
setlocal
echo [%date%, %time%] Started Automation > "C:\Program Files\McAfee\Network Security Manager\App\clouddeployment.log"
path=%path%;C:\Python27
set nsmcounter=1
:checkNSMloop
for /F "tokens=3 delims=: " %%H in ('sc query "NetworkSecurityManager" ^| findstr "        STATE"') do (
  if /I "%%H" NEQ "RUNNING" (
    if %nsmcounter% GTR 30 (
	echo [%date%, %time%] NSM not started after 5 minutes, FAILED >> "C:\Program Files\McAfee\Network Security Manager\App\clouddeployment.log"
    goto :checkNSMfail
  )
	set /a nsmcounter=%nsmcounter%+1
    echo [%date%, %time%] NSM not yet started, tried %nsmcounter% times. Will check again after 10 seconds  >> "C:\Program Files\McAfee\Network Security Manager\App\clouddeployment.log"
    timeout /t 10
    goto :checkNSMloop
  ) else (
	echo [%date%, %time%] NSM has started >> "C:\Program Files\McAfee\Network Security Manager\App\clouddeployment.log"
    python C:\Users\Administrator\Desktop\ScriptFiles\cloudAPIAutomation.py
  )
)
:checkNSMfail