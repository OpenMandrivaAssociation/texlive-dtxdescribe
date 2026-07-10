%global tl_name dtxdescribe
%global tl_revision 79394

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.10
Release:	%{tl_revision}.1
Summary:	Describe additional object types in dtx source files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dtxdescribe
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxdescribe.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxdescribe.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxdescribe.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The doc package includes tools for describing macros and environments in
LaTeX source .dtx format. The dtxdescribe package adds additional tools
for describing booleans, lengths, counters, hooks, sockets, plug, keys,
packages, classes, options, files, commands, arguments, and other
objects, and also works with the standard document classes as well, for
those who do not wish to use the .dtx format. Each item is given a
margin tag similar to \DescribeEnv, and is listed in the index by itself
and also by category. Each item may be sorted further by an optional
class. All index entries except code lines are hyperlinked. The
dtxexample environment is provided for typesetting example code and its
results. Contents are displayed verbatim along with a caption and cross-
referencing. They are then input and executed, and the result is shown.
Environments are also provided for displaying verbatim or formatted
source code, user-interface displays, and sidebars with titles. Macros
are provided for formatting the names of inline LaTeX objects such as
packages and booleans, as well as program and file names, file types,
internet objects, the names of certain programs, a number of logos, and
inline dashes and slashes.

