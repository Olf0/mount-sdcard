%global branch sfos220
Name:          mount-sdcard
Summary:       Enhanced mounting scripts for media as SD-cards
# The version adheres to semantic versioning v2.0.0, see https://semver.org/
Version:       1.8.2
# Since version 1.8.2, the release version consists of two or three fields,
# separated by dots ("."):
# - The first field must contain a natural number greater than zero.  This number
#   should be prefixed by one of {alpha,beta,rc,release}, which results in, e.g.,
#   "alpha42".
# - The second field must contain the git branch from which this release is
#   built; it comprises the minimal required SailfishOS version A.B.C.X in the
#   format "sfosABC" (the fourth field of a SailfishOS version ("X") is neither
#   depended upon or denoted) plus if this is a version which utilises
#   Qualcomm's `qcrypto` kernel module by appending "+qcrypto" to this field.
# - An optional third field might be used by downstream packagers, who alter the
#   package but want to retain the exact version number.  It should consist of
#   the packager's name appended with a natural number greater than zero as the
#   packaging release number, e.g "jane23".
Release:       beta1.%{branch}
# Since v1.8.2, Git tags must adhere to the following format starting (adapted
# from Storeman's format:
# https://github.com/storeman-developers/harbour-storeman/wiki/Git-tag-format ),
# which comprises two fields separated by a slash ("/"):
# - The first field is simply the content of the `Release:` tag, i.e.,
#   `%%{release}`.
# - The second field is simply the content of the `Version:` tag, i.e.,
#   `%%{version}`.
Group:         System/Base
Distribution:  SailfishOS
Vendor:        olf
License:       LGPL-2.1-only
URL:           https://github.com/Olf0/%{name}
# Download URLs for gzipped tarballs at GitHub must conform to:
# %%{url}/archive/<tag-name>/<arbitrary-string>.tar.gz
Source0:       %{url}/archive/%{release}/%{version}/%{name}-%{version}.tar.gz
#Source99:       %{name}.rpmlintrc
# rpmbuild (as of v4.14.1) handles the Icon tag awkwardly and in contrast to
# the Source tag(s): It only accepts a GIF or XPM file (a path is stripped to
# its basename) in the SOURCES directory (but not inside a tarball there)!
# Successfully tested GIF89a and XPMv3, but an XPM icon results in bad visual
# quality and large file size.
# Hence only to be used, when the file (or a symlink to it) is put there:
#Icon:          smartmedia_unmount.256x256.gif
BuildArch:     noarch
Requires:      systemd
Requires:      udisks2
# Better use direct dependencies on specific versions than indirect ones (here:
# the line above versus the one below) in general, but ultimately decided not to
# do so in this special case (for commonality across release versions):
Requires:      sailfish-version >= 2.2.0
# Counter-dependency (necessary for the multiple release branch scheme chosen):
Requires:      sailfish-version < 3.0.1

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
%define _source_payload w6.gzdio

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
