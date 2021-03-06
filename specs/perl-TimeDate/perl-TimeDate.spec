# $Id$
# Authority: dag

### EL6 ships with perl-TimeDate-1.16-11.1.el6
%{?el6:# Tag: rfx}
### EL5 ships with perl-TimeDate-1.16-5.el5
%{?el5:# Tag: rfx}
### EL4 ships with perl-TimeDate-1.16-5.el4
%{?el4:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name TimeDate

Summary: TimeDate module for perl
Name: perl-TimeDate
Version: 1.20
Release: 1%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/TimeDate/

Source: http://www.cpan.org/authors/id/G/GB/GBARR/TimeDate-%{version}.tar.gz
#Source: http://www.cpan.org/modules/by-module/TimeDate/TimeDate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker) >= 0:5.00503
Requires: perl >= 0:5.00503

%description
TimeDate module for perl

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Date/
%{perl_vendorlib}/Time/

%changelog
* Sun Feb 20 2011 Denis Fateyev <denis@fateyev.com> - 1.20-1
- Updated to version 1.20.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.16-1.2
- Rebuild for Fedora Core 5.

* Mon Feb 21 2005 Dag Wieers <dag@wieers.com> - 1.16-1
- Cosmetic cleanup.

* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.16-0
- Initial package. (using DAR)
