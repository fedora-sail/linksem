Name:           linksem
Version:        0.8
Release:        %autorelease
Summary:        Semantic model for aspects of ELF static linking and DWARF debug information

License:        BSD-2-Clause
URL:            https://github.com/rems-project/%{name}
Source0:        https://github.com/rems-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  lem-devel
BuildRequires:  ocaml >= 4.08.1
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-zarith-devel
BuildRequires:  ocaml-rpm-macros

%global debug_package %{nil}

%description
Linksem is a formalisation of substantial parts of ELF linking and DWARF debug information.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n linksem-%{version} -p1

%build
export LEMLIB=/usr/share/lem/library
make

%install
mkdir -p %{buildroot}%{ocamldir}/linksem
make install INSTALLDIR=%{buildroot}%{ocamldir}
%ocaml_files

%files -f .ofiles
%license LICENSE
%doc README.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
