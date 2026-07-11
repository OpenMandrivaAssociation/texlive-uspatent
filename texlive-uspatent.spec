%global tl_name uspatent
%global tl_revision 27744

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	U.S. Patent Application Tools for LaTeX and LyX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uspatent
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uspatent.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uspatent.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a class and other tools for developing a
beautifully formatted, consistent U.S. Patent Application using LaTeX
and/or LyX.

