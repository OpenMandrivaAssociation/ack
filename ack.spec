%define module  ack
%define name	%module
%define version 1.28
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Grep-like text finder for large trees of text
License:	GPL or Artistic
Group:		Text tools
Url:		http://search.cpan.org/dist/%{module}
Source:		%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl
BuildRequires:	perl-File-Next
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
%{__make} test

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



