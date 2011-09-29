%define upstream_name    ack
%define upstream_version 1.96

Name:		%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Grep-like text finder for large trees of text
License:	GPL+ or Artistic
Group:		Text tools
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl
BuildRequires:	perl(File::Next)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
#%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes 
%{perl_vendorlib}/App/*
%{_mandir}/*/*
%{_bindir}/*

