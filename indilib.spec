%define _disable_ld_no_undefined 1
%define _disable_lto 1
%define oname indi

%define major 1
%define libname %mklibname indi %{major}
%define libindidriver %mklibname indidriver %{major}
%define libindiAD %mklibname indiAlignmentDriver %{major}
%define libindilx200 %mklibname indilx200 %{major}
%define devname %mklibname indi -d
%define sdevname %mklibname indi -d -s

Summary:	Library to control astronomical devices
Name:		indilib
Version:	1.9.7
Release:	1
License:	LGPLv2+
Group:		Development/C
Url:		http://www.indilib.org/
Source0:	https://github.com/indilib/indi/archive/v%{version}/%{oname}-%{version}.tar.gz
# Fix build with lld
Patch0:		indi-1.8.5-lld.patch
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	ninja
BuildRequires:	systemd-units
BuildRequires:	boost-devel
BuildRequires:	jpeg-devel
BuildRequires:	libfli-devel
BuildRequires:	libnova-devel
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(gsl)
BuildRequires:  pkgconfig(gmock)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(zlib)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(fftw3)
Provides:	indi = %{EVRD}

%description
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

%files
%doc ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/indi
%{_libdir}/indi
%{_udevrulesdir}/*.rules

#----------------------------------------------------------------------------

%package -n %{libindidriver}
Summary:	Library files for INDI
Group:		Development/C
Conflicts:	%{_lib}indi0 < 0.9.8
Obsoletes:	%{libname} < %{EVRD}

%description -n %{libindidriver}
This package contains library files of indilib.

%files -n %{libindidriver}
%{_libdir}/libindidriver.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libindiAD}
Summary:	Library files for INDI
Group:		Development/C

%description -n %{libindiAD}
This package contains library files of indilib.

%files -n %{libindiAD}
%{_libdir}/libindiAlignmentDriver.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libindilx200}
Summary:	Library files for INDI Lx200
Group:		Development/C

%description -n %{libindilx200}
This package contains library files of indilib Lx200.

%files -n %{libindilx200}
# More of a module than a library, let's not
# spam the -devel package
%{_libdir}/libindilx200.so
%{_libdir}/libindilx200.so.%{major}*


#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	INDI devellopment files
Group:		Development/C
Requires:	%{libindidriver} = %{EVRD}
Requires:	%{libindiAD} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	indi-devel = %{EVRD}

%description -n %{devname}
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

This package contains files need to build applications using indilib.

%files -n %{devname}
%doc ChangeLog README* NEWS
%{_libdir}/libindidriver.so
%{_libdir}/libindiAlignmentDriver.so
%{_libdir}/pkgconfig/libindi.pc
%{_includedir}/libindi

#----------------------------------------------------------------------------

%package -n %{sdevname}
Summary:	INDI devellopment files
Group:		Development/C
Requires:	%{name}-devel = %{EVRD}
Provides:	indi-devel-static = %{EVRD}
Provides:	%{name}-devel-static = %{EVRD}

%description -n %{sdevname}
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

This package contains files need to build applications using indilib.

%files -n %{sdevname}
%{_libdir}/*.a

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}
%cmake  \
	-DUDEVRULES_INSTALL_DIR=%{_udevrulesdir} \
	-DINDI_BUILD_QT5_CLIENT=ON \
	-G Ninja

%build
#export CC=gcc
#export CXX=g++
#global ldflags %{ldflags} -fuse-ld=bfd

%ninja_build -C build

%install
%ninja_install -C build
