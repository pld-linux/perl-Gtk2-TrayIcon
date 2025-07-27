#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pnam	Gtk2-TrayIcon
Summary:	Gtk2::TrayIcon - Perl interface to the EggTrayIcon library
Summary(pl.UTF-8):	Gtk2::TrayIcon - interfejs perlowy do biblioteki EggTrayIcon
Name:		perl-Gtk2-TrayIcon
Version:	0.07
Release:	6
License:	LGPL v2+
Group:		Development/Languages/Perl
Source0:	https://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	c3db5edd7c39ca52625d664b0fb988a5
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	perl-ExtUtils-Depends >= 0.1
BuildRequires:	perl-ExtUtils-PkgConfig >= 0.1
BuildRequires:	perl-Glib-devel >= 1.00
BuildRequires:	perl-Gtk2-devel >= 1.00
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gtk2::TrayIcon module allows a Perl developer to embed an arbitrary
widget in a System Tray like the GNOME notification area.

Note: this module is deprecated and no longer maintained.

%description -l pl.UTF-8
Moduł Gtk2::TrayIcon umożliwia programistom perlowym umieszczanie
dowolnych kontrolek w Zasobniku Systemowym (System Tray), takim jak w
obszarze powiadamiania GNOME.

Uwaga: ten moduł jest przestarzały i nie jest już utrzymywany.

%package devel
Summary:	Development files for Perl Gtk2-TrayIcon bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Gtk2-TrayIcon dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	perl-Cairo-devel
Requires:	perl-Glib-devel >= 1.00
Requires:	perl-Gtk2-devel >= 1.00

%description devel
Development files for Perl Gtk2-TrayIcon bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Gtk2-TrayIcon dla Perla.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{perl_vendorarch}/Gtk2/TrayIcon.pm
%dir %{perl_vendorarch}/Gtk2/TrayIcon
%dir %{perl_vendorarch}/auto/Gtk2/TrayIcon
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/TrayIcon/TrayIcon.so
%{_mandir}/man3/Gtk2::TrayIcon*.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk2/TrayIcon/Install
