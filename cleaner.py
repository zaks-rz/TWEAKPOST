import psutil


SYSTEM_PROCESSES = {
    "system", "idle", "smss.exe", "csrss.exe", "wininit.exe", "services.exe",
    "lsass.exe", "svchost.exe", "explorer.exe", "dwm.exe", "conhost.exe",
    "lsaiso.exe", "fontdrvhost.exe", "winlogon.exe", "taskhostw.exe",
    "sihost.exe", "ctfmon.exe", "searchui.exe", "shellexperiencehost.exe",
    "runtimebroker.exe", "startmenuexperiencehost.exe", "audiodg.exe",
    "spoolsv.exe", "dasHost.exe", "WUDFHost.exe", "SearchIndexer.exe",
    "SecurityHealthService.exe", "SecurityHealthHost.exe", "TiWorker.exe",
    "TrustedInstaller.exe", "dllhost.exe", "PresentationFontCache.exe",
    "WmiPrvSE.exe", "ibtsiva.exe", "ctfmon.exe", "TextInputHost.exe",
    "backgroundtaskhost.exe", "dwm.exe", "fontdrvhost.exe"
}

UNNECESSARY_PROCESSES = {
    # منصات ومتاجر الألعاب بجميع أنواعها
    "steam.exe", "steamservice.exe", "steamwebhelper.exe",
    "epicgameslauncher.exe", "epicwebhelper.exe", "origin.exe",
    "eabackgroundservice.exe", "eadesktop.exe", "ea_desktop.exe",
    "upc.exe", "ubisoftconnect.exe", "ubisoftconnectservice.exe",
    "battlenet.exe", "battle.net.exe", "agent.exe",
    "riotclientservices.exe", "riotclientux.exe", "vanguard.exe",
    "goggalaxy.exe", "goggalaxyhelper.exe", "galaxycommunication.exe",
    "rsc.exe", "wargaminggamelauncher.exe", "minecraftlauncher.exe",

    # برامج الدردشة والتواصل (حتى الطبيعية واليومية)
    "discord.exe", "telegram.exe", "whatsapp.exe", "skype.exe",
    "slack.exe", "teams.exe", "msteams.exe", "zoom.exe",
    "viber.exe", "signal.exe", "messenger.exe", "line.exe",
    "wechatapp.exe", "kakaotalk.exe", "thunderbird.exe",

    # متصفحات الويب بجميع أنواعها وإضافاتها
    "chrome.exe", "msedge.exe", "firefox.exe", "opera.exe",
    "brave.exe", "opera_gx.exe", "vivaldi.exe", "safari.exe",
    "tor browser.exe", "waterfox.exe", "iexplore.exe",

    # خدمات التخزين السحابي والمزامنة الشائعة
    "onedrive.exe", "googledrivesync.exe", "dropbox.exe",
    "box.exe", "icloud.exe", "megasync.exe", "amazoncloudrive.exe",
    "pcloud.exe", "hidrive.exe", "nextcloud.exe", "synologydrive.exe",

    # برامج العتاد واللوحات ومساعدات الماوس والكيبورد البديهية
    "asus_framework.exe", "armourycrate.controlservice.exe", "armourycrate.service.exe",
    "asuscertservice.exe", "aura.exe", "acer quick access", "nahimicingsvc.exe",
    "lcodes.exe", "lghub.exe", "lghub_agent.exe", "lghub_updater.exe",
    "rzchromabroadcast.exe", "rzsynapse.exe", "razersynapse.exe", "razercentral.exe",
    "corsair.service.exe", "icue.exe", "msi_sdk.exe", "dragoncenter.exe",
    "gigabyte.controlcenter.exe", "rgbfusion.exe", "steelseriesengine.exe",
    "logioptions.exe", "elgatoscreensink.exe", "streamdeck.exe",

    # برامج الوسائط، تشغيل الأغاني، والفيديو البديهية
    "spotify.exe", "spotifywebhelper.exe", "itunes.exe", "ituneshelper.exe",
    "quicktime.exe", "vlc.exe", "potplayermini64.exe", "gom.exe",
    "aimp.exe", "winamp.exe", "realplay.exe", "kmplayer.exe",
    "audacity.exe", "handbrake.exe",

    # برامج قراءة ملفات الـ PDF والمستندات (التي تعمل بالخلفية للسرعة)
    "acrobat.exe", "acrord32.exe", "foxitreader.exe", "sumatrapdf.exe",
    "msaccess.exe", "winword.exe", "excel.exe", "powerpnt.exe",
    "onenote.exe", "lync.exe", "outlook.exe",

    # برامج ضغط وفك الملفات وأدوات الصيانة العادية
    "winrar.exe", "7zg.exe", "7zfm.exe", "bandizip.exe",
    "ccleaner.exe", "defraggler.exe", "revouninstaller.exe",
    "advancedsystemcare.exe", "iobituninstaller.exe",

    # تحديثات البرامج ومساعدات الشركات المزعجة
    "adobeupdate.exe", "armsvc.exe", "jusched.exe", "java.exe",
    "javaw.exe", "steamerrorreporter.exe", "adobe arm.exe",
    "acrobat updater.exe", "winstore.app.exe", "cortana.exe",
    "feedbackhub.exe", "yourphone.exe", "people.exe", "skypeapp.exe",
    "mrt.exe", "wireshark.exe", "hxtsr.exe", "igfxext.exe",
    "nvcontainer.exe", "nvcplui.exe", "igcc.exe", "RadeonSoftware.exe",

    # برامج المونتاج، التصميم، والثيمات الحية
    "wallpaper32.exe", "wallpaper64.exe", "rainmeter.exe",
    "obs64.exe", "obs32.exe", "streamlabsobs.exe", "premiere pro.exe",
    "photoshop.exe", "afterfx.exe", "illustrator.exe", "blender.exe",
    "lightroom.exe", "figma.exe", "notion.exe"
}

for proc in psutil.process_iter(["pid", "name"]):
  try:
    p_name = proc.info["name"].lower()
    p_id = proc.info["pid"]

    # حماية حديدية تمنع لمس أي شيء يخص نظام الويندوز
    if p_name in SYSTEM_PROCESSES:
      continue

    # استهداف وقتل أي برنامج باللائحة بدون تردد لتفريغ الرام والمعالج لأقصى حد
    elif p_name in UNNECESSARY_PROCESSES:
      print(f"[*] Mega cleaning process: {p_name} (PID: {p_id})")
      psutil.Process(p_id).terminate()

  except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    pass
