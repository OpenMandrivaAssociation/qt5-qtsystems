%define commit e3332ee38d27a134cef6621fdaf36687af1b6f4a
%define git 20181230

Name:    qt5-qtsystems
Summary: Qt5 Mobility Framework
Version: 5.15.%{git}
Release: 1

License: GPL-3.0
URL:     https://invent.kde.org/qt/qt/qtsystems
Source0: https://github.com/qtproject/qtsystems/archive/%{commit}.tar.gz

BuildRequires: qmake5
BuildRequires: make
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(blkid)
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libudev)
BuildRequires: qt5-qtbase-devel

%description
Qt5 Mobility Project delivers a set of new APIs to Qt with features that are well
known from the mobile device world, in particular phones. However, these APIs
allow the developer to use these features with ease from one framework and apply
them to phones, netbooks and non-mobile personal computers. The framework not
only improves many aspects of a mobile experience, because it improves the use
of these technologies, but has applicability beyond the mobile device arena.

%prep
%autosetup -n qtsystems-%{commit}

%build
%qmake_qt5 PREFIX=/usr
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_ROOT=%{buildroot}

%files
