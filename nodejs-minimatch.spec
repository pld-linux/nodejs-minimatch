%define		pkg	minimatch
Summary:	JavaScript glob matcher
Name:		nodejs-%{pkg}
Version:	0.2.8
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/minimatch
Source0:	http://registry.npmjs.org/minimatch/-/minimatch-%{version}.tgz
# Source0-md5:	aab77712c6130f66c6a39c16bc9f4993
# fix deps to newer version in RPMs
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-lru-cache >= 2.0.0, nodejs-lru-cache < 2.1.0
Requires:	nodejs-sigmund >= 1.0.0, nodejs-sigmund < 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts glob expressions to JavaScript "RegExp" objects.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}
cp -p %{pkg}.js $RPM_BUILD_ROOT%{nodejs_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%doc test/
%{nodejs_libdir}/%{pkg}.js
