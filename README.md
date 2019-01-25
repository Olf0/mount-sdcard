# mount-sdcard
#### Enhanced mounting scripts for SD-cards under SailfishOS

This systemd unit file and the udev rules file are by-products of optimising the start-up timing, feature set and shut-down behavior of [crypto-sdcard](https://github.com/Olf0/crypto-sdcard).

They provide the following enhancements compared to the original versions (as of SailfishOS 2.2.x):
* Start mounting (partitions on) SD-card via udisks at the earliest sensible time: Right after udisks2.service has started.
* Unmount before udisks2 begins stopping, hence achieving a clean unmount.
* Ensure, that AlienDalvik (specifically *alien-service-manager.service*) begins starting after mounting succeeded, to allow for [android_storage on SD-card](https://together.jolla.com/question/179060/how-to-externalising-android_storage-and-other-directories-files-to-sd-card/#179060-2-externalising-homenemoandroid_storage).  Even more importantly this also ensures, that unmounting occurs only after AlienDalvik is completely stopped.<br />
Nevertheless, these configuration files are also applicable to devices without AlienDalvik installed.
* Inhibit stubbornly trying to mount block devices without a filesystem recognised by the kernel / udev.
* Create / try to rectify the "compatibility symlink" in order to allow older apps seamlessly accessing (partitions on) SD-cards at their new (since SailfishOS 2.2.0) mount point.

Notes:
* These configuration files do not alter, replace or delete any extant files.
* Minimal SailfishOS version supported by **mount-sdcard** is 2.2.0.
* Support of partitions and whole devices (as Jolla's original versions do).
* Support for (µ)SD-cards and USB-attached storage (if supported by device hardware and Operating System).
* An RPM built for SailfishOS is available at [OpenRepos](https://openrepos.net/content/olf/mount-sdcard).

