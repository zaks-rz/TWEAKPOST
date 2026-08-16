import psutil

SYSTEM_PROCESSES = {
    "system", "idle", "smss.exe", "csrss.exe", "wininit.exe", "services.exe",
    "lsass.exe", "svchost.exe", "explorer.exe", "dwm.exe", "conhost.exe",
    "lsaiso.exe", "fontdrvhost.exe", "winlogon.exe", "taskhostw.exe",
    "sihost.exe", "ctfmon.exe", "searchui.exe", "shellexperiencehost.exe",
    "runtimebroker.exe", "startmenuexperiencehost.exe", "audiodg.exe",
    "spoolsv.exe", "dashost.exe", "wudfhost.exe", "searchindexer.exe",
    "securityhealthservice.exe", "securityhealthhost.exe", "tiworker.exe",
    "trustedinstaller.exe", "dllhost.exe", "presentationfontcache.exe",
    "wmiprvse.exe", "ibtsiva.exe", "textinputhost.exe", "backgroundtaskhost.exe",
    "igfxext.exe", "nvcontainer.exe", "nvcplui.exe", "igcc.exe", "radeonsoftware.exe",
    "dwm.exe", "fontdrvhost.exe", "dwm.exe", "werfault.exe", "ctfmon.exe"
}

UNNECESSARY_PROCESSES = {
    "steam.exe", "steamservice.exe", "steamwebhelper.exe", "epicgameslauncher.exe",
    "epicwebhelper.exe", "origin.exe", "eabackgroundservice.exe", "eadesktop.exe",
    "ea_desktop.exe", "upc.exe", "ubisoftconnect.exe", "ubisoftconnectservice.exe",
    "battlenet.exe", "battle.net.exe", "agent.exe", "riotclientservices.exe",
    "riotclientux.exe", "vanguard.exe", "goggalaxy.exe", "goggalaxyhelper.exe",
    "galaxycommunication.exe", "rsc.exe", "wargaminggamelauncher.exe", "minecraftlauncher.exe",
    "discord.exe", "telegram.exe", "whatsapp.exe", "skype.exe", "slack.exe",
    "teams.exe", "msteams.exe", "zoom.exe", "viber.exe", "signal.exe",
    "messenger.exe", "line.exe", "wechatapp.exe", "kakaotalk.exe", "thunderbird.exe",
    "chrome.exe", "msedge.exe", "firefox.exe", "opera.exe", "brave.exe",
    "opera_gx.exe", "vivaldi.exe", "safari.exe", "tor browser.exe", "waterfox.exe",
    "iexplore.exe", "onedrive.exe", "googledrivesync.exe", "dropbox.exe", "box.exe",
    "icloud.exe", "megasync.exe", "amazoncloudrive.exe", "pcloud.exe", "hidrive.exe",
    "nextcloud.exe", "synologydrive.exe", "asus_framework.exe", "armourycrate.controlservice.exe",
    "armourycrate.service.exe", "asuscertservice.exe", "aura.exe", "acer quick access",
    "nahimicingsvc.exe", "lcodes.exe", "lghub.exe", "lghub_agent.exe", "lghub_updater.exe",
    "rzchromabroadcast.exe", "rzsynapse.exe", "razersynapse.exe", "razercentral.exe",
    "corsair.service.exe", "icue.exe", "msi_sdk.exe", "dragoncenter.exe",
    "gigabyte.controlcenter.exe", "rgbfusion.exe", "steelseriesengine.exe", "logioptions.exe",
    "elgatoscreensink.exe", "streamdeck.exe", "spotify.exe", "spotifywebhelper.exe",
    "itunes.exe", "ituneshelper.exe", "quicktime.exe", "vlc.exe", "potplayermini64.exe",
    "gom.exe", "aimp.exe", "winamp.exe", "realplay.exe", "kmplayer.exe", "audacity.exe",
    "handbrake.exe", "acrobat.exe", "acrord32.exe", "foxitreader.exe", "sumatrapdf.exe",
    "msaccess.exe", "winword.exe", "excel.exe", "powerpnt.exe", "onenote.exe",
    "lync.exe", "outlook.exe", "winrar.exe", "7zg.exe", "7zfm.exe", "bandizip.exe",
    "ccleaner.exe", "defraggler.exe", "revouninstaller.exe", "advancedsystemcare.exe",
    "iobituninstaller.exe", "adobeupdate.exe", "armsvc.exe", "jusched.exe", "java.exe",
    "javaw.exe", "steamerrorreporter.exe", "adobe arm.exe", "acrobat updater.exe",
    "winstore.app.exe", "cortana.exe", "feedbackhub.exe", "yourphone.exe", "people.exe",
    "skypeapp.exe", "mrt.exe", "wireshark.exe", "hxtsr.exe", "wallpaper32.exe",
    "wallpaper64.exe", "rainmeter.exe", "obs64.exe", "obs32.exe", "streamlabsobs.exe",
    "premiere pro.exe", "photoshop.exe", "afterfx.exe", "illustrator.exe", "blender.exe",
    "lightroom.exe", "figma.exe", "notion.exe", "msmpeng.exe", "presentationfontcache.exe",
    "qttask.exe", "NvSmartMaxApp.exe", "nvdisplay.container.exe", "NvTelemetryContainer.exe",
    "RadeonSettings.exe", "atiesrxx.exe", "Ati2evxx.exe", "RAVBg64.exe", "RtHDVBg.exe",
    "Ctxfihlp.exe", "GrooveMonitor.exe", "ISUSPM.exe", "ISServer.exe", "MSASCuiL.exe",
    "NPSCheck.exe", "NvMcTray.exe", "reader_sl.exe", "qttask.exe", "PDVD10Serv.exe",
    "WLXPro.exe", "WLXComm.exe", "GoogleUpdate.exe", "GoogleCrashHandler.exe",
    "BraveSoftwareUpdate.exe", "Update_Service.exe", "FirefoxUpdateService.exe",
    "FoxitPhantomPDF.exe", "TeamViewer_Service.exe", "AnyDesk.exe", "LogMeIn.exe",
    "LogMeInSystray.exe", "Hamachi.exe", "NordVPN.exe", "ExpressVPN.exe",
    "Surfshark.exe", "CyberGhost.exe", "ProtonVPN.exe", "PIA_Service.exe",
    "Bitdefender.exe", "AvastUI.exe", "avgui.exe", "NortonSecurity.exe",
    "McAfee.Core.Init.exe", "Kaspersky.exe", "Eset.UI.exe", "Malwarebytes.exe",
    "CCleaner64.exe", "WiseCare365.exe", "GlaryUtilities.exe", "IObitMalwareFighter.exe",
    "DriverBooster.exe", "AdvancedSystemCareService.exe", "SmartDefrag.exe",
    "EpicWebHelper.exe", "OriginWebHelperService.exe", "Battle.net Helper.exe",
    "UnityCrashHandler64.exe", "UnrealCEFSubProcess.exe", "QtWebEngineProcess.exe",
    "electron.exe", "node.exe", "javaw.exe", "conhost.exe", "cmd.exe", "powershell.exe",
    "wscript.exe", "cscript.exe", "mshta.exe", "rundll32.exe", "regsvr32.exe"
}

for proc in psutil.process_iter(["pid", "name"]):
  try:
    p_name = proc.info["name"].lower()
    p_id = proc.info["pid"]

    if p_name in SYSTEM_PROCESSES:
      continue
    elif p_name in UNNECESSARY_PROCESSES:
      psutil.Process(p_id).terminate()

  except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    pass
