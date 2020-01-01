Name:          mount-sdcard
Summary:       Enhanced mounting scripts for SD-cards
Version:       1.2.1
# Stop evaluating the "Release:" field (per %{release}) and cease including it in git tags since v1.2.0, 
# in order to satisfy OBS and consequently switching to a three field semantic versioning scheme for
# releases and their git tags.
# Hence any changes to the spec file now always trigger an increase of the bug fix release number, i.e.
# the third field of %{version}.
# But %{release} is now used to merely counting up monotonically through *all* releases (starting from 1).
# Note that no other release identifiers shall be used.
Release:       14
Group:         System/Base
Distribution:  SailfishOS
Vendor:        olf
Packager:      olf
License:       MIT
URL:           https://github.com/Olf0/%{name}
Source:        https://github.com/Olf0/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:     noarch
Requires:      systemd
Requires:      udisks2 >= 2.8.1+git5-1.12.1.jolla
# Requires:     sailfish-version >= 3.2.1
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

