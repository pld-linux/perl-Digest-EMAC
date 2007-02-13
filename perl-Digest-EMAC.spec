#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	EMAC
Summary:	Digest::EMAC - encrypted MAC (formerly known as Double MAC)
Summary(pl.UTF-8):	Digest::EMAC - szyfrowany MAC (wcześniej znany jako podwójny MAC)
Name:		perl-Digest-EMAC
Version:	1.2
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b794a64554dc1ea9b3714e8d6825ffd6
BuildRequires:	perl-Crypt-CBC >= 2.08
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Crypt-CBC >= 2.08
Obsoletes:	perl-Digest-DMAC
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Encrypted MAC (EMAC), formerly known as Double MAC (DMAC).
Unlike HMAC, which reuses an existing one-way hash function, such as
MD5, SHA-1 or RIPEMD-160, EMAC reuses an existing block cipher to
produce a secure message authentication code (MAC).

%description -l pl.UTF-8
EMAC to jest Encrypted MAC (szyfrowany MAC), poprzednio znany jako
Double MAC (DMAC - podwójny MAC). W przeciwieństwie do HMAC, który
wykorzystuje istniejącą jednokierunkową funkcję mieszającą, taką jak
MD5, SHA-1 czy RIPEMD-160, EMAC używa istniejącego szyfru blokowego
do stworzenia bezpiecznego kodu uwierzytelniającego wiadomość
(Message Authentication Code - MAC).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Digest/EMAC.pm
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
