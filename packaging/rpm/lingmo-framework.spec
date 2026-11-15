Name:           lingmo-framework
Version:        5.0.4
Release:        1.lingmo5u1%{?dist}
Summary:        Lingmo desktop framework clients
License:        GPL-3.0-or-later
URL:            https://github.com/LingmoOS/lingmo-framework
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  lingmo-sdk-devel >= 5.0.5
BuildRequires:  pkgconfig(icu-uc) pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libsystemd) pkgconfig(libpipewire-0.3) pkgconfig(libspa-0.2)

%description
Shared Lingmo desktop framework clients for Bluetooth, audio, networking,
power, files and system services.

%package devel
Summary:        Development files for the Lingmo framework
Requires:       %{name} = %{version}-%{release}
Requires:       lingmo-sdk-devel >= 5.0.5

%description devel
Headers, CMake metadata and link libraries for applications using the Lingmo
framework clients.

%prep
%autosetup -p1

%build
%cmake -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/liblingmo-*.so.*

%files devel
%{_includedir}/lingmo/
%{_libdir}/liblingmo-*.so
%{_libdir}/cmake/LingmoFramework/

%changelog
* Mon Nov 16 2026 Lingmo OS Team <team@lingmo.org> - 5.0.4-1.lingmo5u1
- Add the initial RPM packages for framework runtime and development files.
