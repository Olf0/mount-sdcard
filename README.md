# mount-sdcard
#### Enhanced mounting scripts for SD-cards under SailfishOS

This systemd unit file and the udev rules file are by-products of optimising the start-up timing, feature set and shut-down behavior of [crypto-sdcard](https://github.com/Olf0/crypto-sdcard).

They provide the following enhancements compared to SailfishOS' original versions:
* Start mounting (partitions on) SD-card via udisks at the earliest sensible time: Right after *udisks2.service* has started.
* Unmount before *udisks2.service* begins stopping, hence achieving a clean unmount.
* Also do not use SailfishOS' *udisksctl-user* script for unmounting (because this cannot work, at the time ExecStop is executed), which is installed and used by SailfishOS since its release 3.2.1, and was also used by *mount-sdcard* versions 1.1-1 to 1.3.0-21; see [details here](https://github.com/Olf0/mount-sdcard/pull/2).
* Ensure, that AlienDalvik (specifically *alien-service-manager.service*) begins starting after mounting succeeded, to allow for [android_storage on SD-card](https://together.jolla.com/question/203539/guide-externalising-android_storage-and-other-directories-files-to-sd-card/#203539-2-externalising-homenemoandroid_storage).<br />
  Even more importantly (i.e., also relevant for devices without "android_storage on SD-card") this also ensures, that unmounting occurs only after AlienDalvik has completely stopped.<br />
  Nevertheless, these configuration files are also applicable to devices without AlienDalvik installed.
* Versions below 1.0-4: Inhibit stubbornly trying to mount block devices without a filesystem recognised by the kernel / udev.<br />
  As Jolla resolved this in SailfishOS 3.0.1 (see [commit](https://git.sailfishos.org/mer-core/udisks2/commit/6fae1738440d65deb995edb0e5d759c74729d00b) and [changelog](https://together.jolla.com/question/195733/changelog-301-sipoonkorpi/#195733-udisks2)), this workaround is omitted in [*mount-sdcard 1.0-4*](https://github.com/Olf0/mount-sdcard/releases) (and later versions), making [*v1.0-3*](https://github.com/Olf0/mount-sdcard/releases/tag/1.0-3) the last release installable on SailfishOS 2.2.0, 2.2.1 and 3.0.0.
* Versions below 1.0: Create / try to rectify the "compatibility symlink" in order to allow older apps seamlessly accessing (partitions on) SD-cards at their new (since SailfishOS 2.2.0) mount point.

Notes:
* These configuration files do not alter, replace or delete any extant files.
* Minimal SailfishOS version supported by *mount-sdcard* is 2.2.0.
* Since *mount-sdcard 1.0-4* at least [SailfishOS 3.0.1](https://github.com/Olf0/mount-sdcard/releases/tag/1.0-4) is required.
* Since *mount-sdcard 1.1-1* at least [SailfishOS 3.2.1](https://github.com/Olf0/mount-sdcard/pull/2) is required.
* Support of partitions and whole devices (as SailfishOS' original versions do).
* Support for (µ)SD-cards and USB-attached storage (if supported by device hardware and Operating System).
* An RPM built for SailfishOS is available at [OpenRepos](https://openrepos.net/content/olf/mount-sdcard).
