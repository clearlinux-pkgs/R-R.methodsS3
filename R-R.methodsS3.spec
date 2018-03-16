#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-R.methodsS3
Version  : 1.7.1
Release  : 1
URL      : https://cran.r-project.org/src/contrib/R.methodsS3_1.7.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/R.methodsS3_1.7.1.tar.gz
Summary  : S3 Methods Simplified
Group    : Development/Tools
License  : LGPL(>=-2.1)
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n R.methodsS3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521238621

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521238621
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R.methodsS3
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R.methodsS3
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R.methodsS3
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library R.methodsS3|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/R.methodsS3/CITATION
/usr/lib64/R/library/R.methodsS3/DESCRIPTION
/usr/lib64/R/library/R.methodsS3/INDEX
/usr/lib64/R/library/R.methodsS3/Meta/Rd.rds
/usr/lib64/R/library/R.methodsS3/Meta/features.rds
/usr/lib64/R/library/R.methodsS3/Meta/hsearch.rds
/usr/lib64/R/library/R.methodsS3/Meta/links.rds
/usr/lib64/R/library/R.methodsS3/Meta/nsInfo.rds
/usr/lib64/R/library/R.methodsS3/Meta/package.rds
/usr/lib64/R/library/R.methodsS3/NAMESPACE
/usr/lib64/R/library/R.methodsS3/NEWS
/usr/lib64/R/library/R.methodsS3/R/R.methodsS3
/usr/lib64/R/library/R.methodsS3/R/R.methodsS3.rdb
/usr/lib64/R/library/R.methodsS3/R/R.methodsS3.rdx
/usr/lib64/R/library/R.methodsS3/help/AnIndex
/usr/lib64/R/library/R.methodsS3/help/R.methodsS3.rdb
/usr/lib64/R/library/R.methodsS3/help/R.methodsS3.rdx
/usr/lib64/R/library/R.methodsS3/help/aliases.rds
/usr/lib64/R/library/R.methodsS3/help/paths.rds
/usr/lib64/R/library/R.methodsS3/html/00Index.html
/usr/lib64/R/library/R.methodsS3/html/R.css