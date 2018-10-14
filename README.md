# mount-sdcard
Enhanced mounting scripts for SD-cards under SailfishOS 2.2.x

These systemd units "mount-sd@.service", "symlink-sd@.service" and the udev rule file "81-mount-sd.rule" are by-products of optimising the start-up timing, feature set and shut-down behavior of [crypto-sdcard](https://github.com/Olf0/crypto-sdcard). 
They provide the following enhancements compared to the original versions (as of SailfishOS 2.2.x):  * Start mounting (partitions on) SD-card via udisks at the earliest sensible time: Right after udisks2.service has started.  * Unmount before udisks2 begins stopping, hence achieving a clean unmount.  * Ensure, that AlienDalvik (alien-service-manager.service) begins starting after mounting succeeded, to allow for android_storage ("/data/media") on SD-card; even more importantly this also ensures, that unmounting occurs only after AlienDalvik is completely stopped.<br />
Nevertheless, these configuration files are also applicable to devices without AlienDalvik installed.
* These configuration files do not alter, substitute or delete any extant files.
* Inhibit stubbornly trying to mount block devices without a filesystem recognised by the kernel / udev.
* Create a "compatibility symlink" to allow older apps seamlessly accessing (partitions on) SD-cards at their new (since SailfishOS 2.2.0) mount point.
