Summary:	A customizable and lightweight notification-daemon
Name:		dunst
Version:	1.0.0
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://www.knopwob.org/public/dunst-release/%{name}-%{version}.tar.bz2
# Source0-md5:	bb5fee3cdf6ee30f7e11b7edd35e6723
Patch0:		%{name}-libs.patch
BuildRequires:	cairo-devel
BuildRequires:	glib-devel
BuildRequires:	libnotify-devel
BuildRequires:	libxdg-basedir-devel
BuildRequires:	pango-devel
BuildRequires:	perl-tools-pod
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXScrnSaver-devel
BuildRequires:	xorg-libXScrnSaver-devel
Requires:	dbus
Provides:	xdg-desktop-notification-daemon
Obsoletes:	xdg-desktop-notification-daemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dunst is a lightweight replacement for the notification-daemons
provided by most desktop environments. It's very customizable, doesn't
depend on any toolkits and therefore fits in those windowmanager
centric setups we all love to customize to perfection.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}"			\
	EXTRACFLAGS="%{rpmcflags}"	\
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG LICENSE RELEASE_NOTES.*
%attr(755,root,root) %{_bindir}/dunst
%{_datadir}/dbus-1/services/org.knopwob.dunst.service
%{_datadir}/%{name}
%{_mandir}/man1/dunst.1*

