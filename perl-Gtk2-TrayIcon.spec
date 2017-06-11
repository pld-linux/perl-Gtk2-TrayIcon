#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Gtk2-TrayIcon
Summary:	Gtk2::TrayIcon - Perl interface to the EggTrayIcon library
Summary(pl.UTF-8):	Gtk2::TrayIcon - interfejs perlowy do biblioteki EggTrayIcon
Name:		perl-Gtk2-TrayIcon
Version:	0.06
Release:	12
License:	LGPL v2+
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	522c328f14681a25d76eeaf317e05049
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	perl-Glib >= 1.00
BuildRequires:	perl-Gtk2 >= 1.00
BuildRequires:	perl-ExtUtils-Depends >= 0.1
BuildRequires:	perl-ExtUtils-PkgConfig >= 0.1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gtk2::TrayIcon module allows a Perl developer to embed an arbitrary
widget in a System Tray like the GNOME notification area.

%description -l pl.UTF-8
Moduł Gtk2::TrayIcon umożliwia programistom perlowym umieszczanie
dowolnych kontrolek w Zasobniku Systemowym (System Tray), takim jak w
obszarze powiadamiania GNOME.

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
%{perl_vendorarch}/Gtk2/TrayIcon/Install
%dir %{perl_vendorarch}/auto/Gtk2/TrayIcon
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/TrayIcon/*.so
%{_mandir}/man3/Gtk2::TrayIcon*.3pm*
