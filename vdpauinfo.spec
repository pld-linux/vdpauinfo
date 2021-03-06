Summary:	VDPAU information utility
Summary(pl.UTF-8):	Narzędzie podające informacje o VDPAU
Name:		vdpauinfo
Version:	1.4
Release:	1
License:	MIT
Group:		Applications/System
#Source0Download: https://gitlab.freedesktop.org/vdpau/vdpauinfo/tags
Source0:	https://gitlab.freedesktop.org/vdpau/vdpauinfo/uploads/8f047eac351672cc4316724edb6ad2b2/%{name}-%{version}.tar.gz
# Source0-md5:	b0d43317b6bfbf4d55be07f5ad5c085f
URL:		https://freedesktop.org/wiki/Software/VDPAU/
BuildRequires:	libstdc++-devel
BuildRequires:	libvdpau-devel >= 1.4
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
Requires:	libvdpau >= 1.4
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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
