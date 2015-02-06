%define upstream_name       SQL-Statement
%define upstream_version 1.405

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.405
Release:	3

Summary:	SQL parsing and processing engine
License:	GPL
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SQL/SQL-Statement-1.405.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Clone)
BuildRequires:	perl(Params::Util)

BuildArch:	noarch

%description
The SQL::Statement module implements a pure Perl SQL parsing and execution
engine. While it by no means implements full ANSI standard, it does support
many features including column and table aliases, built-in and user-defined
functions, implicit and explicit joins, complexly nested search conditions, and
other features.

%prep 
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
SQL_STATEMENT_WARN_UPDATE=sure perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/SQL
%{_mandir}/*/*


%changelog
* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 1.330.0-2mdv2011.0
+ Revision: 640781
- rebuild to obsolete old packages

* Mon Feb 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.330.0-1
+ Revision: 636616
- update to new version 1.33

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.320.0-1
+ Revision: 635243
- update to new version 1.32

* Tue Aug 17 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.310.0-1mdv2011.0
+ Revision: 570746
- update to 1.31

* Sun Aug 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.300.0-1mdv2011.0
+ Revision: 567731
- new version

* Fri Jul 16 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.280.0-1mdv2011.0
+ Revision: 553973
- update to 1.28

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.270.0-1mdv2011.0
+ Revision: 552629
- update to 1.27

* Sun Apr 18 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.260.0-1mdv2010.1
+ Revision: 536212
- update to 1.26

* Tue Mar 16 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.250.0-1mdv2010.1
+ Revision: 521629
- update to 1.25

* Sat Nov 21 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.230.0-1mdv2010.1
+ Revision: 467878
- update to 1.23

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.220.0-1mdv2010.1
+ Revision: 461357
- update to 1.22

* Sun Aug 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.200.0-1mdv2010.0
+ Revision: 419915
- new perl version macro
- fix one of the two failing tests, ignore other

* Fri Mar 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2009.1
+ Revision: 349681
- update to new version 1.20

* Mon Feb 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.19-1mdv2009.1
+ Revision: 338673
- update to new version 1.19

* Sat Jan 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.17-1mdv2009.1
+ Revision: 333300
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.15-4mdv2009.0
+ Revision: 241906
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 1.15-2mdv2008.0
+ Revision: 23891
- rebuild


* Wed Mar 01 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.15-1mdk
- New release 1.15

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.14-2mdk
- fix url
- Fix Source
- remove -q
- mkrel

* Mon May 09 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.14-1mdk
- 1.14
- Convert files to Unix end of lines, don't leave them executable

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.09-1mdk
- 1.09

* Fri Aug 15 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.005-5mdk
- rebuild for new perl
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.005-4mdk
- rebuild for new auto{prov,req}

* Mon May 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.005-3mdk
- buildrequires


