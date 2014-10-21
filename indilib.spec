%define _disable_ld_no_undefined 1

%define major 0
%define libname %mklibname indi %{major}
%define libindidriver %mklibname indidriver %{major}
%define libindimain %mklibname indimain %{major}
%define libindiAD %mklibname indiAlignmentDriver %{major}
%define devname %mklibname indi -d
%define sdevname %mklibname indi -d -s

Summary:	Library to control astronomical devices
Name:		indilib
Version:	0.9.8.1
Release:	1
License:	LGPLv2+
Group:		Development/C
Url:		http://indi.sourceforge.net/
Source0:	http://downloads.sourceforge.net/indi/libindi_%{version}.tar.gz
Patch0:		libindi-0.9.8-static-client.patch
Patch1:		libindi-0.9.8.1-mathplugin.patch
BuildRequires:	cmake
BuildRequires:	systemd-units
BuildRequires:	boost-devel
BuildRequires:	jpeg-devel
BuildRequires:	libfli-devel
BuildRequires:	libnova-devel
BuildRequires:	pkgconfig(cfitsio)
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
%{_udevrulesdir}/99-gpusb.rules

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

%package -n %{libindimain}
Summary:	Library files for INDI
Group:		Development/C
Conflicts:	%{_lib}indi0 < 0.9.8

%description -n %{libindimain}
This package contains library files of indilib.

%files -n %{libindimain}
%{_libdir}/libindimain.so.%{major}*

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
Requires:	%{libindimain} = %{EVRD}
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
%{_libdir}/libindimain.so
%{_libdir}/libindiAlignmentDriver.so
%{_libdir}/pkgconfig/libindi.pc
%{_includedir}/libindi/*.h

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
%setup -qn libindi-0.9.8
%patch0 -p1
%patch1 -p1

%build
%cmake
%make

%install
%makeinstall_std -C build

