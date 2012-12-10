%define upstream_name    ack
%define upstream_version 1.96

Name:		%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Grep-like text finder for large trees of text
License:	GPL+ or Artistic
Group:		Text tools
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Next)
BuildArch:	noarch

%description
ack is a grep-like program with optimizations for searching through large trees
of source code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# tests failing on cluster because they seem to require a real term.
# ==> skipping tests for now
#make test

%install
%makeinstall_std

%files
%doc Changes 
%{perl_vendorlib}/App/*
%{_mandir}/*/*
%{_bindir}/*

%changelog
* Thu Sep 29 2011 Andrey Bondrov <abondrov@mandriva.org> 1.960.0-1mdv2012.0
+ Revision: 701880
- New version: 1.96

* Fri Mar 18 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.940.0-1
+ Revision: 646444
- fix %%doc
- update to 1.94

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.920.0-1mdv2011.0
+ Revision: 477614
- update to 1.92

* Wed Sep 09 2009 Jérôme Quelin <jquelin@mandriva.org> 1.900.0-1mdv2010.0
+ Revision: 435709
- update to 1.90

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.880.0-1mdv2010.0
+ Revision: 401463
- rebuild
- using %%perl_convert_version
- fixed license field

* Mon Feb 09 2009 Jérôme Quelin <jquelin@mandriva.org> 1.88-1mdv2009.1
+ Revision: 338870
- skipping tests since they seem to require a valid term
- better prereqs
- update to new version 1.88

* Wed Nov 12 2008 Jérôme Quelin <jquelin@mandriva.org> 1.86-1mdv2009.1
+ Revision: 302519
- update to new version 1.86

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.76-3mdv2009.0
+ Revision: 266116
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 23 2008 Jérôme Quelin <jquelin@mandriva.org> 1.76-2mdv2009.0
+ Revision: 196891
- rebuild

* Sun Mar 02 2008 Michael Scherer <misc@mandriva.org> 1.76-1mdv2008.1
+ Revision: 177690
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-not-capitalized

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 1.28-2mdv2008.1
+ Revision: 135813
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 20 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.28-2mdv2007.0
+ Revision: 71267
+ Status: not released
- Add BuildRequires
- New version

