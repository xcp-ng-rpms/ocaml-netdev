%global debug_package %{nil}

Name:           ocaml-netdev
Version:        1.3.0
Release:        1%{?dist}
Summary:        Manipulate Linux bridges, network devices and openvswitch instances in OCaml
License:        LGPL
URL:            https://github.com/xapi-project/netdev

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/netdev/archive?at=v1.3.0&format=tar.gz&prefix=ocaml-netdev-1.3.0#/netdev-1.3.0.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/netdev/archive?at=v1.3.0&format=tar.gz&prefix=ocaml-netdev-1.3.0#/netdev-1.3.0.tar.gz) = 6a046c9d5e996a56798c2d0b912220a1ba1e617c

BuildRequires:  xs-opam-repo
BuildRequires:  forkexecd-devel

%global _use_internal_dependency_generator 0
%global __requires_exclude *caml*

%description
Manipulate Linux bridges, network devices and openvswitch instances in OCaml.

%package        devel
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/netdev/archive?at=v1.3.0&format=tar.gz&prefix=ocaml-netdev-1.3.0#/netdev-1.3.0.tar.gz) = 6a046c9d5e996a56798c2d0b912220a1ba1e617c
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       forkexecd-devel%{?_isa}
Requires:       xs-opam-repo

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%global ocaml_dir /usr/lib/opamroot/ocaml-system
%global ocaml_libdir %{ocaml_dir}/lib
%global ocaml_docdir %{ocaml_dir}/doc

%prep
%autosetup -p1

%build
make

%install
make DESTDIR=%{buildroot} install

%files
%doc ChangeLog
%doc LICENSE
%doc MAINTAINERS
%doc README.md
%{ocaml_libdir}/xapi-netdev
%exclude %{ocaml_libdir}/xapi-netdev/*.a
%exclude %{ocaml_libdir}/xapi-netdev/*.cmxa
%exclude %{ocaml_libdir}/xapi-netdev/*.cmxs
%exclude %{ocaml_libdir}/xapi-netdev/*.cmx
%exclude %{ocaml_libdir}/xapi-netdev/*.cmt
%exclude %{ocaml_libdir}/xapi-netdev/*.cmti
%exclude %{ocaml_libdir}/xapi-netdev/*.mli
%{ocaml_libdir}/stublibs/dllxapi_netdev_stubs.so

%files devel
%{ocaml_libdir}/xapi-netdev/*.a
%{ocaml_libdir}/xapi-netdev/*.cmx
%{ocaml_libdir}/xapi-netdev/*.cmxa
%{ocaml_libdir}/xapi-netdev/*.cmxs
%{ocaml_libdir}/xapi-netdev/*.mli
%{ocaml_docdir}/xapi-netdev

%changelog
* Wed Jan 23 2019 Christian Lindig <christian.lindig@citrix.com> - 1.3.0-1
- Prepare for Dune 1.6

* Fri Jan 11 2019 Christian Lindig <christian.lindig@citrix.com> - 1.2.0-1
- Port to dune.

* Wed Apr 04 2018 Marcello Seri <marcello.seri@citrix.com> - 1.1.0-6
- Update SPEC file to get rid of rpmbuild warnings

* Wed Jan 10 2018 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 1.1.0-1
- Ported build from oasis to jbuilder

* Mon Mar 13 2017 Marcello Seri <marcello.seri@citrix.com> - 1.0.0-2
- Update OCaml dependencies and build/install script after xs-opam-repo split

* Wed Jun 22 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Fri Jun 6 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.1-1
- Update to 0.9.1

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.9.0-2
- Split files correctly between base and devel packages

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.0-1
- Initial package

