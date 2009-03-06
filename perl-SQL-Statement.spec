%define	module	SQL-Statement
%define	name	perl-%{module}
%define	version	1.20
%define	release	%mkrel 1

Name:		%{name}
Summary:	SQL parsing and processing engine
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/SQL/%{module}-%{version}.tar.gz
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
%setup -q -n %{module}-%{version}
# remove DOS end of lines and fix permissions
find -type f | xargs perl -pi -e 's/\cM//'
find -type f | xargs chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
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

