%define _disable_ld_no_undefined 1
%define _disable_lto 1
%define oname indi

%define major 2
%define libname %mklibname indi %{major}
%define libindidriver %mklibname indidriver %{major}
%define libindiAD %mklibname indiAlignmentDriver %{major}
%define libindilx200 %mklibname indilx200 %{major}
%define libindiclient %mklibname indiclient %{major}
%define libindiclientqt %mklibname indiclientqt %{major}
%define devname %mklibname indi -d
%define sdevname %mklibname indi -d -s
%define oldlibname %mklibname indi 2
%define oldlibindidriver %mklibname indidriver 2
%define oldlibindiAD %mklibname indiAlignmentDriver 2
%define oldlibindilx200 %mklibname indilx200 2
%define oldlibindiclient %mklibname indiclient 2
%define oldlibindiclientqt %mklibname indiclientqt 2

Summary:	Library to control astronomical devices
Name:		indilib
Version:	2.0.8
Release:	1
License:	LGPLv2+
Group:		Development/C
Url:		https://www.indilib.org/
Source0:	https://github.com/indilib/indi/archive/v%{version}/%{oname}-%{version}.tar.gz
# Fix build with lld
Patch0:		indi-1.8.5-lld.patch
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	ninja
BuildRequires:	systemd
BuildRequires:	boost-devel
BuildRequires:	jpeg-devel
BuildRequires:	libfli-devel
BuildRequires:	libnova-devel
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libev)
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
BuildRequires:	pkgconfig(openssl)
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
Obsoletes:	%{oldlibindidriver} < %{EVRD}

%description -n %{libindidriver}
This package contains library files of indilib.

%files -n %{libindidriver}
%{_libdir}/libindidriver.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libindiAD}
Summary:	Library files for INDI
Group:		Development/C
Obsoletes:	%{oldlibindiAD} < %{EVRD}

%description -n %{libindiAD}
This package contains library files of indilib.

%files -n %{libindiAD}
%{_libdir}/libindiAlignmentDriver.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libindilx200}
Summary:	Library files for INDI Lx200
Group:		Development/C
Obsoletes:	%{oldlibindilx200} < %{EVRD}

%description -n %{libindilx200}
This package contains library files of indilib Lx200.

%files -n %{libindilx200}
# More of a module than a library, let's not
# spam the -devel package
%{_libdir}/libindilx200.so
%{_libdir}/libindilx200.so.%{major}*


#----------------------------------------------------------------------------

%package -n %{libindiclient}
Summary:	Library files for INDI
Group:		Development/C
Obsoletes:	%{oldlibindiclient} < %{EVRD}

%description -n %{libindiclient}
This package contains library files of indilib.

%files -n %{libindiclient}
%{_libdir}/libindiclient.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libindiclientqt}
Summary:	Library files for INDI
Group:		Development/C
Obsoletes:	%{oldlibindiclientqt} < %{EVRD}

%description -n %{libindiclientqt}
This package contains library files of indilib.

%files -n %{libindiclientqt}
%{_libdir}/libindiclientqt.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	INDI devellopment files
Group:		Development/C
Requires:	%{libindidriver} = %{EVRD}
Requires:	%{libindiAD} = %{EVRD}
Requires:	%{libindiclient} = %{EVRD}
Requires:	%{libindiclientqt} = %{EVRD}
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
%{_libdir}/libindiclient.so
%{_libdir}/libindiclientqt.so
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
	-DINDI_BUILD_QT5_CLIENT:BOOL=ON \
	-DLIBEV_INCLUDE_DIR=%{_includedir}/libev \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
