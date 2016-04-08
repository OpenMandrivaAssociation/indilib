%define _disable_ld_no_undefined 1

%define major 1
%define libname %mklibname indi %{major}
%define libindidriver %mklibname indidriver %{major}
%define libindiAD %mklibname indiAlignmentDriver %{major}
%define devname %mklibname indi -d
%define sdevname %mklibname indi -d -s

Summary:	Library to control astronomical devices
Name:		indilib
Version:	1.2.0
Release:	1
License:	LGPLv2+
Group:		Development/C
Url:		http://indi.sourceforge.net/
Source0:	http://downloads.sourceforge.net/indi/libindi_%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	systemd-units
BuildRequires:	boost-devel
BuildRequires:	jpeg-devel
BuildRequires:	libfli-devel
BuildRequires:	libnova-devel
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(zlib)
Provides:	indi = %{EVRD}

%description
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

%files
%doc ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/indi
%{_libdir}/indi
%{_udevrulesdir}/*.rules

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library files for INDI
Group:		Development/C

%description -n %{libname}
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

This package contains library files of indilib.

%files -n %{libname}
%{_libdir}/libindi.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libindidriver}
Summary:	Library files for INDI
Group:		Development/C
Conflicts:	%{_lib}indi0 < 0.9.8

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

%package -n %{devname}
Summary:	INDI devellopment files
Group:		Development/C
Requires:	%{libname} = %{EVRD}
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
%{_libdir}/libindi.so
%{_libdir}/libindidriver.so
%{_libdir}/libindiAlignmentDriver.so
%{_libdir}/pkgconfig/libindi.pc
%{_includedir}/libindi/*.h
%{_includedir}/libindi/alignment/

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
%setup -qn libindi_%{version}

%build
%cmake
%make

%install
%makeinstall_std -C build

