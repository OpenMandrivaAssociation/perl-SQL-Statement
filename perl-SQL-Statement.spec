%define upstream_name       SQL-Statement
%define upstream_version 1.28

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	SQL parsing and processing engine
License:	GPL
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/SQL/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Clone)
BuildRequires:  perl(Params::Util)

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
The SQL::Statement module implements a pure Perl SQL parsing and execution
engine. While it by no means implements full ANSI standard, it does support
many features including column and table aliases, built-in and user-defined
functions, implicit and explicit joins, complexly nested search conditions, and
other features.

%prep 
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
SQL_STATEMENT_WARN_UPDATE=sure %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/SQL
%{_mandir}/*/*
