## SuperWASP air conditioner daemon [![Travis CI build status](https://travis-ci.org/warwick-one-metre/aircond.svg?branch=master)](https://travis-ci.org/warwick-one-metre/aircond)

Part of the observatory software for the Warwick La Palma telescopes.

`aircond` is a Pyro frontend that interfaces with the Panasonic comfort cloud API to monitor and control the air conditioners.

The instrument/camera room air conditioner is automatically disabled when the roof is open (as measured by the room alert), and restored when closed.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software setup

Create a file `/root/.netrc` owned by root with permission 700:
```
machine aircon
login <email for comfort cloud account>
password <password for comfort cloud account>
```

After installing `wasp-aircon-server`, the `aircond` must be enabled using:
```
sudo systemctl enable aircond.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start aircond.service
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9030/tcp --permanent
sudo firewall-cmd --reload
```
