Summary: A Dictionary Lookup program
Name: ding
Version: 1.5
Release: %mkrel 1
License: GPL 
Group: System/Internationalization
Source: ftp://ftp.tu-chemnitz.de/pub/Local/urz/ding/ding-%{version}.tar.bz2
Patch: ding-1.5-xdg.patch
Patch1: ding-1.5-encoding.patch
URL: http://www-user.tu-chemnitz.de/~fri/ding/
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick
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
