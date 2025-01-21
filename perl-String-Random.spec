#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-String-Random
Version  : 0.32
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/String-Random-0.32.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/String-Random-0.32.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libstring-random-perl/libstring-random-perl_0.29-1.debian.tar.xz
Summary  : 'Perl module to generate random strings based on a pattern'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-String-Random-license = %{version}-%{release}
Requires: perl-String-Random-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution String-Random,
version 0.32:
Perl module to generate random strings based on a pattern

%package dev
Summary: dev components for the perl-String-Random package.
Group: Development
Provides: perl-String-Random-devel = %{version}-%{release}
Requires: perl-String-Random = %{version}-%{release}

%description dev
dev components for the perl-String-Random package.


%package license
Summary: license components for the perl-String-Random package.
Group: Default

%description license
license components for the perl-String-Random package.


%package perl
Summary: perl components for the perl-String-Random package.
Group: Default
Requires: perl-String-Random = %{version}-%{release}

%description perl
perl components for the perl-String-Random package.


%prep
%setup -q -n String-Random-0.32
cd %{_builddir}
tar xf %{_sourcedir}/libstring-random-perl_0.29-1.debian.tar.xz
cd %{_builddir}/String-Random-0.32
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/String-Random-0.32/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
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
cp %{_builddir}/String-Random-0.32/LICENSE %{buildroot}/usr/share/package-licenses/perl-String-Random/38e94f89ec602e1a6495ef7c30477d01aeefedc9
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/String::Random.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-String-Random/38e94f89ec602e1a6495ef7c30477d01aeefedc9

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
