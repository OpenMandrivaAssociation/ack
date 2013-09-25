%define upstream_name    ack
%define upstream_version 2.10
%bcond_with	 beta

Name:		%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
%if %{with beta}
Release: 0.%{with beta}
%else
Release: 1
%endif
Summary:	Grep-like text finder for large trees of text
License:	GPL+ or Artistic
Group:		Text tools
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/P/PE/PETDANCE/%{upstream_name}-%{upstream_version}.tar.gz
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


