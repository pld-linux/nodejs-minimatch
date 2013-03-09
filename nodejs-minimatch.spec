%define		pkg	minimatch
Summary:	JavaScript glob matcher
Name:		nodejs-%{pkg}
Version:	0.2.11
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/minimatch
Source0:	http://registry.npmjs.org/minimatch/-/minimatch-%{version}.tgz
# Source0-md5:	0891b8addfc6930824331eec9e8e0aa5
# fix deps to newer version in RPMs
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-lru-cache >= 2
Requires:	nodejs-lru-cache < 3
Requires:	nodejs-sigmund >= 1.0.0
Requires:	nodejs-sigmund < 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts glob expressions to JavaScript "RegExp" objects.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -p %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%doc test/
%{nodejs_libdir}/%{pkg}
