%define shortname indi

Summary: Library to control astronomical devices
Name: indilib
Version: 0.8
Release: 1
Source0: http://downloads.sourceforge.net/indi/libindi_%version.tar.gz
Patch1: libindi-0.8-libsuffix.patch
License: LGPLv2+
Group: Development/C
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://indi.sourceforge.net/
BuildRequires: zlib-devel libusb-devel
BuildRequires: cfitsio-devel >= 3.090
BuildRequires: libfli-devel
BuildRequires: cmake
Provides: indi = %version-%release

%description
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

%files
%defattr(-,root,root)
%doc ChangeLog NEWS README TODO
%_bindir/*
%_datadir/%shortname

#--------------------------------------------------------------------

%define libname %mklibname %shortname 0
%package -n %libname
Summary: Librar file for INDI
Group: Development/C

%description -n %libname
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

This package contains library files of indilib.

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.0*

#--------------------------------------------------------------------

%define develname %mklibname -d %shortname
%package -n %develname
Summary: INDI devellopment files
Group: Development/C
Requires: %libname = %version
Provides: indi-devel = %version-%release
Provides: %name-devel = %version-%release

%description -n %develname
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

This package contains files need to build applications using indilib.

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog README* NEWS
%_libdir/*.so
%_libdir/*.a
%_libdir/pkgconfig/libindi.pc
%_includedir/libindi/*.h

#--------------------------------------------------------------------

%prep
%setup -q -n libindi-%version
%patch1 -p0

%build
%cmake
%make

%install
%makeinstall_std -C build

