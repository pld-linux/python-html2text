#
# Conditional build:
%bcond_without	python2		# Python 2 package
%bcond_without	python3		# Python 3 package

%define		module	html2text
Summary:	A HTML to markdown-structured text converter
Name:		python-%{module}
Version:	2014.12.5
Release:	1
License:	GPL v3
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/h/html2text/%{module}-%{version}.tar.gz
# Source0-md5:	165c314c5957cc8cf847c9a8cac3e4d2
URL:		https://github.com/Alir3z4/html2text/
%if %{with python2}
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-Cython
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A HTML to markdown-structured text converter.

%package -n python3-%{module}
Summary:	A HTML to markdown-structured text converter
Group:		Libraries/Python

%description -n python3-%{module}
A HTML to markdown-structured text converter.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%{__python} setup.py build
%endif
%if %{with python3}
%{__python3} setup.py build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/html2text
%{py_sitescriptdir}/html2text/*.py[co]
%{py_sitescriptdir}/html2text-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/html2text
%{py3_sitescriptdir}/html2text/*.py
%{py3_sitescriptdir}/html2text/__pycache__
%{py3_sitescriptdir}/html2text-*.egg-info
%endif
