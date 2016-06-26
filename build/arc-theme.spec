%global git 3095952c1eb6

Name:		arc-theme
# Version from $(date +%s)
Version:	20160605
Release:	1.git%{git}%{?dist}
Summary:	Arc is a theme for GTK 3, GTK 2 and GNOMEShell
Group:		User Interface/Desktops
Epoch:		1

License:	GPLv3
URL:		https://github.com/horst3180/Arc-theme

Source0:	%{name}-%{version}.tar.gz

BuildRequires: autoconf automake gtk3-devel

%if 0%{?suse_version}
Requires:	gtk2-engine-murrine
Requires:	gtk2-theming-engine-adwaita
%else
Requires:	gtk-murrine-engine
Requires:	gnome-themes-standard
%endif

BuildArch:	noarch

%description
Arc is a flat theme with transparent elements for GTK 3, GTK 2 and Gnome-Shell. It supports GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Pantheon, etc.

%prep
%setup -q

%build
./autogen.sh --with-gnome=3.20 --disable-unity --prefix=/usr

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc
%{_datadir}/themes/Arc
%{_datadir}/themes/Arc-Darker
%{_datadir}/themes/Arc-Dark

%changelog
* Sun Jun 26 2016 Chris Smart <csmart@kororaproject.org> 20160605-1.git3095952c1eb6
- Build latest version from tag.

* Thu May 12 2016 Chris Smart <csmart@kororaproject.org> 1463048461-1.git5ec25f42e639
- Convert upstream spec file for use with kp build system
- Build package for Korora 24

