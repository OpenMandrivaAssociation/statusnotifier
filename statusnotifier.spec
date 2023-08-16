%define	major	1
%define	api		1.0
%define libname %mklibname %{name}
%define devname %mklibname %{name} -d
%define girname %mklibname %{name}-gir %{api}

Summary:	Library to use KDE's StatusNotifierItem via GObject 
Name:		statusnotifier
Version:	1.0.0
Release:	1
Group:		System/Libraries
License:	GPLv3+
URL:		https://jjacky.com/statusnotifier
Source0:	https://jjacky.com/statusnotifier/%{name}-%{version}.tar.xz
# (mageia)
Patch1:		0001-Fix-gtk-doc-build-with-libtool.patch
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(dbusmenu-glib-0.4)
BuildRequires:	pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)

%description
Starting with Plasma Next, KDE doesn't support the XEmbed systray in favor
of their own Status Notifier Specification.

This little library allows to easily create a GObject to manage a
StatusNotifierItem, handling all the DBus interface and letting you simply
deal with the object's properties and signals.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library to use KDE's StatusNotifierItem via GObject 
Group:		System/Libraries

%description -n %{libname}
Starting with Plasma Next, KDE doesn't support the XEmbed systray in favor
of their own Status Notifier Specification.

This little library allows to easily create a GObject to manage a
StatusNotifierItem, handling all the DBus interface and letting you simply
deal with the object's properties and signals.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{girname}
Summary:	GObject Introspection interface description for statusnotifier
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for statusnotifier.

%files -n %{girname}
%{_libdir}/girepository-1.0/StatusNotifier-%{api}.typelib

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for the statusnotifier library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development header and library for the %{name}.

%files -n %{devname}
%{_includedir}/%{name}*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/StatusNotifier-%{api}.gir
%doc %{_datadir}/gtk-doc/html/%{name}/

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
	--enable-dbusmenu=yes \
	--enable-introspection=yes
%make_build

%install
%make_install

# remove static stuff
#find %{buildroot} -name "*.la" -delete

%check
make check

