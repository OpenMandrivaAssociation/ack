Name:		ack
Version:	3.7.0
Release: 	1
Summary:	Grep-like text finder for large trees of text
License:	GPL+ or Artistic
Group:		Text tools
Url:		http://search.cpan.org/dist/%{name}
Source0:	http://www.cpan.org/authors/id/P/PE/PETDANCE/%{name}-v%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(File::Next)
BuildArch:	noarch

%description
ack is a grep-like program with optimizations for searching through large trees
of source code.

%prep
%autosetup -p1 -n %{name}-v%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build


%install
%make_install

%files
%doc Changes 
%{perl_vendorlib}/App/*
%{_mandir}/*/*
%{_bindir}/*
