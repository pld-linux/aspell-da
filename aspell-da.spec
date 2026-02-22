Summary:	Danish dictionary for aspell
Summary(da.UTF-8):	Den store danske ordliste
Summary(pl.UTF-8):	Duński słownik dla aspella
Name:		aspell-da
Version:	1.6.36
%define	subv	11-0
Release:	3
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	https://ftp.gnu.org/gnu/aspell/dict/da/aspell6-da-%{version}-%{subv}.tar.bz2
# Source0-md5:	a3981f71bca43b5533897ba1dfe8b154
URL:		http://aspell.net/
BuildRequires:	aspell >= 2:0.60.0
Requires:	aspell >= 2:0.60.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Danish dictionary (i.e. word list) for aspell.

%description -l da.UTF-8
Den store danske ordliste.

%description -l pl.UTF-8
Duński słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell6-da-%{version}-%{subv}

gunzip doc/contributors.gz

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
%doc Copyright doc/{README,contributors}
%{_prefix}/lib/aspell/da.multi
%{_prefix}/lib/aspell/da.rws
%{_prefix}/lib/aspell/danish.alias
%{_prefix}/lib/aspell/dansk.alias
%{_datadir}/aspell/da.dat
%{_datadir}/aspell/da_phonet.dat
