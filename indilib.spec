%define shortname indi

Name:		indilib
Version:	0.9
Release:	1
Summary:	Library to control astronomical devices
Source0:	http://downloads.sourceforge.net/indi/libindi_%{version}.tar.gz
Patch1:		libindi-0.8-libsuffix.patch
Patch2:		libindi0_0.6-fix-str-fmt.patch
License:	LGPLv2+
Group:		Development/C
Url:		http://indi.sourceforge.net/
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
%{_libdir}/*.a
%{_libdir}/pkgconfig/libindi.pc
%{_includedir}/libindi/*.h

#--------------------------------------------------------------------

%prep
%setup -q -n libindi-%{version}
%patch1 -p1
%patch2 -p0

%build
%cmake
%make

%install
%makeinstall_std -C build

