%global commit0 da14df5535fd46776fb1c9da3130973295c87aca
%global date 20241027
%global api_version 164
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%bcond_with bootstrap

Name:           x264
Version:        0.%{api_version}
Release:        36%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Epoch:          1
Summary:        H264/AVC video streams encoder
License:        GPLv2+
URL:            https://www.videolan.org/developers/x264.html

# No releases, not GitHub, no versioning except internal API version
Source0:        %{name}-%{version}-%{shortcommit0}.tar.xz
Source1:        %{name}-snapshot.sh

BuildRequires:  gcc
BuildRequires:  nasm >= 2.13
BuildRequires:  pkgconfig(bash-completion)
%if %{without bootstrap}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
%endif

Requires:       bash-completion

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
    --enable-bashcompletion \
    --enable-debug \
    --enable-pic \
    --enable-shared \
    --bit-depth=all \
    --system-libx264

%make_build

%install
%make_install

%ldconfig_scriptlets libs

%files
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}

%files libs
%license COPYING
%doc AUTHORS
%{_libdir}/lib%{name}.so.*

%files devel
%doc doc/*
%{_includedir}/%{name}.h
%{_includedir}/%{name}_config.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Oct 29 2024 Simone Caronni <negativo17@gmail.com> - 1:0.164-36.20241027gitda14df5
- Update to latest snapshot.

* Wed Sep 25 2024 Simone Caronni <negativo17@gmail.com> - 1:0.164-35.20240917gitc24e06c
- Update to latest snapshot.

* Thu May 23 2024 Simone Caronni <negativo17@gmail.com> - 1:0.164-34.20240513git4613ac3
- Adjust bash-completion installation and URL (#1).

* Wed May 22 2024 Simone Caronni <negativo17@gmail.com> - 1:0.164-33.20240513git4613ac3
- Update to latest snapshot.
- Switch to unified build with multiple bit depths.
- Trim changelog.
- Move bash completion file to /usr/share/bash-completion/completions.

* Wed Mar 20 2024 Simone Caronni <negativo17@gmail.com> - 1:0.164-32.20240314git585e019
- Update to latest snapshot.

* Wed Jan 10 2024 Simone Caronni <negativo17@gmail.com> - 1:0.164-31.20231123gitc1c9931
- Update to latest snapshot.

* Fri Sep 29 2023 Simone Caronni <negativo17@gmail.com> - 1:0.164-30.20230402gita8b68eb
- Update to latest snapshot.

* Tue Mar 07 2023 Simone Caronni <negativo17@gmail.com> - 1:0.164-29.20230128giteaa68fa
- Update to latest snapshot.

* Fri Sep 16 2022 Simone Caronni <negativo17@gmail.com> - 1:0.164-28.20220905git7628a56
- Update to latest snapshot.

* Wed Apr 06 2022 Simone Caronni <negativo17@gmail.com> - 1:0.164-27.20220222gitbfc87b7
- Rebuild for updated dependencies.

* Thu Mar 31 2022 Simone Caronni <negativo17@gmail.com> - 1:0.164-26.20220222gitbfc87b7
- Update to latest snapshot.
- Enable bash completion for cli.
- Fix dependencies for split ffmpeg package.
