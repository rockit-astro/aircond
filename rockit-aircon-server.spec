Name:      rockit-aircon-server
Version:   %{_version}
Release:   1
Url:       https://github.com/rockit-astro/aircond
Summary:   Daemon for querying and controlling the half metre and computer room air conditioners.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3.9dist(rockit-common) python3.9dist(pcomfortcloud)

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
