Name:          mount-sdcard
Summary:       Enhanced mounting scripts for SD-cards
Version:       1.2.2
# Stop evaluating the Release tag content (only set it) and cease including it in git tags since v1.2.0, 
# in order to satisfy OBS' git_tar.  Consequently switch to a three field semantic versioning scheme for
# releases and their git tags.
# Hence any changes to the spec file now always trigger an increase of the bug fix release number, i.e.
# the third field of the Version.
# But the Release tag is now merely used to monotonically count up through all releases (starting from 1).
# Note that no other release identifiers shall be used.
Release:       15
Group:         System/Base
Distribution:  SailfishOS
Vendor:        olf
Packager:      olf
License:       MIT
URL:           https://github.com/Olf0/%{name}
Source:        https://github.com/Olf0/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# rpmbuild (as of v4.14.1) handles the Icon tag awkwardly and in contrast to the Source tag(s):
# It only accepts a GIF or XPM file (successfully tested GIF89a and XPMv3) in the SOURCE directory
# (but not in the tarball)!  Hence only to be used, when the file is put there:
# Icon:         smartmedia_unmount.128x128.gif
BuildArch:     noarch
Requires:      systemd
Requires:      udisks2 >= 2.8.1+git5-1.12.1.jolla
# Better use direct dependencies than indirect ones (here: the line above versus the one below), but
# ultimately decided to use both in this case:
Requires:      sailfish-version >= 3.2.1
# Omit anti-dependency on future, untested SFOS versions, until a known conflict exists:
# Requires:     sailfish-version < 3.9.9

%description
%{summary}

%prep
%setup

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}
cp -R systemd %{buildroot}%{_sysconfdir}/

%files
%defattr(-,root,root,-)
%{_sysconfdir}/systemd/system/mount-sd@.service

