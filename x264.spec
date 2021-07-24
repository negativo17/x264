%global commit0 5db6aa6cab1b146e07b60cc1736a01f21da01154
%global date 20210613
%global api_version 163
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%bcond_with bootstrap

Name:           x264
Version:        0.%{api_version}
Release:        25%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Epoch:          1
Summary:        H264/AVC video streams encoder
License:        GPLv2+
URL:            http://www.videolan.org/developers/x264.html

# No releases, not GitHub, no versioning except internal API version
Source0:        %{name}-%{version}-%{shortcommit0}.tar.xz
Source1:        %{name}-snapshot.sh

BuildRequires:  gcc
%if %{without bootstrap}
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
* Sat Jul 24 2021 Simone Caronni <negativo17@gmail.com> - 1:0.163-25.20210613git5db6aa6
- Update to latest stable snapshot.

* Mon Mar 01 2021 Simone Caronni <negativo17@gmail.com> - 1:0.161-24.20210124git544c61f
- Update to latest stable snapshot.

* Thu Dec 03 2020 Simone Caronni <negativo17@gmail.com> - 1:0.161-23.20200912gitd198931
- Update to latest stable snapshot.

* Mon Jul 13 2020 Simone Caronni <negativo17@gmail.com> - 1:0.160-22.20200702gitcde9a93
- Update to latest stable snapshot.

* Fri May 15 2020 Simone Caronni <negativo17@gmail.com> - 1:0.159-21.20200409git296494a
- Update to latest stable snapshot.

* Fri Jan 17 2020 Simone Caronni <negativo17@gmail.com> - 1:0.159-20.20191127git1771b55
- Update to latest stable snapshot.

* Wed Sep 04 2019 Simone Caronni <negativo17@gmail.com> - 1:0.157-19.20190717git34c06d1
- Update to latest stable snapshot.
- Disable GPAC.
- Trim changelog.

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
