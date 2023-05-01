Name:    qt5-qtsystems
Summary: Qt5 Mobility Framework
Version: 5.15
Release: %autorelease

License: GPL-3.0
URL:     https://invent.kde.org/qt/qt/qtsystems
Source0: %{url}/-/archive/%commit/qt5-mobility-%commit.tar.gz
Source1: https://salsa.debian.org/qt-kde-team/qt/qtsystems/-/archive/master/qtsystems-master.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(blkid)
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(QtDeclarative)
BuildRequires: pkgconfig(QtGui) pkgconfig(QtOpenGL)
BuildRequires: pkgconfig(QtNetwork) >= 4.7
BuildRequires: pkgconfig(xv)
BuildRequires: pkgconfig(QtDBus)
BuildRequires: qt5-doctools
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-rpm-macros
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtbase

Provides: %{name}-bearer = %{version}-%{release}
Provides: %{name}-connectivity = %{version}-%{release}
Provides: %{name}-contacts = %{version}-%{release}
Provides: %{name}-feedback = %{version}-%{release}
Provides: %{name}-gallery = %{version}-%{release}
Provides: %{name}-location = %{version}-%{release}
Provides: %{name}-multimediakit = %{version}-%{release}
Provides: %{name}-organizer = %{version}-%{release}
Provides: %{name}-publishsubscribe = %{version}-%{release}
Provides: %{name}-sensors = %{version}-%{release}
Provides: %{name}-serviceframework = %{version}-%{release}
Provides: %{name}-systeminfo = %{version}-%{release}
Provides: %{name}-versit = %{version}-%{release}

%description
Qt5 Mobility Project delivers a set of new APIs to Qt with features that are well
known from the mobile device world, in particular phones. However, these APIs
allow the developer to use these features with ease from one framework and apply
them to phones, netbooks and non-mobile personal computers. The framework not
only improves many aspects of a mobile experience, because it improves the use
of these technologies, but has applicability beyond the mobile device arena.
