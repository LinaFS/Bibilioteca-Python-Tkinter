; NSIS installer script for BibliotecaApp
; Usage: run `makensis installer.nsi` after building the exe (dist\BibliotecaApp.exe)

Name "BibliotecaApp"
OutFile "dist\\BibliotecaAppInstaller.exe"
InstallDir "$PROGRAMFILES\\BibliotecaApp"
RequestExecutionLevel admin

Page directory
Page instfiles

Section "Install"
  SetOutPath "$INSTDIR"
  ; Copy the single-file exe built by PyInstaller
  File "dist\\BibliotecaApp.exe"

  ; Copy credentials and bundled gui assets
  File "firebase-credentials.json"
  SetOutPath "$INSTDIR\\guiBuild"
  File /r "guiBuild\\*.*"

  ; Create Start Menu and Desktop shortcuts
  CreateDirectory "$SMPROGRAMS\\BibliotecaApp"
  CreateShortCut "$SMPROGRAMS\\BibliotecaApp\\BibliotecaApp.lnk" "$INSTDIR\\BibliotecaApp.exe"
  CreateShortCut "$DESKTOP\\BibliotecaApp.lnk" "$INSTDIR\\BibliotecaApp.exe"
SectionEnd

Section "Uninstall"
  Delete "$SMPROGRAMS\\BibliotecaApp\\BibliotecaApp.lnk"
  Delete "$DESKTOP\\BibliotecaApp.lnk"
  RMDir /r "$INSTDIR"
  RMDir "$SMPROGRAMS\\BibliotecaApp"
SectionEnd
