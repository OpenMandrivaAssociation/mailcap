# Defined in CVS makefile.
%define	name	mailcap
%define	version	2.0.4
%define	release	%mkrel 16

Summary:	Associates helper applications with particular file types
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Public Domain
Group:		System/Configuration/Networking 
# get the source from our cvs repository (see
# http://www.linuxmandrake.com/en/cvs.php3)
Source0:	%{name}-%{version}.tar.bz2
Source1:	mimetypes
Patch0:		mailcap-2.0.4.patch
Patch1:		mailcap-2.0.4-java-web-start.patch
Url:		http://archive.ncsa.uiuc.edu/SDG/Software/Mosaic/Docs/mailcap.html
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

%build

%install
rm -rf %{buildroot}
perl -pi -e "s!/usr/man!%{_mandir}!g" Makefile
%makeinstall
mv %{buildroot}%{_sysconfdir}/mailcap{,.base}
install -m755 %{SOURCE1} -D %{buildroot}%{_sysconfdir}/menu-methods/mailcap

%pre
if [ ! -f /etc/mailcap.base -a -f /etc/mailcap ]; then
	mv /etc/mailcap /etc/mailcap.base
fi

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog
%config(noreplace) %{_sysconfdir}/mailcap.base
%config(noreplace) %{_sysconfdir}/mailcap.vga
%config(noreplace) %{_sysconfdir}/mime.types
%config(noreplace) %{_sysconfdir}/menu-methods/mailcap
%{_mandir}/man4/*

