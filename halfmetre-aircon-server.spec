Name:      halfmetre-aircon-server
Version:   20230202
Release:   0
Url:       https://github.com/warwick-one-metre/aircond
Summary:   Daemon for querying and controlling the half metre and computer room air conditioners.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-warwick-observatory-common python3-pcomfortcloud

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/aircond %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/aircond.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/aircond
%defattr(-,root,root,-)
%{_unitdir}/aircond.service

%changelog
