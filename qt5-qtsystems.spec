%define commit e3332ee38d27a134cef6621fdaf36687af1b6f4a
%define git 20181230

%define devname %mklibname -d %{name}

Name:    qt5-qtsystems
Summary: Qt5 Mobility Framework
Version: 5.4.0
Release: 0.%{git}.1

License: GPL-3.0
URL:     https://invent.kde.org/qt/qt/qtsystems
Source0: https://github.com/qtproject/qtsystems/archive/qtsystems-%{commit}.tar.gz

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

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}

%description -n %{devname}
Development files for %{name}

%package examples
Summary:	Code examples showing the use of %{name}
Group:		Documentation
Requires:	%{devname} = %{EVRD}

%description examples
Code examples showing the use of %{name}

%prep
%autosetup -n qtsystems-%{commit}
%{_libdir}/qt5/bin/syncqt.pl -version %{version}
%qmake_qt5 PREFIX=%{_prefix}

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_libdir}/lib*.so*
%{_libdir}/qt5/qml/*
%{_libdir}/qt5/bin/*

%files -n %{devname}
%{_libdir}/lib*.prl
%{_includedir}/qt5/*
%{_libdir}/qt5/mkspecs/*
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/*

%files examples
%{_libdir}/qt5/examples
