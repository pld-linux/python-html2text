%define		module	html2text
Summary:	A HTML to markdown-structured text converter
Name:		python-%{module}
Version:	2019.8.11
Release:	1
License:	GPL v3
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/h/html2text/%{module}-%{version}.tar.gz
# Source0-md5:	21aad7ec95b70606024b783c8253899c
URL:		https://github.com/Alir3z4/html2text/
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildArch:	noarch
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
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/html2text
%{py_sitescriptdir}/html2text/*.py[co]
%{py_sitescriptdir}/html2text-*.egg-info
