Name:       	mount-sdcard
Summary:    	Enhanced mounting scripts for SD-cards
Version:    	0.1
Release:   	2
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
Requires:     sailfish-version >= 2.2.0
Requires:     sailfish-version < 3.0.0

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
%{_sysconfdir}/udev/rules.d/81-mountsd.rules

