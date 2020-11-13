%global xdg_desktop_portal_version 1.6.0

Name:           xdg-desktop-portal-gtk
Version:        1.8.0
Release:        1
Summary:        Backend implementation for xdg-desktop-portal using GTK+
Group:          Graphical desktop/GNOME
License:        LGPLv2+
URL:            https://github.com/flatpak/%{name}
Source0:        https://github.com/flatpak/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  systemd-macros
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(xdg-desktop-portal) >= %{xdg_desktop_portal_version}
Requires:       dbus
Requires:       xdg-desktop-portal >= %{xdg_desktop_portal_version}

%{?systemd_requires}
# Use rich deps to pull in this package when flatpak and gtk3 are both installed
Supplements:    (flatpak and gtk+3.0)

%description
A backend implementation for xdg-desktop-portal that is using GTK+ and various
pieces of GNOME infrastructure, such as the org.gnome.Shell.Screenshot or
org.gnome.SessionManager D-Bus interfaces.

%prep
%autosetup -p1

%build
%configure --disable-silent-rules --with-systemduserunitdir=%{_userunitdir}
%make_build

%install
%make_install
%find_lang %{name}

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.gtk.service
%{_datadir}/xdg-desktop-portal/portals/gtk.portal
%{_userunitdir}/%{name}.service
