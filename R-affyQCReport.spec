%define		packname	affyQCReport

Summary:	QC Report Generation for affyBatch objects
Name:		R-%{packname}
Version:	1.36.0
Release:	1
License:	LGPL v2+
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	9712a8f30e08dc7798ac9601ec297a06
URL:		http://bioconductor.org/packages/release/bioc/html/%{packname}.html
BuildRequires:	R
BuildRequires:	R-Biobase
BuildRequires:	R-affy
BuildRequires:	R-affyPLM
BuildRequires:	R-genefilter
BuildRequires:	R-simpleaffy
BuildRequires:	R-cran-RColorBrewer
BuildRequires:	R-cran-xtable
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-Biobase
Requires:	R-affy
Requires:	R-affyPLM
Requires:	R-genefilter
Requires:	R-simpleaffy
Requires:	R-cran-RColorBrewer
Requires:	R-cran-xtable
Suggests:	R-tkWidgets
Suggests:	R-affydata
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package creates a QC report for an AffyBatch object.
The report is intended to allow the user to quickly assess the quality
of a set of arrays in an AffyBatch object.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/Templates
%{_libdir}/R/library/%{packname}/scripts
