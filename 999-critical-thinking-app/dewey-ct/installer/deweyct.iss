; deweyct.iss  —  Inno Setup 6 script for DeweyCT Windows installer
;
; Compile with:
;   "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer\deweyct.iss
;
; Expected release/ directory layout (built by build-installer.ps1):
;
;   installer\release\
;     deweyct\          ← PyInstaller launcher bundle
;       deweyct.exe
;       _internal\
;     backend\          ← FastAPI source code
;     python\           ← Python embeddable + site-packages
;     frontend\         ← Next.js standalone + public\ + .next\
;     node\             ← node.exe (portable)
;     ollama\           ← ollama.exe (portable)
;     data\             ← JSON content files
;     .env              ← default configuration

#define MyAppName      "DeweyCT"
#define MyAppVersion   "1.0.0"
#define MyAppPublisher "DeweyCT"
#define MyAppURL       "https://github.com/your-org/deweyct"
#define MyAppExeName   "deweyct.exe"
#define ReleaseDir     "release"

[Setup]
AppId={{8B2F4E3A-1C7D-4F9E-B2A5-3D6E8F1C2B4A}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
; Installer output
OutputDir=..
OutputBaseFilename=DeweyctInstaller
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern
; Require admin for Program Files write
PrivilegesRequired=admin
; Minimum Windows 10
MinVersion=10.0
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
; Icon (shown in Add/Remove Programs and installer wizard)
; SetupIconFile=launcher\assets\deweyct.ico
UninstallDisplayIcon={app}\deweyct\{#MyAppExeName}

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon";     Description: "{cm:CreateDesktopIcon}";     GroupDescription: "{cm:AdditionalIcons}"; Flags: checkedonce
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1; Check: not IsAdminInstallMode

[Files]
; Launcher bundle (compiled by PyInstaller)
Source: "{#ReleaseDir}\deweyct\*";    DestDir: "{app}\deweyct";    Flags: ignoreversion recursesubdirs createallsubdirs

; Backend (Python source)
Source: "{#ReleaseDir}\backend\*";   DestDir: "{app}\backend";   Flags: ignoreversion recursesubdirs createallsubdirs

; Portable Python runtime + site-packages
Source: "{#ReleaseDir}\python\*";    DestDir: "{app}\python";    Flags: ignoreversion recursesubdirs createallsubdirs

; Next.js standalone server + public assets
Source: "{#ReleaseDir}\frontend\*";  DestDir: "{app}\frontend";  Flags: ignoreversion recursesubdirs createallsubdirs

; Portable Node.js
Source: "{#ReleaseDir}\node\*";      DestDir: "{app}\node";      Flags: ignoreversion recursesubdirs createallsubdirs

; Ollama portable binary
Source: "{#ReleaseDir}\ollama\*";    DestDir: "{app}\ollama";    Flags: ignoreversion recursesubdirs createallsubdirs

; Content data files
Source: "{#ReleaseDir}\data\*";      DestDir: "{app}\data";      Flags: ignoreversion recursesubdirs createallsubdirs

; Default .env (will not overwrite if user already has one)
Source: "{#ReleaseDir}\.env";        DestDir: "{app}";           Flags: ignoreversion onlyifinternalbuilddebug
Source: "{#ReleaseDir}\.env";        DestDir: "{app}";           Flags: ignoreversion uninsneveruninstall; DestName: ".env"

[Icons]
; Start Menu
Name: "{group}\{#MyAppName}";          Filename: "{app}\deweyct\{#MyAppExeName}"
Name: "{group}\Uninstall {#MyAppName}"; Filename: "{uninstallexe}"

; Desktop shortcut
Name: "{autodesktop}\{#MyAppName}";   Filename: "{app}\deweyct\{#MyAppExeName}"; Tasks: desktopicon

[Run]
; Launch DeweyCT after install (optional, user can uncheck)
Filename: "{app}\deweyct\{#MyAppExeName}"; \
  Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; \
  Flags: nowait postinstall skipifsilent

[UninstallRun]
; Nothing special needed on uninstall — child processes stop with the launcher

[Code]
// Show a friendly "Downloading model…" note on the finish page
// explaining that the first launch will need internet.
procedure CurPageChanged(CurPageID: Integer);
begin
  if CurPageID = wpFinished then
  begin
    WizardForm.FinishedLabel.Caption :=
      'DeweyCT has been installed.' + #13#10 + #13#10 +
      'On first launch the app will download the selected AI model ' +
      '(~2–5 GB). This requires an internet connection and may take ' +
      'several minutes depending on your connection speed.' + #13#10 + #13#10 +
      'Subsequent launches are instant.' + #13#10 + #13#10 +
      WizardForm.FinishedLabel.Caption;
  end;
end;
