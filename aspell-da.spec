Summary:	Danish dictionary for aspell
Summary(pl):	Duñski s³ownik dla aspella
Name:		aspell-da
Version:	0.50
%define	subv	2
Release:	2
Epoch:		1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/da/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	c023f246ef448128e6a3b93388ed57e7
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Danish dictionary (i.e. word list) for aspell.

%description -l pl
Duñski s³ownik (lista s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README doc/contributors
%{_libdir}/aspell/*
%{_datadir}/aspell/*
