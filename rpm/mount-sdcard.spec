Name:       	mount-sdcard
Summary:    	Enhanced mounting scripts for SD-cards under SailfishOS 2.2.x
Version:    	0.1
Release:  	1
Group:      	System/Base
Distribution:	SailfishOS
Vendor:     	olf
Packager:   	olf
License:    	MIT
URL:        	https://github.com/Olf0/%{name}
Source0:    	%{name}-%{version}-%{release}.tar.gz
Source1:    	https://github.com/Olf0/%{name}/archive/%{version}-%{release}.tar.gz
BuildArch:  	noarch
BuildRequires:	systemd
Requires:   	systemd
Requires:   	udisks2
Requires: 	sailfish-version >= 2.2.0

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}-%{release}

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}
cp -R systemd udev %{buildroot}%{_sysconfdir}/

%files
%defattr(-,root,root,-)
%{_sysconfdir}/systemd/system/mount-sd@.service
%{_sysconfdir}/systemd/system/symlink-sd@.service
%{_sysconfdir}/udev/rules.d/81-mountsd.rules

