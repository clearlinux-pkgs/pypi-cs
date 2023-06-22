#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-cs
Version  : 3.2.0
Release  : 15
URL      : https://files.pythonhosted.org/packages/68/09/f2ed131a6b154b371ca59c0cce2368be3020ef577980663b739aac90424f/cs-3.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/68/09/f2ed131a6b154b371ca59c0cce2368be3020ef577980663b739aac90424f/cs-3.2.0.tar.gz
Summary  : A simple yet powerful CloudStack API client for Python and the command-line.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-cs-bin = %{version}-%{release}
Requires: pypi-cs-license = %{version}-%{release}
Requires: pypi-cs-python = %{version}-%{release}
Requires: pypi-cs-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
CS
==
.. image:: https://img.shields.io/pypi/l/cs.svg
:alt: License
:target: https://pypi.org/project/cs/

%package bin
Summary: bin components for the pypi-cs package.
Group: Binaries
Requires: pypi-cs-license = %{version}-%{release}

%description bin
bin components for the pypi-cs package.


%package license
Summary: license components for the pypi-cs package.
Group: Default

%description license
license components for the pypi-cs package.


%package python
Summary: python components for the pypi-cs package.
Group: Default
Requires: pypi-cs-python3 = %{version}-%{release}

%description python
python components for the pypi-cs package.


%package python3
Summary: python3 components for the pypi-cs package.
Group: Default
Requires: python3-core
Provides: pypi(cs)
Requires: pypi(pytz)
Requires: pypi(requests)

%description python3
python3 components for the pypi-cs package.


%prep
%setup -q -n cs-3.2.0
cd %{_builddir}/cs-3.2.0
pushd ..
cp -a cs-3.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1687445167
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cs
cp %{_builddir}/cs-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cs/584304f9e6f63d2d9ced518704d939e073a7c890 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cs

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cs/584304f9e6f63d2d9ced518704d939e073a7c890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
