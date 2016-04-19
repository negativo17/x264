%global commit0 5c6570495f8f1c716b294aee1430d8766a4beb9c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global api_version 148


Name:           x264
Version:        0.%{api_version}
Release:        3.%{?shortcommit0}%{?dist}
Epoch:          1
Summary:        H264/AVC video streams encoder
License:        GPLv2+
URL:            http://www.videolan.org/developers/x264.html

# No releases, not GitHub, no versioning except internal API version
Source0:        %{name}-%{version}-%{shortcommit0}.tar.xz
Source1:        %{name}-snapshot.sh

BuildRequires:  gpac-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  yasm

%description
%{name} is a free software library and application for encoding video streams into
the H.264/MPEG-4 AVC compression format. This package contains the command line
encoder.

%package libs
Summary:        Library for encoding H264/AVC video streams

%description libs
%{name} is a free software library and application for encoding video streams into
the H.264/MPEG-4 AVC compression format. This package contains the shared
libraries.

%package devel
Summary:        Development files for the x264 library
Requires:       %{name}-libs%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%setup -qn %{name}


%build
%configure \
    --enable-debug \
    --enable-pic \
    --enable-shared \
    --bit-depth=10
sed -i -e "s/SONAME=libx264.*/SONAME=libx264_main10.so/g" config.mak
make %{?_smp_mflags}

%configure \
    --enable-debug \
    --enable-pic \
    --enable-shared \
    --bit-depth=8
make %{?_smp_mflags}

%install
%make_install
install -p -m 755 libx264_main10.so %{buildroot}%{_libdir}/

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/%{name}

%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS
%{_libdir}/lib%{name}.so.*
# Loaded at runtime, unversioned
%{_libdir}/lib%{name}_main10.so

%files devel
%doc doc/*
%{_includedir}/%{name}.h
%{_includedir}/%{name}_config.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sun Feb 07 2016 Simone Caronni <negativo17@gmail.com> - 1:0.148-3.5c65704
- Enable platform-specific assembly optimizations.

* Thu Feb 04 2016 Simone Caronni <negativo17@gmail.com> - 0.148-2.5c65704
- Update to latest stable snapshot.
- Use a different name for the 10 bit library for consistency with x265.
- Bump Epoch.

* Mon Nov 23 2015 Simone Caronni <negativo17@gmail.com> - 0.148-1.7599210
- First build from master branch.
