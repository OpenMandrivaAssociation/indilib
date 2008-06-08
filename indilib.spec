%define name indilib
%define version 0.3
%define release %mkrel 4

%define shortname indi

%define libname %{_lib}%{shortname}

Summary: Library to control astronomical devices
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}.tar.bz2
License: LGPL
Group: Development/C
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://indi.sourceforge.net/
BuildRequires: zlib-devel
Provides: indi = %version-%release
ExclusiveArch: x86_64 %{ix86}

%description
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

%package -n %libname-devel
Summary: INDI devellopment files
Group: Development/C
Provides: indi-devel = %version-%release
Provides: %name-devel = %version-%release

%description -n %libname-devel
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

This package contains files need to build applications using indilib.

%prep
%setup -q -n %shortname

find . -name "CVS"        -depth -exec rm -fr {} \;
find . -name ".cvsignore" -depth -exec rm -fr {} \;

%build
%configure

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

mkdir -p %buildroot{%_libdir,%_includedir}

cp src/*.a %buildroot%_libdir/

cp src/*.h %buildroot%_includedir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog NEWS README TODO
%_bindir/*
%_datadir/%shortname

%files -n %libname-devel
%defattr(-,root,root)
%doc ChangeLog src/README
%doc src/examples src/INDI.dtd
%_libdir/*
%_includedir/*.h

