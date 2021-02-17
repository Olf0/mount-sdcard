# mount-sdcard
#### Enhanced mounting scripts for SD-cards under SailfishOS

This systemd unit file and the udev rules file are by-products of optimising the start-up timing, feature set and shut-down behavior of [crypto-sdcard](https://github.com/Olf0/crypto-sdcard).

They provide the following enhancements compared to SailfishOS' original versions:
* Start mounting (partitions on) SD-card via udisks at the earliest sensible time: Right after *udisks2.service* has started.
* Unmount before *udisks2.service* begins stopping, hence achieving a clean unmount.
* Also do not use SailfishOS' *udisksctl-user* script for unmounting (because this cannot work at the time ExecStop is executed), which is installed and used by SailfishOS since its release 3.2.1, and was also used by *mount-sdcard* versions 1.1-1 to 1.3.0-21; see [details here](https://github.com/Olf0/mount-sdcard/pull/2).
* Ensure, that AlienDalvik (specifically *alien-service-manager.service*) begins starting after mounting succeeded, to allow for [android_storage on SD-card](https://together.jolla.com/question/203539/guide-externalising-android_storage-and-other-directories-files-to-sd-card/#203539-2-externalising-homenemoandroid_storage).<br />
  Even more importantly (i.e., also relevant for devices without "android_storage on SD-card") this also ensures, that unmounting occurs only after AlienDalvik has completely stopped.<br />
  Nevertheless, these configuration files are also applicable to devices without AlienDalvik installed.
* Since v1.3.3: Try to evaluate the Systemd [EnvironmentFile](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#EnvironmentFile=)s `mount-sd.conf` and `mount-sd@<device-name>.conf` (in this order) located in `/var/lib/environment/udisks2/`.  *mount-sdcard* looks only for these two file names for mounting (each partition on) an SD-card, in contrast to [Jolla's original](https://git.sailfishos.org/mer-core/udisks2/blob/master/rpm/0013-Pass-extra-mount-options-to-mount-sd-service.patch), which uses any `*.conf` file in this directory for every partition the original *mount-sd.service* mounts.<br />
  Note that *mount-sdcard* actually deploys `/var/lib/environment/udisks2/mount-sd.conf` (in contrast to Jolla's original), containing `UDISKS2_MOUNT_OPTIONS="-o noexec"`.  As with Jolla's original, ...
  * only the environment variable `UDISKS2_MOUNT_OPTIONS` is evaluated.
  * all other variable assignments, empty lines, empty `*.conf` files or missing files are ignored.
  * mind that *udisks2* filters the mount options: While `noexec` and `readonly` are allowed, `lazytime` results in *udisks2* refusing to mount (I have not tried any other additional mount options, but these three).
  
  If you want to execute files located on your unencrypted SD-card, do **not** delete `/var/lib/environment/udisks2/mount-sd.conf`: It will be redeployd by the next update of *mount-sdcard*.  Instead empty this file, e.g. by executing (as root) `cd /var/lib/environment/udisks2/ && rm -f mount-sd.conf && touch mount-sd.conf`
* Versions below 1.0-4: Inhibit stubbornly trying to mount block devices without a filesystem recognised by the kernel / udev.<br />
  As Jolla resolved this in SailfishOS 3.0.1 (see [commit](https://git.sailfishos.org/mer-core/udisks2/commit/6fae1738440d65deb995edb0e5d759c74729d00b) and [changelog](https://together.jolla.com/question/195733/changelog-301-sipoonkorpi/#195733-udisks2)), this workaround is omitted in *mount-sdcard 1.0-4* (and later versions), making [*v1.0-3*](https://github.com/Olf0/mount-sdcard/releases/tag/1.0-3) the last release installable on SailfishOS 2.2.0, 2.2.1 and 3.0.0.
* Versions below 1.0: Create / try to rectify the "compatibility symlink" in order to allow older apps seamlessly accessing (partitions on) SD-cards at their new (since SailfishOS 2.2.0) mount point.

Notes:
* These configuration files do not alter, replace or delete any extant files.
* Minimal SailfishOS version supported by *mount-sdcard* is 2.2.0.
* Since *mount-sdcard 1.0-4* at least [SailfishOS 3.0.1](https://github.com/Olf0/mount-sdcard/releases/tag/1.0-4) is required.
* Since *mount-sdcard 1.1-1* at least [SailfishOS 3.2.1](https://github.com/Olf0/mount-sdcard/pull/2) is required.
* Support of partitions and whole devices (as SailfishOS' original versions do).
* Support for (µ)SD-cards and USB-attached storage (if supported by device hardware and Operating System).
* An RPM built for SailfishOS is available at [OpenRepos](https://openrepos.net/content/olf/mount-sdcard).
