#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-String-Random
Version  : 0.30
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/String-Random-0.30.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/String-Random-0.30.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libstring-random-perl/libstring-random-perl_0.29-1.debian.tar.xz
Summary  : 'Perl module to generate random strings based on a pattern'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-String-Random-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution String-Random,
version 0.30:
Perl module to generate random strings based on a pattern

%package dev
Summary: dev components for the perl-String-Random package.
Group: Development
Provides: perl-String-Random-devel = %{version}-%{release}

%description dev
dev components for the perl-String-Random package.


%package license
Summary: license components for the perl-String-Random package.
Group: Default

%description license
license components for the perl-String-Random package.


%prep
%setup -q -n String-Random-0.30
cd ..
%setup -q -T -D -n String-Random-0.30 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/String-Random-0.30/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-String-Random
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-String-Random/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/String/Random.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/String::Random.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-String-Random/LICENSE
