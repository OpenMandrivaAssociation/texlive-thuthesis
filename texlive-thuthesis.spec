%global tl_name thuthesis
%global tl_revision 79163

Name:		texlive-%{tl_name}
Epoch:		1
Version:	7.7.1
Release:	%{tl_revision}.1
Summary:	Thesis template for Tsinghua University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thuthesis
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thuthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thuthesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thuthesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package establishes a simple and easy-to-use LaTeX template for
Tsinghua dissertations, including general undergraduate research papers,
masters theses, doctoral dissertations, and postdoctoral reports.

