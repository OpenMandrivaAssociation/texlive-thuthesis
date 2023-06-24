Name:		texlive-thuthesis
Version:	67127
Release:	1
Summary:	Thesis template for Tsinghua University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thuthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thuthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thuthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thuthesis.source.r%{version}.tar.xz
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
%{_texmfdistdir}/bibtex/bst/thuthesis
%{_texmfdistdir}/tex/latex/thuthesis
%doc %{_texmfdistdir}/doc/latex/thuthesis
#- source
%doc %{_texmfdistdir}/source/latex/thuthesis

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
