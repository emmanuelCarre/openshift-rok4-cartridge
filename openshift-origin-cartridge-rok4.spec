%global cartridgedir %{_libexecdir}/openshift/cartridges/rok4

Name:		openshift-origin-cartridge-rok4	
Version:	1.0.9
Release:	1%{?dist}
Summary:	Embedded rok4 support for OpenShift

Group:		Network/Daemons
License:	CeCILL
URL:		http://www.openshift.com
Source0:	http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz

Requires:       rok4
Requires:       rubygem(openshift-origin-node)
Requires:       openshift-origin-node-util

BuildArch:      noarch

%description
Provides rok4 cartridge support to OpenShift

%prep
%setup -q

%build
%__rm %{name}.spec
%__rm -rf rel-eng

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/conf/
%attr(0755,-,-) %{cartridgedir}/lib/
%attr(0755,-,-) %{cartridgedir}/metadata/
%attr(0755,-,-) %{cartridgedir}/template/
%attr(0755,-,-) %{cartridgedir}/usrrok4/
%doc %{cartridgedir}/README.md

%changelog
* Tue May 26 2015 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.9-1
- new package built with tito

* Thu May 21 2015 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.8-1
- new package built with tito

* Thu May 21 2015 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.7-1
- new package built with tito

* Thu May 21 2015 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.6-1
- new package built with tito

* Thu May 21 2015 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.4-1
- Update bin path rok4 (nicolas.messin@worldline.com)

* Wed Sep 10 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.4-1
- Update conf/server.conf.erb path rok4 (nicolas.messin@worldline.com)

* Wed Sep 10 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.3-1
- Up server.conf.erb path with /rok4 

* Wed Sep 10 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.2-1
- new package built with tito

* Mon Sep 08 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.1-1
- new package built with tito

* Mon Sep 08 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.O
- Creation of initial rok4 cartridge
