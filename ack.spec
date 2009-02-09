%define module  ack
%define name	%module
%define version 1.88
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Grep-like text finder for large trees of text
License:	GPL or Artistic
Group:		Text tools
Url:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl
BuildRequires:	perl(File::Next)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
ack is a grep-like program with optimizations for searching through large trees
of source code.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# tests failing on cluster because they seem to require a real term.
# ==> skipping tests for now
#%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/App/*
%{_mandir}/*/*
%{_bindir}/*



