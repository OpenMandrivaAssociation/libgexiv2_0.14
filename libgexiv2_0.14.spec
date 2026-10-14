%define url_ver %(echo %{version}|cut -d. -f1,2)

%define gir_major 0.10
%define major 2
%define libname %mklibname gexiv2_ %{major}
%define girname %mklibname gexiv2-gir %{gir_major}
%define devname %mklibname -d gexiv2_2

Summary:	A GObject-based wrapper around the Exiv2 library
Name:		libgexiv2_0.14
Version:	0.14.7
Release:	2
License:	GPLv2+
Group:		Graphics
Url:		https://wiki.gnome.org/Projects/gexiv2
Source0:	https://download.gnome.org/sources/gexiv2/%{url_ver}/gexiv2-%{version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:	libtool
BuildRequires:	sed
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-gi

%description
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%package -n %{libname}
Summary:	A GObject-based wrapper around the Exiv2 library
Group:		Graphics

%description -n %{libname}
gexiv2 is a GObject-based wrapper around the Exiv2 library. It makes
the basic features of Exiv2 available to GNOME applications.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}gexiv2_2 < 0.6.1-2

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	A GObject-based wrapper around the Exiv2 library
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%autosetup -n gexiv2-%{version} -p1

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libgexiv2.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/*-%{gir_major}.typelib

%files -n %{devname}
%doc %{_datadir}/gtk-doc/
%{_includedir}/gexiv2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*-%{gir_major}.gir
%{_datadir}/vala/vapi/gexiv2.vapi
%{_datadir}/vala/vapi/gexiv2.deps
%{python_sitelib}/gi/overrides/GExiv2.py
%{python_sitelib}/gi/overrides/__pycache__/GExiv2.cpython-*.pyc
