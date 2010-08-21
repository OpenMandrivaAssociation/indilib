%define shortname indi

Summary: Library to control astronomical devices
Name: indilib
Version: 0.6.2
Release: %mkrel 1
Source0: http://downloads.sourceforge.net/indi/libindi_%version.tar.gz
Patch1: libindi-0.6.2-libsuffix.patch
Patch2: libindi0_0.6-fix-str-fmt.patch
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
Requires: %libname = %version
Provides: indi-devel = %version-%release
Provides: %name-devel = %version-%release

%description -n %develname
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

This package contains files need to build applications using indilib.

%prep
%setup -q -n libindi-%version
%patch1 -p0
%patch2 -p0

%build
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

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
%doc ChangeLog README* NEWS
%_libdir/*.so
%_libdir/*.a
%_libdir/pkgconfig/libindi.pc
%_includedir/libindi/*.h
