%define shortname indi

Summary: Library to control astronomical devices
Name: indilib
Version: 0.5
Release: %mkrel 1
Source0: http://nchc.dl.sourceforge.net/sourceforge/indi/%name-%version.tar.gz
Patch0: indilib-0.5-gcc-4.3.patch
License: LGPLv2+
Group: Development/C
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://indi.sourceforge.net/
BuildRequires: zlib-devel libusb-devel
Provides: indi = %version-%release
ExclusiveArch: x86_64 %{ix86}

%description
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

%define libname %mklibname %shortname 0
%package -n %libname
Summary: Librar file for INDI
Group: Development/C

%description -n %libname
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

This package contains library files of indilib.

%define develname %mklibname -d %shortname
%package -n %develname
Summary: INDI devellopment files
Group: Development/C
Provides: indi-devel = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %{_lib}indi-devel

%description -n %develname
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

This package contains files need to build applications using indilib.

%prep
%setup -q -n %shortname
%patch0 -p0

%build
%configure2_5x --disable-static --enable-libusb
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p %buildroot%_includedir
cp src/*.h %buildroot%_includedir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog NEWS README TODO
%_bindir/*
%_datadir/%shortname

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.0*

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog src/README
%doc src/examples
%_libdir/*.so
%_libdir/*.la
%_includedir/*.h

