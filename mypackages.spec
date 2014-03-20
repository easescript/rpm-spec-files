Name:     mypackages
Version:  1.0
Release:	1%{?dist}
Summary:	My Packages Meta
Vendor:   Ease Script
Group:		System Environment/Base
License:	Beerware
BuildArch:	noarch

BuildRequires:	rpm-build, yum-utils
Requires:	openssh-clients, bind-utils, cifs-utils, keyutils, perl-Net-IP, jwhois, lynx, lftp
Requires: perl-Image-ExifTool, ImageMagick, ffmpeg
Requires: vim-enhanced, ctags

%description
This meta-package provides some tools that I need.

%files

%changelog
* Thu Mar 20 2014 Ease Script <easescript@users.noreply.github.com> 1.0-1
- Initial build on CentOS 6.5
