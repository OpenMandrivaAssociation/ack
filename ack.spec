%define upstream_name    ack
%define upstream_version 3.3.1
%bcond_with	 beta

Name:		%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release: 1
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
%make_build


%install
%make_install

%files
%doc Changes 
%{perl_vendorlib}/App/*
%{_mandir}/*/*
%{_bindir}/*
