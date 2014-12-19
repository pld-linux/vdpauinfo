Summary:	VDPAU information utility
Summary(pl.UTF-8):	Narzędzie podające informacje o VDPAU
Name:		vdpauinfo
Version:	0.9
Release:	1
License:	MIT
Group:		Applications/System
Source0:	http://people.freedesktop.org/~aplattner/vdpau/%{name}-%{version}.tar.gz
# Source0-md5:	f48e7ce838146021a138592ca9bdffc8
BuildRequires:	libstdc++-devel
BuildRequires:	libvdpau-devel >= 0.9
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
Requires:	libvdpau >= 0.2
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
