%define _disable_ld_no_undefined 1

%define shortname indi

Name:		indilib
Version:	0.9.6
Release:	1
Summary:	Library to control astronomical devices
License:	LGPLv2+
Group:		Development/C
Url:		http://indi.sourceforge.net/
Source0:	http://downloads.sourceforge.net/indi/libindi_%{version}.tar.gz
Patch0:		libindi-0.9.6-linkage.patch
BuildRequires:	zlib-devel
BuildRequires:	libusb-devel
BuildRequires:	cfitsio-devel >= 3.090
BuildRequires:	libfli-devel
BuildRequires:	cmake
BuildRequires:	boost-devel
Provides:	indi = %{version}-%{release}

%description
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

%files
%doc ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/%{shortname}
%{_sysconfdir}/udev/rules.d/99-gpusb.rules

#--------------------------------------------------------------------

%define major 0
%define libname %mklibname %{shortname} %{major}

%package -n %{libname}
Summary:	Library files for INDI
Group:		Development/C

%description -n %{libname}
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

This package contains library files of indilib.

%files -n %{libname}
%{_libdir}/*.so.%{major}*

#--------------------------------------------------------------------

%define develname %mklibname -d %{shortname}

%package -n %{develname}
Summary:	INDI devellopment files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	indi-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

This package contains files need to build applications using indilib.

%files -n %{develname}
%doc ChangeLog README* NEWS
%{_libdir}/*.so
%{_libdir}/pkgconfig/libindi.pc
%{_includedir}/libindi/*.h

#--------------------------------------------------------------------
%define develnamestatic %mklibname -d -s %{shortname}

%package -n %{develnamestatic}
Summary:	INDI devellopment files
Group:		Development/C
Requires:	%{name}-devel = %{version}-%{release}
Provides:	indi-devel-static = %{version}-%{release}
Provides:	%{name}-devel-static = %{version}-%{release}

%description -n %{develnamestatic}
INDI is an instrument neutral distributed interface control protocol
that aims to provide backend driver support and automation for a wide
range of Astronomical devices (telescopes, focusers, CCDs..etc).

This package contains files need to build applications using indilib.

%files -n %{develnamestatic}
%{_libdir}/*.a

#-------------------------------------------------------------------
%prep
%setup -q -n libindi-%{version}
%patch0 -p1

%build
%cmake
%make

%install
%makeinstall_std -C build

