Summary:	Bitmap Font Editor
Name:		gbdfed
Version:	1.6
Release:	1
License:	BSD 3-Clause
Group:		X11/Applications
Source0:	http://sofia.nmsu.edu/~mleisher/Software/gbdfed/%{name}-%{version}.tar.bz2
# Source0-md5:	2a2e1cbfe8566db6d302f0b9ab79b8dd
Source1:	http://sofia.nmsu.edu/~mleisher/Software/gbdfed/gbdfed16x16.png
# Source1-md5:	28625f0878e83687b4c3a293467fc926
Source2:	http://sofia.nmsu.edu/~mleisher/Software/gbdfed/gbdfed32x32.png
# Source2-md5:	da88f074603ef8dc621b05bfda5e09f9
Source3:	http://sofia.nmsu.edu/~mleisher/Software/gbdfed/gbdfed48x48.png
# Source3-md5:	3681abf22f23a62c48acfca417655dd0
Source4:	%{name}.desktop
Patch0:		%{name}-1.6_64bit.patch
Patch1:		%{name}-1.6_array-index.patch
URL:		http://sofia.nmsu.edu/~mleisher/Software/gbdfed/
BuildRequires:	freetype-devel
BuildRequires:	gtk+2-devel >= 2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Gtk-based bitmap font (BDF) editor, descendant of XmBDFed. It can
import PK/GF fonts, HBF fonts (Han Bitmap Font),Linux console fonts
(PSF, CP, FNT), Sun console fonts (vfont), Windows FON/FNT fonts,
TrueType fonts and collections, and X server fonts. It exports PSF
and HEX fonts and allows you to edit two- and four-bits-per-pixel
grayscale fonts.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p0

%build
%configure
%{__make} \
	DEFINES="-DHAVE_FREETYPE -DHAVE_HBF -DG_DISABLE_DEPRECATED -DGDK_PIXBUF_DISABLE_DEPRECATED"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps,%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install -p %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -p %{SOURCE2} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -p %{SOURCE3} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -p %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*x*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*
