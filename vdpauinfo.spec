Summary:	VDPAU query too
Name:		vdpauinfo
Version:	0.0.6
Release:	1
License:	BSD-like ?
Group:		Applications/System
Source0:	http://people.freedesktop.org/~aplattner/vdpau/%{name}-%{version}.tar.gz
# Source0-md5:	513df206613cbd061b6d49cdbfe927ef
BuildRequires:	libvdpau-devel >=0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
command line utility for querying the capabilities of a VDPAU
device.

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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
