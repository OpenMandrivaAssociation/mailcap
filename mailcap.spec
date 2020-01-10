Summary:	Associates helper applications with particular file types
Name:		mailcap
Version:	2.0.4
Release:	41
License:	Public Domain
Group:		System/Configuration/Networking 
Source0:	%{name}-%{version}.tar.bz2
Source1:	mime.types
Patch0:		mailcap-2.0.4.patch
Patch1:		mailcap-2.0.4-java-web-start.patch
Patch2:		mailcap-2.0.4-ooffice.patch
BuildArch:	noarch

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
%autopatch -p1

%build

%install
sed -i -e "s!/usr/man!%{_mandir}!g" Makefile
%makeinstall

# overwrite the original one, which is outdated
install -m 0644 %{SOURCE1}  %{buildroot}/%{_sysconfdir}/mime.types

%files
%doc ChangeLog
%config(noreplace) %{_sysconfdir}/mailcap
%config(noreplace) %{_sysconfdir}/mailcap.vga
%config(noreplace) %{_sysconfdir}/mime.types
%{_mandir}/man4/*

