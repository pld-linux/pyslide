Summary:	A tiny program to make presentations.
Summary(pl):	Malutki program do robienia prezentacji.
Name:		pyslide
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://www.hispalinux.es/~setepo/pyslide/%{name}-%{version}.tar.gz
# Source0-md5:	cdb7336ec2507e698646a5aa901f0fde
Patch0:		%{name}-include.patch
URL:		http://www.hispalinux.es/~setepo/pyslide/
BuildRequires:	python-modules >= 2.3
BuildRequires:	python-pygame-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyslide is a tiny program to make presentations. It uses SDL (through
pygame) to create interesting effects. The presentations are created
in an XML file. You can compile it into Python code. At this moment,
there is no exhaustive document about the language, but you can read a
brief description in the README file. The vocabulary is very easy, and
there are examples in the distribution where all of the features are
shown.

%description -l pl
Pyslide jest ma�ym programem do robienia prezentacji. U�ywa SDL
(poprzez pygame) w celu uzyskania ciekawych efekt�w graficznych.
Prezentacje s� tworzone w plikach XML. Mog� one by� kompilowane do
kodu Pythona. Na t� chwil� nie ma dokumentu dok�adnie opisuj�cego
sk�adni� opisu prezentacji. Kr�tki opis znajduje si� w pliku README -
sk�adnia jest bardzo prosta. Za��czone przyk�ady pokazuj� wszystkie
mo�liwo�ci pyslide.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags}"
export CLFAGS
BUILD_EXT=1 python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version},%{_mandir}/man1}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

BUILD_EXT=1 python setup.py install \
   --root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
%dir %{py_sitedir}/Pyslide
%{py_sitedir}/Pyslide/*.so
%{py_sitedir}/Pyslide/*.py[co]