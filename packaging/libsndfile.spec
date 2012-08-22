Name:       libsndfile
Summary:    Library for reading and writing sound files
Version: 1.0.21
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.mega-nerd.com/libsndfile/
Source0:    http://www.mega-nerd.com/libsndfile/libsndfile-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(alsa)
#BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)


%description
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface. It can
currently read/write 8, 16, 24 and 32-bit PCM files as well as 32 and
64-bit floating point WAV files and a number of compressed formats. It
compiles and runs on *nix, MacOS, and Win32.



%package devel
Summary:    Development files for libsndfile
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface.
This package contains files needed to develop with libsndfile.



%prep
%setup -q -n %{name}-%{version}


%build

%configure --disable-static \
    --disable-dependency-tracking

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%docs_package


%files
%defattr(-,root,root,-)
%doc COPYING 
%{_bindir}/*
%{_libdir}/%{name}.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/sndfile.h
%{_includedir}/sndfile.hh
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/sndfile.pc
/usr/share/doc/libsndfile1-dev

