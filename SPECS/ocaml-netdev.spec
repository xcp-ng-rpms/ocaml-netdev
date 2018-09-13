%global debug_package %{nil}

Name:           ocaml-netdev
Version:        1.1.0
Release:        14%{?dist}
Summary:        Manipulate Linux bridges, network devices and openvswitch instances in OCaml
License:        LGPL
URL:            https://github.com/xapi-project/netdev
Source0:        https://code.citrite.net/rest/archive/latest/projects/XSU/repos/netdev/archive?at=v%{version}&format=tar.gz&prefix=netdev-%{version}#/netdev-%{version}.tar.gz
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/netdev/archive?at=v1.1.0&format=tar.gz&prefix=netdev-1.1.0#/netdev-1.1.0.tar.gz) = 2de554b4515b6cbc531674a4365dc71e9bd6e267
BuildRequires:  xs-opam-repo
BuildRequires:  forkexecd-devel

%global _use_internal_dependency_generator 0
%global __requires_exclude *caml*

%description
Manipulate Linux bridges, network devices and openvswitch instances in OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       forkexecd-devel%{?_isa}
Requires:       xs-opam-repo

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%global ocaml_dir /usr/lib/opamroot/system
%global ocaml_libdir %{ocaml_dir}/lib
%global ocaml_docdir %{ocaml_dir}/doc

%prep
%autosetup -p1 -n netdev-%{version}

%build
eval $(opam config env --root=/usr/lib/opamroot)
make

%install
eval $(opam config env --root=/usr/lib/opamroot)
mkdir -p %{buildroot}%{ocaml_libdir}
mkdir -p %{buildroot}%{ocaml_docdir}
make install OPAM_PREFIX=%{buildroot}%{ocaml_dir} OPAM_LIBDIR=%{buildroot}%{ocaml_libdir}

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

