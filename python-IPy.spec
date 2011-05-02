%define oname IPy

Summary:        Python module for handling IPv4 and IPv6 Addresses and Networks
Name:           python-%{oname}
Version:        0.75
Release:        %mkrel 1
Epoch:          0
URL:            http://software.inl.fr/trac/trac.cgi/wiki/IPy
Source0:        http://cheeseshop.python.org/packages/source/I/IPy/IPy-%{version}.tar.gz
License:        BSD
Group:          Development/Python
BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

%description
IPy is a Python module for handling IPv4 and IPv6 Addresses and Networks
in a fashion similar to perl's Net::IP and friends. The IP class allows
a comfortable parsing and handling for most notations in use for IPv4
and IPv6 Addresses and Networks.

%prep
%setup -q -n %{oname}-%{version}

%build
CFLAGS="%{optflags}" %{_bindir}/python setup.py build

%install
%{__rm} -rf %{buildroot}
%{_bindir}/python setup.py install --root=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog PKG-INFO README
%{python_sitelib}/%{oname}*


