#
# Conditional build:
%bcond_without	apidocs	# do not build and package API docs
%bcond_without	python3	# CPython 3.x module
%bcond_with	rhsm	# Red Had Subscription Management support
%bcond_with	rpm5	# build with rpm5
#
Summary:	Library providing simplified C and Python API to libsolv
Summary(pl.UTF-8):	Biblioteka zapewniająca uproszczone API C i Pythona do libsolv
Name:		libdnf
Version:	0.73.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/rpm-software-management/libdnf/releases
Source0:	https://github.com/rpm-software-management/libdnf/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f1b714f950ac43bce22eb4bcbc1fc575
Patch0:		%{name}-rpm5.patch
URL:		https://github.com/rpm-software-management/libdnf
BuildRequires:	check-devel
BuildRequires:	cmake >= 2.8.5
BuildRequires:	cppunit-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.46.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	json-c-devel
BuildRequires:	libmodulemd-devel >= 2.12.0
BuildRequires:	librepo-devel >= 1.15.0
%{?with_rhsm:BuildRequires:	librhsm-devel >= 0.0.3}
BuildRequires:	libsmartcols-devel
BuildRequires:	libsolv-devel >= 0.7.17
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-modules
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-build >= 4.6
%{!?with_rpm5:BuildRequires:	rpm-devel >= 1:4.15.0}
%{?with_rpm5:BuildRequires:	rpm-devel >= 5}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sphinx-pdg
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	swig
BuildRequires:	swig-python
BuildRequires:	zchunk-devel >= 0.9.11
Requires:	glib2 >= 1:2.46.0
Requires:	librepo >= 1.15.0
Requires:	libsolv >= 0.7.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# PyErr_Format(HyExc_Exception, e.what());
%define		filterout	-Wformat -Werror=format-security

# hawkey(3) man page shared between python-hawkey and python3-hawkey
%define		_duplicate_files_terminate_build	0

%description
Library providing simplified C and Python API to libsolv.

%description -l pl.UTF-8
Biblioteka zapewniająca uproszczone API C i Pythona do libsolv.

%package devel
Summary:	Header files for libdnf library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdnf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.46.0
Requires:	librepo-devel >= 1.15.0
Requires:	libsolv-devel >= 0.7.17
%{!?with_rpm5:Requires:	rpm-devel >= 1:4.15.0}
%{?with_rpm5:Requires:	rpm-devel >= 5}

%description devel
Header files for libdnf library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdnf.

%package apidocs
Summary:	API documentation for libdnf library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libdnf
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libdnf library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libdnf.

%package -n python-hawkey
Summary:	Python 2.x bindings for hawkey library
Summary(pl.UTF-8):	Wiązania Pythona 2.x do biblioteki hawkey
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-hawkey
Python 2.x bindings for hawkey library.

%description -n python-hawkey -l pl.UTF-8
Wiązania Pythona 2.x do biblioteki hawkey.

%package -n python-hawkey-test
Summary:	Test module for hawkey library
Summary(pl.UTF-8):	Moduł testowy dla biblioteki hawkey
Group:		Development/Libraries
Requires:	python-hawkey = %{version}-%{release}

%description -n python-hawkey-test
Test module for hawkey library.

%description -n python-hawkey-test -l pl.UTF-8
Moduł testowy dla biblioteki hawkey.

%package -n python3-hawkey
Summary:	Python 3.x bindings for hawkey library
Summary(pl.UTF-8):	Wiązania Pythona 3.x do biblioteki hawkey
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-hawkey
Python 3.x bindings for hawkey library.

%description -n python3-hawkey -l pl.UTF-8
Wiązania Pythona 3.x do biblioteki hawkey.

%package -n python3-hawkey-test
Summary:	Test module for hawkey library
Summary(pl.UTF-8):	Moduł testowy dla biblioteki hawkey
Group:		Development/Libraries
Requires:	python3-hawkey = %{version}-%{release}

%description -n python3-hawkey-test
Test module for hawkey library.

%description -n python3-hawkey-test -l pl.UTF-8
Moduł testowy dla biblioteki hawkey.

%package -n python-hawkey-apidocs
Summary:	API documentation for Python hawkey module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona hawkey
Group:		Documentation
Obsoletes:	hawkey-apidocs < 0.6.4-2
BuildArch:	noarch

%description -n python-hawkey-apidocs
API documentation for Python hawkey module.

%description -n python-hawkey-apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona hawkey.

%package -n python-libdnf
Summary:	Python 2.x bindings for libdnf library
Summary(pl.UTF-8):	Wiązania Pythona 2.x do biblioteki libdnf
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-libdnf
Python 2.x bindings for hawkey libdnf.

%description -n python-libdnf -l pl.UTF-8
Wiązania Pythona 2.x do biblioteki libdnf.

%package -n python3-libdnf
Summary:	Python 3.x bindings for libdnf library
Summary(pl.UTF-8):	Wiązania Pythona 3.x do biblioteki libdnf
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-libdnf
Python 3.x bindings for hawkey library.

%description -n python3-libdnf -l pl.UTF-8
Wiązania Pythona 3.x do biblioteki libdnf.

%prep
%setup -q
%{?with_rpm5:%patch0 -p1}

%build
export CFLAGS="%{rpmcflags} -D_GNU_SOURCE}"
install -d build %{?with_python3:build-py3}
cd build
%cmake .. \
	%{?with_rhsm:-DENABLE_RHSM_SUPPORT=ON} \
	-DPYTHON_DESIRED=2

%{__make}
%{__make} doc-html

%if %{with python3}
cd ../build-py3
%cmake .. \
	%{?with_rhsm:-DENABLE_RHSM_SUPPORT=ON} \
	-DPYTHON_DESIRED=3

%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%{__make} -C build-py3 install \
	DESTDIR=$RPM_BUILD_ROOT

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}/hawkey
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}/hawkey

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}/libdnf
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}/libdnf
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/hawkey
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/hawkey

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/libdnf
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/libdnf
%py_postclean

install -d $RPM_BUILD_ROOT%{_gtkdocdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/* $RPM_BUILD_ROOT%{_gtkdocdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README.md docs/release_notes.rst
%attr(755,root,root) %{_libdir}/libdnf.so.2
%dir %{_libdir}/libdnf
%dir %{_libdir}/libdnf/plugins

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdnf.so
%{_includedir}/libdnf
%{_pkgconfigdir}/libdnf.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libdnf
%endif

%files -n python-hawkey
%defattr(644,root,root,755)
%dir %{py_sitedir}/hawkey
%attr(755,root,root) %{py_sitedir}/hawkey/_hawkeymodule.so
%{py_sitedir}/hawkey/__init__.py[co]
%{_mandir}/man3/hawkey.3*

%files -n python-hawkey-test
%defattr(644,root,root,755)
%dir %{py_sitedir}/hawkey/test
%{py_sitedir}/hawkey/test/*.py[co]
%attr(755,root,root) %{py_sitedir}/hawkey/test/_hawkey_testmodule.so

%if %{with python3}
%files -n python3-hawkey
%defattr(644,root,root,755)
%dir %{py3_sitedir}/hawkey
%attr(755,root,root) %{py3_sitedir}/hawkey/_hawkey.so
%{py3_sitedir}/hawkey/*.py
%{py3_sitedir}/hawkey/__pycache__
%{_mandir}/man3/hawkey.3*

%files -n python3-hawkey-test
%defattr(644,root,root,755)
%dir %{py3_sitedir}/hawkey/test
%{py3_sitedir}/hawkey/test/*.py
%{py3_sitedir}/hawkey/test/__pycache__
%attr(755,root,root) %{py3_sitedir}/hawkey/test/_hawkey_test.so
%endif

%files -n python-hawkey-apidocs
%defattr(644,root,root,755)
%doc build/docs/hawkey/html/{_static,*.html,*.js}

%files -n python-libdnf
%defattr(644,root,root,755)
%dir %{py_sitedir}/libdnf
%{py_sitedir}/libdnf/*.py[co]
%attr(755,root,root) %{py_sitedir}/libdnf/*.so
%{py_sitedir}/libdnf-%{version}.dist-info

%files -n python3-libdnf
%defattr(644,root,root,755)
%dir %{py3_sitedir}/libdnf
%{py3_sitedir}/libdnf/*.py
%{py3_sitedir}/libdnf/__pycache__
%attr(755,root,root) %{py3_sitedir}/libdnf/*.so
%{py3_sitedir}/libdnf-%{version}.dist-info
