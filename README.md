## Air conditioner daemon

`aircond` is a Pyro frontend that interfaces with the Panasonic comfort cloud API to monitor and control the air conditioners.

The halfmetre room air conditioner is automatically disabled when the roof is open (as measured by the domealert), and restored when closed.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the observatory software architecture and instructions for developing and deploying the code.

### Software setup

Create a file `/root/.netrc` owned by root with permission 700:
```
machine aircon
login <email for comfort cloud account>
password <password for comfort cloud account>
```

After installing `halfmetre-aircon-server`, the `aircond` must be enabled using:
```
sudo systemctl enable --now aircond.service
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9030/tcp --permanent
sudo firewall-cmd --reload
```
