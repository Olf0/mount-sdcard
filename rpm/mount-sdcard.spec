Name:          mount-sdcard
Summary:       Enhanced mounting scripts for SD-cards
Version:       1.5.0
# Since v1.4.2, the release version consists of two or three fields, separated by a dot ("."):
# - The first field must contain a natural number greater than zero.
#   This number may be prefixed by one of {alpha,beta,stable}, e.g. "alpha13".
# - The second field indicates the minimal required SailfishOS version A.B.C.X in the format "sfosABC";
#   the fourth field of a SailfishOS version ("X") is neither depended upon or denoted.
# - An optional third field might be used by downstream packagers, who alter the package but want to
#   retain the exact version number.  It shall consist of the packager's name appended with a natural 
#   number greater than zero, e.g "joe8".
Release:       1.sfos220
Group:         System/Base
Distribution:  SailfishOS
Vendor:        olf
Packager:      olf
License:       LGPL-2.1-only
URL:           https://github.com/Olf0/%{name}
Source:        https://github.com/Olf0/%{name}/archive/%{version}-%{release}/%{name}-%{version}-%{release}.tar.gz
# rpmbuild (as of v4.14.1) handles the Icon tag awkwardly and in contrast to the Source tag(s):
# It only accepts a GIF or XPM file (a path is stripped to its basename) in the SOURCES directory
# (but not inside a tarball there)!  Successfully tested GIF89a and XPMv3, but an XPM icon results
# in bad visual quality and large file size.
# Hence only to be used, when the file (or a symlink to it) is put there:
#Icon:          smartmedia_unmount.256x256.gif
BuildArch:     noarch
Requires:      systemd
Requires:      udisks2
# Better use direct dependencies than indirect ones (here: the line above versus the one below), but
# ultimately decided to use both in this case:
Requires:      sailfish-version >= 2.2.0
# Omit anti-dependency on future, untested SFOS versions, until a known conflict exists:
Requires:      sailfish-version < 3.0.1

%description
%{summary}

%prep
%setup -n %{name}-%{version}-%{release}

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}
cp -R systemd udev %{buildroot}%{_sysconfdir}/
mkdir -p %{buildroot}%{_sharedstatedir}
cp -R environment %{buildroot}%{_sharedstatedir}/

%files
%defattr(-,root,root,-)
%{_sysconfdir}/systemd/system/mount-sd@.service
%{_sysconfdir}/udev/rules.d/91-mountsd.rules
%config(noreplace) %{_sharedstatedir}/environment/udisks2/mount-sd@.conf

