%define oname IPy
Summary:        Python module for handling IPv4 and IPv6 Addresses and Networks
Name:           python-%{oname}
Version:        0.81
Release:        24%{?dist}
URL:            https://github.com/haypo/python-ipy
Source0:        https://files.pythonhosted.org/packages/source/I/IPy/IPy-%{version}.tar.gz
License:        BSD
BuildRequires:  python2-devel python3-devel
BuildArch:      noarch
Provides:	python3-%{oname} = %{EVRD}

%description
IPy is a Python module for handling IPv4 and IPv6 Addresses and Networks 
in a fashion similar to perl's Net::IP and friends. The IP class allows 
a comfortable parsing and handling for most notations in use for IPv4 
and IPv6 Addresses and Networks.

%package -n python2-%{oname}
Summary: Python 2 module for handling IPv4 and IPv6 Addresses and Networks

%description -n python2-%{oname}
IPy is a Python 2 module for handling IPv4 and IPv6 Addresses and Networks 
in a fashion similar to perl's Net::IP and friends. The IP class allows 
a comfortable parsing and handling for most notations in use for IPv4 
and IPv6 Addresses and Networks.

%prep
%setup -q -n %{oname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{oname}
%license COPYING
%doc AUTHORS ChangeLog README
%{python2_sitelib}/%{oname}*

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{python3_sitelib}/%{oname}*
%{python3_sitelib}/__pycache__/%{oname}*
