#
%include        /usr/lib/rpm/macros.perl
%define pnam    Gtk2-TrayIcon
Name:	perl-%{pnam}
Summary:	GNOME TrayIcon library
Version:	0.03
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	4c627fd00cc316ac018732e7739a5c4f
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	perl-Gtk2 >= 1.00
BuildRequires:	perl-Glib >= 1.00
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME TrayIcon library

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk2/TrayIcon.pm
%dir %{perl_vendorarch}/Gtk2/TrayIcon
%dir %{perl_vendorarch}/auto/Gtk2/TrayIcon
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/TrayIcon/*.so
%{perl_vendorarch}/Gtk2/TrayIcon/Install
%{perl_vendorarch}/auto/Gtk2/TrayIcon/*.bs
%{_mandir}/man3/*
