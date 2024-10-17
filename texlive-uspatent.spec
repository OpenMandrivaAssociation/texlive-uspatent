Name:		texlive-uspatent
Version:	27744
Release:	2
Summary:	U.S. Patent Application Tools for LaTeX and LyX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uspatent
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uspatent.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uspatent.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a class and other tools for developing a
beautifully formatted, consistent U.S. Patent Application using
LaTeX and/or LyX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uspatent/uspatent.cls
%doc %{_texmfdistdir}/doc/latex/uspatent/DocumentSettings.png
%doc %{_texmfdistdir}/doc/latex/uspatent/DrawingZoomBad.png
%doc %{_texmfdistdir}/doc/latex/uspatent/DrawingZoomGood.png
%doc %{_texmfdistdir}/doc/latex/uspatent/Drawings.lyx
%doc %{_texmfdistdir}/doc/latex/uspatent/Drawings.tex
%doc %{_texmfdistdir}/doc/latex/uspatent/LyX.png
%doc %{_texmfdistdir}/doc/latex/uspatent/LyXCustomInsets.png
%doc %{_texmfdistdir}/doc/latex/uspatent/LyXDocumentSettingsFont.png
%doc %{_texmfdistdir}/doc/latex/uspatent/LyXDocumentSettingsOutput.png
%doc %{_texmfdistdir}/doc/latex/uspatent/LyXEnvironments.png
%doc %{_texmfdistdir}/doc/latex/uspatent/LyXSettings.png
%doc %{_texmfdistdir}/doc/latex/uspatent/LyXSettingsDocumentClass.png
%doc %{_texmfdistdir}/doc/latex/uspatent/PatentApplication.lyx
%doc %{_texmfdistdir}/doc/latex/uspatent/PatentApplication.pdf
%doc %{_texmfdistdir}/doc/latex/uspatent/PatentApplication.tex
%doc %{_texmfdistdir}/doc/latex/uspatent/PatentApplicationGuide.lyx
%doc %{_texmfdistdir}/doc/latex/uspatent/PatentApplicationGuide.pdf
%doc %{_texmfdistdir}/doc/latex/uspatent/PatentApplicationGuide.tex
%doc %{_texmfdistdir}/doc/latex/uspatent/README
%doc %{_texmfdistdir}/doc/latex/uspatent/TeXworks.png
%doc %{_texmfdistdir}/doc/latex/uspatent/TpXDrawing.tpx
%doc %{_texmfdistdir}/doc/latex/uspatent/TpXSettingsAccess.png
%doc %{_texmfdistdir}/doc/latex/uspatent/VisioDrawing.pdf
%doc %{_texmfdistdir}/doc/latex/uspatent/VisioDrawing.vsd
%doc %{_texmfdistdir}/doc/latex/uspatent/VisioMainDrawing.vsd
%doc %{_texmfdistdir}/doc/latex/uspatent/VisioSave.png
%doc %{_texmfdistdir}/doc/latex/uspatent/annotationAlignment.png
%doc %{_texmfdistdir}/doc/latex/uspatent/uspatent.layout

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
