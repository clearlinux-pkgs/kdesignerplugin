#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kdesignerplugin
Version  : 5.115.0
Release  : 90
URL      : https://download.kde.org/stable/frameworks/5.115/portingAids/kdesignerplugin-5.115.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.115/portingAids/kdesignerplugin-5.115.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.115/portingAids/kdesignerplugin-5.115.0.tar.xz.sig
Summary  : Integration of Frameworks widgets in Qt Designer/Creator
Group    : Development/Tools
License  : LGPL-2.1
Requires: kdesignerplugin-bin = %{version}-%{release}
Requires: kdesignerplugin-data = %{version}-%{release}
Requires: kdesignerplugin-license = %{version}-%{release}
Requires: kdesignerplugin-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : kplotting-dev
BuildRequires : qtbase-dev
BuildRequires : qttools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KDesignerPlugin
Integrating custom widgets with Qt Designer
This tool is deprecated. In your CMake-based build system use [ECMAddQtDesignerPlugin](https://api.kde.org/ecm/module/ECMAddQtDesignerPlugin.html) from "Extra CMake Modules" instead.

%package bin
Summary: bin components for the kdesignerplugin package.
Group: Binaries
Requires: kdesignerplugin-data = %{version}-%{release}
Requires: kdesignerplugin-license = %{version}-%{release}

%description bin
bin components for the kdesignerplugin package.


%package data
Summary: data components for the kdesignerplugin package.
Group: Data

%description data
data components for the kdesignerplugin package.


%package dev
Summary: dev components for the kdesignerplugin package.
Group: Development
Requires: kdesignerplugin-bin = %{version}-%{release}
Requires: kdesignerplugin-data = %{version}-%{release}
Provides: kdesignerplugin-devel = %{version}-%{release}
Requires: kdesignerplugin = %{version}-%{release}

%description dev
dev components for the kdesignerplugin package.


%package license
Summary: license components for the kdesignerplugin package.
Group: Default

%description license
license components for the kdesignerplugin package.


%package man
Summary: man components for the kdesignerplugin package.
Group: Default

%description man
man components for the kdesignerplugin package.


%prep
%setup -q -n kdesignerplugin-5.115.0
cd %{_builddir}/kdesignerplugin-5.115.0

%build
## build_prepend content
# Make sure the package only builds if kdoctools has been updated first
sed -i -r -e 's,(KF.?DocTools \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707750022
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
## build_prepend content
# Make sure the package only builds if kdoctools has been updated first
sed -i -r -e 's,(KF.?DocTools \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-apx
pushd clr-build-apx
## build_prepend content
# Make sure the package only builds if kdoctools has been updated first
sed -i -r -e 's,(KF.?DocTools \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CC=gcc-14
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -mapxf -mavx10.1 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707750022
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdesignerplugin
cp %{_builddir}/kdesignerplugin-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/kdesignerplugin/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v3
pushd clr-build-apx
%make_install_va  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kgendesignerplugin
/usr/bin/kgendesignerplugin

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/as/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/az/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/be/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/br/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/da/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/de/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/el/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/es/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/et/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/he/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/id/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/is/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/it/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/km/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/or/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/se/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/si/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/te/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/th/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kdesignerplugin5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kdesignerplugin5_qt.qm

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/KF5DesignerPlugin/KF5DesignerPluginConfig.cmake
/usr/lib64/cmake/KF5DesignerPlugin/KF5DesignerPluginConfigVersion.cmake
/usr/lib64/cmake/KF5DesignerPlugin/KF5DesignerPluginMacros.cmake
/usr/lib64/cmake/KF5DesignerPlugin/KF5DesignerPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5DesignerPlugin/KF5DesignerPluginTargets.cmake

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdesignerplugin/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kgendesignerplugin.1
/usr/share/man/ca@valencia/man1/kgendesignerplugin.1
/usr/share/man/de/man1/kgendesignerplugin.1
/usr/share/man/es/man1/kgendesignerplugin.1
/usr/share/man/it/man1/kgendesignerplugin.1
/usr/share/man/man1/kgendesignerplugin.1
/usr/share/man/nl/man1/kgendesignerplugin.1
/usr/share/man/pt/man1/kgendesignerplugin.1
/usr/share/man/pt_BR/man1/kgendesignerplugin.1
/usr/share/man/sv/man1/kgendesignerplugin.1
/usr/share/man/uk/man1/kgendesignerplugin.1
