Summary:	Extract FreeS/WAN ipsec keys from X.509 format certificates
Name:		fswcert
Version:	0.6
Release:	1
URL:		http://www.strongsec.com/freeswan/
Source0:	http://www.strongsec.com/freeswan/%{name}-%{version}.tar.gz
License:	GPL
Group:		System Environment/Daemons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	freeswan
Requires:	openssl
BuildRequires:	openssl-devel

%description
Utility to extract FreeS/WAN RSA keys from X.509 format certificates

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d  $RPM_BUILD_ROOT%{_sbindir}
install --strip fswcert  $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf README CHANGES
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/fswcert


# EOF
