Name:       	mount-sdcard
Summary:    	Enhanced mounting scripts for SD-cards
Version:    	0.6
Release:   	1
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
# Omit anti-dependency on future, untested SFOS versions, until a known conflict exists:
# Requires:     sailfish-version < 3.0.1

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
%{_sysconfdir}/udev/rules.d/91-mountsd.rules

%post
# Replay adapted https://git.merproject.org/olf/udisks2/blob/master/rpm/udisks2-symlink-mount-path
OLD_MOUNT_PATH="/media/sdcard"
if [ ! -L "$OLD_MOUNT_PATH" ] 
then
  DEF_UID="$(grep '^UID_MIN' /etc/login.defs | tr -s ' ' | cut -f 2 -d ' ')"
  DEVICEUSER="$(getent passwd $DEF_UID | sed 's/:.*//')"
  for path in "$OLD_MOUNT_PATH"/*
  do
    if [ -L "$path" ]
    then rm -f "$path"
    else rmdir "$path"
    fi
  done
  if rmdir "$OLD_MOUNT_PATH"
  then ln -s "/run/media/$DEVICEUSER" "$OLD_MOUNT_PATH"
  else
    echo '[%{name}] Warning:'
    echo "$OLD_MOUNT_PATH does either not exist, is not a directory or contains files or non-empty directories."
    echo "Thus omitting creation of compatibility symlink $OLD_MOUNT_PATH -> /run/media/${DEVICEUSER}!"
  fi
fi

