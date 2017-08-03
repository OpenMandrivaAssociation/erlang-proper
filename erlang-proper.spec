%global realname proper
%global upstream manopapad
# Technically, we're noarch; but erlang whose directories we install into is not.
%global debug_package %{nil}
%global commit 1b773eeb47cb2c3116d78bdf681505703b762eee


Name:       erlang-%{realname}
Version:    1.1
Release:    %mkrel 7
Group:      Development/Erlang
Summary:    A QuickCheck-inspired property-based testing tool for Erlang

License:    GPLv3+
URL:		https://github.com/%{upstream}/%{realname}
# VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
#Source0:	https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
# For now we are packaging a commit, because the 1.1 release does not build on Erlang 18 and
# upstream has not made a release since 2013.
Source0:    https://github.com/manopapad/proper/archive/%{commit}.tar.gz

BuildRequires: erlang-rebar


%description
PropEr (PROPerty-based testing tool for ERlang) is a QuickCheck-inspired
open-source property-based testing tool for Erlang.


%prep
%autosetup -n %{realname}-%{commit}


%build
%rebar_compile
./make_doc


%install
mkdir -p %{buildroot}%{_erllibdir}/%{realname}-%{version}/{ebin,include}
install -pm 644 ebin/* %{buildroot}%{_erllibdir}/%{realname}-%{version}/ebin
install -pm644 include/proper* %{buildroot}%{_erllibdir}/%{realname}-%{version}/include


%files
%license COPYING
%doc doc
%doc examples
%doc README.md
%{_erllibdir}/%{realname}-%{version}/



%changelog
* Fri May 06 2016 neoclust <neoclust> 1.1-7.mga6
+ Revision: 1009757
- Rebuild post boostrap
- imported package erlang-proper

