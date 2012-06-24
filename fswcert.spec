Summary:	Extract FreeS/WAN ipsec keys from X.509 format certificates
Summary(pl.UTF-8):   Narzędzie tworzące klucze ipsec z certyfikatów X.509
Name:		fswcert
Version:	0.6
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.strongsec.com/freeswan/%{name}-%{version}.tar.gz
# Source0-md5:	db202a0b83ee9299efb55b7f7ab1781e
URL:		http://www.strongsec.com/freeswan/
BuildRequires:	openssl-devel >= 0.9.7d
Requires:	freeswan
Requires:	openssl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to extract FreeS/WAN RSA keys from X.509 format certificates.

%description -l pl.UTF-8
Narzędzie tworzące klucze RSA do FreeS/WAN z certyfikatów w formacie
X.509.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}
install fswcert $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_sbindir}/fswcert
