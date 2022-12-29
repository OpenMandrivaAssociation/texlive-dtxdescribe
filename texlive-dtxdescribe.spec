Name:		texlive-dtxdescribe
Version:	65223
Release:	1
Summary:	Describe additional object types in dtx source files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dtxdescribe
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxdescribe.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxdescribe.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxdescribe.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The doc package includes tools for describing macros and
environments in LaTeX source .dtx format. The dtxdescribe
package adds additional tools for describing booleans, lengths,
counters, keys, packages, classes, options, files, commands,
arguments, and other objects, and also works with the standard
document classes as well, for those who do not wish to use the
.dtx format. Each item is given a margin tag similar to
\DescribeEnv, and is listed in the index by itself and also by
category. Each item may be sorted further by an optional class.
All index entries except code lines are hyperlinked. The
dtxexample environment is provided for typesetting example code
and its results. Contents are displayed verbatim along with a
caption and cross-referencing. They are then input and
executed, and the result is shown. Environments are also
provided for displaying verbatim or formatted source code,
user-interface displays, and sidebars with titles. Macros are
provided for formatting the names of inline LaTeX objects such
as packages and booleans, as well as program and file names,
file types, internet objects, the names of certain programs, a
number of logos, and inline dashes and slashes.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/dtxdescribe
%{_texmfdistdir}/tex/latex/dtxdescribe
%doc %{_texmfdistdir}/doc/latex/dtxdescribe

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
