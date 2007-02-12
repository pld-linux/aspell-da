Summary:	Danish dictionary for aspell
Summary(da.UTF-8):	Den store danske ordliste
Summary(pl.UTF-8):	Duński słownik dla aspella
Name:		aspell-da
Version:	1.4.42
%define	subv	1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/da/aspell5-da-%{version}-%{subv}.tar.bz2
# Source0-md5:	d14c03dca23b572606279d7317b022d0
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Danish dictionary (i.e. word list) for aspell.

%description -l da.UTF-8
Den store danske ordliste.

%description -l pl.UTF-8
Duński słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell5-da-%{version}-%{subv}

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
