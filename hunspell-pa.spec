Name: hunspell-pa
Summary: Punjabi hunspell dictionaries
Version: 20050726
Release: 4.1%{?dist}
Source: http://hunspell.sourceforge.net/pa-demo.tar.gz
Group: Applications/Text
URL: http://hunspell.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Punjabi hunspell dictionaries.

%prep
%setup -q -c -n pa-demo
iconv -f ISO-8859-1 -t UTF-8 pa/Copyright > pa/Copyright.utf8
mv pa/Copyright.utf8 pa/Copyright

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
mv pa/pa.dic pa/pa_IN.dic
mv pa/pa.aff pa/pa_IN.aff
cp -p pa/*.dic pa/*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc pa/README pa/COPYING pa/Copyright
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 20050726-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050726-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 06 2008 Parag <pnemade@redhat.com> - 20050726-2
- Added Copyright

* Thu Jan 03 2008 Parag <pnemade@redhat.com> - 20050726-1
- Initial Fedora release
