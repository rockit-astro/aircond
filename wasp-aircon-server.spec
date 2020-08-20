Name:      wasp-aircon-server
Version:   1.0.0
Release:   0
Url:       https://github.com/warwick-one-metre/tngd
Summary:   TNG weather feed client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwick-observatory-common, python3-pcomfortcloud
Requires:  observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the Warwick La Palma telescopes.

aircond is a Pyro frontend that interfaces with the Panasonic comfort cloud API to monitor and control the air conditioners.

The instrument/camera room air conditioner is automatically disabled when the roof is open (as measured by the room alert), and restored when closed.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/aircond %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/aircond.service %{buildroot}%{_unitdir}

%post
%systemd_post aircond.service

%preun
%systemd_preun aircond.service

%postun
%systemd_postun_with_restart aircond.service

%files
%defattr(0755,root,root,-)
%{_bindir}/aircond
%defattr(-,root,root,-)
%{_unitdir}/aircond.service

%changelog
