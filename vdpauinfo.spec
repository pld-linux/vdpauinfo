Summary:	VDPAU information utility
Summary(pl.UTF-8):	Narzędzie podające informacje o VDPAU
Name:		vdpauinfo
Version:	0.0.6
Release:	1
License:	MIT
Group:		Applications/System
Source0:	http://people.freedesktop.org/~aplattner/vdpau/%{name}-%{version}.tar.gz
# Source0-md5:	513df206613cbd061b6d49cdbfe927ef
BuildRequires:	libstdc++-devel
BuildRequires:	libvdpau-devel >= 0.2
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line utility for querying the capabilities of a VDPAU
device.

%description -l pl.UTF-8
Działające z linii poleceń narzędzie do sprawdzania możliwości
urządzenia VDPAU.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
