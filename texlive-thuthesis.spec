# revision 24361
# category Package
# catalog-ctan /macros/latex/contrib/thuthesis
# catalog-date 2009-03-02 15:13:08 +0100
# catalog-license lppl
# catalog-version 4.5.1
Name:		texlive-thuthesis
Version:	4.5.1
Release:	1
Summary:	Thesis template for Tsinghua University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thuthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thuthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thuthesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thuthesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
ThuThesis is a LaTeX thesis template package for Tsinghua
University in order to make it easy to write theses for either
bachelor's, master's or doctor's degree.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/thuthesis/thubib.bst
%{_texmfdistdir}/tex/latex/thuthesis/thuthesis.cfg
%{_texmfdistdir}/tex/latex/thuthesis/thuthesis.cls
%{_texmfdistdir}/tex/latex/thuthesis/thutils.sty
%doc %{_texmfdistdir}/doc/latex/thuthesis/README
%doc %{_texmfdistdir}/doc/latex/thuthesis/dtx-style.sty
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/Makefile
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/data/ack.tex
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/data/appendix01.tex
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/data/chap01.tex
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/data/chap02.tex
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/data/cover.tex
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/data/denotation.tex
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/data/resume.tex
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/figures/hello.eps
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/figures/hello.fig
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/figures/hello.pdf
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/figures/thu-fig-logo.eps
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/figures/thu-fig-logo.pdf
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/figures/thu-lib-logo.eps
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/figures/thu-lib-logo.pdf
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/figures/thu-text-logo.eps
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/figures/thu-text-logo.pdf
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/figures/thu-whole-logo.eps
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/figures/thu-whole-logo.pdf
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/main.tex
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/msmake.cmd
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/ref/refs.bib
%doc %{_texmfdistdir}/doc/latex/thuthesis/example/shuji.tex
%doc %{_texmfdistdir}/doc/latex/thuthesis/thuthesis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/thuthesis/thuthesis.dtx
%doc %{_texmfdistdir}/source/latex/thuthesis/thuthesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
