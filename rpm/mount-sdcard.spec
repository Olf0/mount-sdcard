Name:          mount-sdcard
Summary:       Enhanced mounting scripts for media as SD-cards
Version:       1.8.2
# Since v1.4.2, the release version consists of two or three fields, separated by a dot ("."):
# - The first field must contain a natural number greater than zero.
#   This number may be prefixed by one of {alpha,beta,rc,release}, e.g. "alpha13".
# - The second field indicates the minimal required SailfishOS version A.B.C.X in the format "sfosABC";
#   the fourth field of a SailfishOS version ("X") is neither depended upon or denoted.
# - An optional third field might be used by downstream packagers, who alter the package but want to
#   retain the exact version number.  It should consist of the packager's name appended with a natural 
#   number greater than zero as the packaging release number, e.g "joe8".
Release:       1.sfos340
Group:         System/Base
Distribution:  SailfishOS
Vendor:        olf
Packager:      olf
License:       LGPL-2.1-only
URL:           https://github.com/Olf0/%{name}
# Download URLs for gzipped tarballs at GitHub must conform to: %{url}/archive/<tag-name>/<arbitrary-string>.tar.gz
Source:        %{url}/archive/%{version}-%{release}/%{name}-%{version}.tar.gz
# rpmbuild (as of v4.14.1) handles the Icon tag awkwardly and in contrast to the Source tag(s):
# It only accepts a GIF or XPM file (a path is stripped to its basename) in the SOURCES directory
# (but not inside a tarball there)!  Successfully tested GIF89a and XPMv3, but an XPM icon results
# in bad visual quality and large file size.
# Hence only to be used, when the file (or a symlink to it) is put there:
#Icon:          smartmedia_unmount.256x256.gif
BuildArch:     noarch
Requires:      systemd
Requires:      udisks2
# Better use direct dependencies on specific versions than indirect ones (here: the line above
# versus the one below) in general, but ultimately decided not to do so in this special case
# (for commonality across release versions):
Requires:      sailfish-version >= 3.4.0
# Omit anti-dependency on future, untested SFOS versions, until a known conflict exists:
# Requires:      sailfish-version < 9.9.9

%description
%{summary}, USB-attached storage etc.

%if 0%{?_chum}
PackageName: %{name}
Type: generic
Categories:
 - Utilities
 - System
DeveloperName: olf (Olf0)
Custom:
  Repo: %{url}
Icon: %{url}/raw/master/icon/smartmedia_unmount.256x256.png
Url:
  Homepage: https://openrepos.net/content/olf/%{name}
  Help: %{url}/issues
  Bugtracker: %{url}/issues
  Donation: https://openrepos.net/donate
%endif

%define _binary_payload w6.gzdio
%define _source_payload w2.gzdio

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}
cp -R polkit-1 systemd udev %{buildroot}%{_sysconfdir}/

%files
%defattr(-,root,root,-)
%{_sysconfdir}/systemd/system/mount-sd@.service
%{_sysconfdir}/udev/rules.d/91-mountsd.rules
%{_sysconfdir}/polkit-1/localauthority/50-local.d/61-mountsd.pkla
%config %{_sysconfdir}/systemd/system/mount-sd.conf

%changelog
* Thu Sep  9 1999 olf <Olf0@users.noreply.github.com> - 99.99.99
- See %{url}/releases
