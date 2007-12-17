%define	module	SQL-Statement
%define	name	perl-%{module}
%define	version	1.15
%define	release	%mkrel 2

Name:		%{name}
Summary:	%{module} module for perl (String_Lang_Text_Proc/SQL)
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JZ/JZUCKER/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:perl-devel
%endif
BuildArch:	noarch

%description
%{module} is a Perl module engine for parsing and processing SQL data.

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
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/SQL/*
%{_mandir}/*/*

