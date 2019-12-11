Name:          mount-sdcard
Summary:       Enhanced mounting scripts for SD-cards
Version:       1.1
Release:       1
Group:         System/Base
Distribution:  SailfishOS
Vendor:        olf
Packager:      olf
License:       MIT
URL:           https://github.com/Olf0/%{name}
Source:        https://github.com/Olf0/%{name}/archive/%{version}-%{release}/%{name}-%{version}-%{release}.tar.gz
BuildArch:     noarch
Requires:      systemd
Requires:      udisks2
Requires:      sailfish-version >= 3.2.1
# Omit anti-dependency on future, untested SFOS versions, until a known conflict exists:
# Requires:     sailfish-version < 3.9.9

%description
%{summary}

%prep
%setup -n %{name}-%{version}-%{release}

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}
cp -R systemd %{buildroot}%{_sysconfdir}/

%files
%defattr(-,root,root,-)
%{_sysconfdir}/systemd/system/mount-sd@.service

