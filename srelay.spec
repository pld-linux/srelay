Summary:	A socks 4/5 protocol proxy server
Summary(pl.UTF-8):	Serwer SOCKS dla SOCKS4 i SOCKS5
Name:		srelay
Version:	0.4.8b5
Release:	0.1
License:	GPL
Group:		Daemons
Source0:	http://downloads.sourceforge.net/project/socks-relay/socks-relay/srelay-0.4.8/%{name}-%{version}.tar.gz
# Source0-md5:	d23c1981e9cb07a05729de4251a70e5a
URL:		http://socks-relay.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libwrap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Srelay is a socks 4/5 protocol proxy server.
Supports socks connect/bind request in the protocol v4, v4a, and v5.
Supports socks server chaining with both v4 and v5 servers.
Supports Username/Password authentication in v5 (not recommended).
Supports IPv6 as well as IPv4. 

%description -l pl.UTF-8
Serwer SOCKS dla SOCKS4 i SOCKS5.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D srelay  $RPM_BUILD_ROOT%{_bindir}/srelay
install -D srelay.8    $RPM_BUILD_ROOT%{_mandir}/man8/srelay.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/srelay
%{_mandir}/man8/*
