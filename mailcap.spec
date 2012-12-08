# Defined in CVS makefile.
%define	name	mailcap
%define	version	2.0.4
%define	release	%mkrel 28

Summary:	Associates helper applications with particular file types
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Public Domain
Group:		System/Configuration/Networking 
Source0:	%{name}-%{version}.tar.bz2
Source1:	mime.types
Patch0:		mailcap-2.0.4.patch
Patch1:		mailcap-2.0.4-java-web-start.patch
Patch2:		mailcap-2.0.4-ooffice.patch
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The mailcap file is used by the metamail program.  Metamail reads the
mailcap file to determine how it should display non-text or multimedia
material.  Basically, mailcap associates a particular type of file
with a particular program that a mail agent or other program can call
in order to handle the file.

Mailcap should be installed to allow certain programs to be able to
handle non-text files.

%prep
%setup -q
%patch0 -p1 -b .mdk
%patch1 -p1 -b .javastart
%patch2 -p1 -b .ooffice

%build

%install
rm -rf %{buildroot}
perl -pi -e "s!/usr/man!%{_mandir}!g" Makefile
%makeinstall

# overwrite the original one, which is outdated
install -m 0644 %{SOURCE1}  %{buildroot}/%{_sysconfdir}/mime.types

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog
%config(noreplace) %{_sysconfdir}/mailcap
%config(noreplace) %{_sysconfdir}/mailcap.vga
%config(noreplace) %{_sysconfdir}/mime.types
%{_mandir}/man4/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.4-26mdv2011.0
+ Revision: 666357
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.4-25mdv2011.0
+ Revision: 606622
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.4-24mdv2010.1
+ Revision: 523239
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.0.4-23mdv2010.0
+ Revision: 426060
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.0.4-22mdv2009.1
+ Revision: 351547
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.0.4-21mdv2009.0
+ Revision: 223141
- rebuild

* Wed Mar 26 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.0.4-20mdv2008.1
+ Revision: 190441
- update mime.types file (taken from latest apache)
- add ooffice.patch, which adds openoffice entries to mailcap
- remove outdated urls from specfile

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 30 2007 Frederic Crozat <fcrozat@mandriva.com> 2.0.4-19mdv2008.1
+ Revision: 114174
- Remove autogeneration of mailcap, back to static file (Mdv bug #35872)

  + Lenny Cartier <lenny@mandriva.org>
    - Replace xanim by totem
    - Remove menu method

* Thu May 10 2007 Lenny Cartier <lenny@mandriva.org> 2.0.4-16mdv2008.0
+ Revision: 25970
- Use qiv in main rather than ee in contribs


* Wed Feb 07 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.4-15mdv2007.0
+ Revision: 117318
- add java web start type
  cosmetics

* Wed Nov 22 2006 Lenny Cartier <lenny@mandriva.com> 2.0.4-14mdv2007.1
+ Revision: 86187
- Use mkrel & rebuild
- Import mailcap

* Thu May 12 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.0.4-13mdk
- rebuild

* Thu Feb 19 2004 Frederic Lepied <flepied@mandrakesoft.com> 2.0.4-12mdk
- do nothing when menu method is run as a normal user (bug #7935)

* Tue Feb 10 2004 Frederic Lepied <flepied@mandrakesoft.com> 2.0.4-11mdk
- name the menu method mailcap to be coherent
- add a comment at the beginning of mailcap

* Tue Feb 10 2004 Frederic Lepied <flepied@mandrakesoft.com> 2.0.4-10mdk
- use a menu method to update mailcap

