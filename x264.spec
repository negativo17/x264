%global commit0 34c06d1c17ad968fbdda153cb772f77ee31b3095
%global date 20190717
%global api_version 157
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%bcond_with bootstrap

Name:           x264
Version:        0.%{api_version}
Release:        19%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Epoch:          1
Summary:        H264/AVC video streams encoder
License:        GPLv2+
URL:            http://www.videolan.org/developers/x264.html

# No releases, not GitHub, no versioning except internal API version
Source0:        %{name}-%{version}-%{shortcommit0}.tar.xz
Source1:        %{name}-snapshot.sh

BuildRequires:  gcc
%if %{without bootstrap}
BuildRequires:  gpac-devel
BuildRequires:  ffmpeg-devel
%endif
BuildRequires:  nasm >= 2.13

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
%autosetup -p1 -n %{name}
sed -i -e 's/gpac_static/gpac/g' configure

%build
%configure \
    --enable-debug \
    --enable-pic \
    --enable-shared \
    --bit-depth=10 \
    --system-libx264
sed -i -e "s/SONAME=libx264.*/SONAME=libx264_main10.so/g" config.mak
make %{?_smp_mflags}

%configure \
    --enable-debug \
    --enable-pic \
    --enable-shared \
    --bit-depth=8 \
    --system-libx264
make %{?_smp_mflags}

%install
%make_install
install -p -m 755 libx264_main10.so %{buildroot}%{_libdir}/

%ldconfig_scriptlets libs

%files
%{_bindir}/%{name}

%files libs
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
* Wed Sep 04 2019 Simone Caronni <negativo17@gmail.com> - 1:0.157-19.20190717git34c06d1
- Update to latest stable snapshot.

* Thu May 23 2019 Simone Caronni <negativo17@gmail.com> - 1:0.157-18.20190303git72db437
- Update to latest stable snapshot.
- Update SPEC file, use bootstrap packaging guidelines.

* Tue Feb 26 2019 Simone Caronni <negativo17@gmail.com> - 1:0.155-17.20180806git0a84d98
- Rebuild for updated libraries.

* Mon Nov 12 2018 Simone Caronni <negativo17@gmail.com> - 1:0.155-16.20180806git0a84d98
- Rebuild for FFMpeg update.

* Wed Aug 22 2018 Simone Caronni <negativo17@gmail.com> - 1:0.155-15.20180806git0a84d98
- Update to latest stable snapshot.

* Thu Apr 26 2018 Simone Caronni <negativo17@gmail.com> - 1:0.152-14.20171224gite9a5903
- Rebuild for FFMpeg update.

* Sat Jan 06 2018 Simone Caronni <negativo17@gmail.com> - 1:0.152-13.20171224gite9a5903
- Update to latest stable snapshot.

* Sun Sep 10 2017 Simone Caronni <negativo17@gmail.com> - 1:0.148-12.20170521gitaaa9aa8
- Update to latest stable snapshot.

* Wed May 24 2017 Simone Caronni <negativo17@gmail.com> - 1:0.148-11.20170519gitd32d7bf
- Update to latest stable snapshot.

* Sun Feb 12 2017 Simone Caronni <negativo17@gmail.com> - 1:0.148-10.20170121git97eaef2
- Update to latest stable snapshot.

* Wed Nov 09 2016 Simone Caronni <negativo17@gmail.com> - 1:0.148-9.20160920git86b7198
- Rebuild for FFmpeg update.

* Sat Oct 08 2016 Simone Caronni <negativo17@gmail.com> - 1:0.148-8.20160920git86b7198
- Update to latest snapshot.
- Update snapshot script.
- Use packaging guidelines for snapshot format.

* Fri Jul 22 2016 Simone Caronni <negativo17@gmail.com> - 1:0.148-7.a5e06b9
- Rebuild for ffmpeg 3.1.1.

* Fri Jul 01 2016 Simone Caronni <negativo17@gmail.com> - 1:0.148-6.a5e06b9
- Use dynamic gpac library.

* Fri Jul 01 2016 Simone Caronni <negativo17@gmail.com> - 1:0.148-5.a5e06b9
- Update sources.
- Remove upstreamed patch.

* Fri Apr 22 2016 Simone Caronni <negativo17@gmail.com> - 1:0.148-4.fd2c324
- Update to latest sources.
- Allow building without CLI (--without=cli).

* Sun Feb 07 2016 Simone Caronni <negativo17@gmail.com> - 1:0.148-3.5c65704
- Enable platform-specific assembly optimizations.

* Thu Feb 04 2016 Simone Caronni <negativo17@gmail.com> - 0.148-2.5c65704
- Update to latest stable snapshot.
- Use a different name for the 10 bit library for consistency with x265.
- Bump Epoch.

* Mon Nov 23 2015 Simone Caronni <negativo17@gmail.com> - 0.148-1.7599210
- First build from master branch.
