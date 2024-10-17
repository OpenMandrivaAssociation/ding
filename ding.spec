Summary: A Dictionary Lookup program
Name: ding
Version: 1.7
Release: 4
License: GPL 
Group: System/Internationalization
Source: ftp://ftp.tu-chemnitz.de/pub/Local/urz/ding/ding-%{version}.tar.bz2
Patch: ding-1.5-xdg.patch
Patch1: ding-1.5-encoding.patch
URL: https://www-user.tu-chemnitz.de/~fri/ding/
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: desktop-file-utils
BuildRequires: imagemagick
Requires: tcl >= 8.0
Requires: tk >= 8.0
Requires: aspell-en
Requires: aspell-de

%description 
Ding (DIctionary Nice Grep) is a tool to lookup words in dictionaries.
It uses tools like agrep, dict, ispell/aspell etc. It contains a program 
(ding) written in Tcl/Tk and a German - English dictionary with about
180,000 translations.

%prep 
%setup -q
%patch -p1 -b .xdg
%patch1 -p1 -b .encoding

%build
%install
echo $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/dict
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp ding $RPM_BUILD_ROOT%{_bindir}/ding
cp de-en.txt $RPM_BUILD_ROOT%{_datadir}/dict/de-en.txt
cp ding.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/ding.png
cp ding.desktop $RPM_BUILD_ROOT%{_datadir}/applications/ding.desktop
cp ding.1 $RPM_BUILD_ROOT%{_mandir}/man1/ding.1
mkdir -p %buildroot{%_liconsdir,%_miconsdir,%_iconsdir}
ln -s %_datadir/pixmaps/%name.png %buildroot%_iconsdir/
convert -scale 16 %name.png %buildroot%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files 
%defattr(-,root,root)
%doc README
%doc CHANGES
%doc COPYING
%{_bindir}/ding
%{_datadir}/dict/de-en.txt
%{_datadir}/pixmaps/ding.png
%{_datadir}/applications/ding.desktop
%{_mandir}/man1/ding.1*
%_iconsdir/%name.png
%_miconsdir/%name.png


%changelog
* Thu Sep 15 2011 Götz Waschk <waschk@mandriva.org> 1.7-2mdv2012.0
+ Revision: 699820
- rebuild

* Tue Sep 14 2010 Götz Waschk <waschk@mandriva.org> 1.7-1mdv2011.0
+ Revision: 578234
- update to new version 1.7

* Sat May 09 2009 Götz Waschk <waschk@mandriva.org> 1.6-1mdv2011.0
+ Revision: 373842
- update to new version 1.6

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.5-3mdv2009.0
+ Revision: 244337
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.5-1mdv2008.1
+ Revision: 136365
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 1.5-1mdv2007.1
+ Revision: 13548
- Import ding



* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 1.5-1mdv2007.1
- fix deps
- rediff patches
- New version 1.5

* Sat Aug  5 2006 Götz Waschk <waschk@mandriva.org> 1.4-4mdv2007.0
- fix patch 1

* Thu Aug  3 2006 Götz Waschk <waschk@mandriva.org> 1.4-3mdv2007.0
- fix setting of the encoding

* Thu Aug  3 2006 Götz Waschk <waschk@mandriva.org> 1.4-2mdv2007.0
- add debian menu entry for backports
- depend on locales-de

* Wed Aug  2 2006 Götz Waschk <waschk@mandriva.org> 1.4-1mdv2007.0
- initial mdv version

* Fri Jan 21 2005 Frank Richter <frank.richter@hrz.tu-chemnitz.de>
- version 1.4

* Wed Feb 11 2004 Frank Richter <frank.richter@hrz.tu-chemnitz.de>
- Time to start a changelog ...
- Changes for version 1.3, fiddling with *.desktop files
