%define		_class		Net
%define		_subclass	Ping
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	2.4.5
Release:	6
Summary:	Execute ping
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Net_Ping/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This package provides a PHP wrapper around the ping command.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4.5-4mdv2012.0
+ Revision: 742162
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4.5-3
+ Revision: 679482
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4.5-2mdv2011.0
+ Revision: 613734
- the mass rebuild of 2010.1 packages

* Mon Nov 30 2009 Oden Eriksson <oeriksson@mandriva.com> 2.4.5-1mdv2010.1
+ Revision: 471994
- 2.4.5 (fixes CVE-2009-4024)

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.4-3mdv2010.1
+ Revision: 468712
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 2.4.4-2mdv2010.0
+ Revision: 441489
- rebuild

* Sun Mar 22 2009 Funda Wang <fwang@mandriva.org> 2.4.4-1mdv2009.1
+ Revision: 360151
- new version 2.4.4

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 2.4.1-3mdv2009.1
+ Revision: 322495
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 2.4.1-2mdv2009.0
+ Revision: 236992
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 2.4.1-1mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 2.4.1-1mdv2007.0
+ Revision: 82400
- Import php-pear-Net_Ping

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 2.4.1-1mdk
- 2.4.1
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 2.4-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 2.4-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 2.4-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.4-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 2.4-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 2.4-1mdk
- initial Mandriva package (PLD import)

