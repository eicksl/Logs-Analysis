# Logs Analysis

This tool uses Vagrant. Download it from
[vagrantup.com](https://www.vagrantup.com/downloads.html), then follow these
steps after installation:

* Download the virtual machine configuration [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)

* Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

* Move both the data and the logs directory into ```FSND-Virtual-Machine/vagrant```

* Navigate to the above directory on the command line and run ```vagrant up```
to connect to the virtual machine, then log in with ```vagrant ssh```

* Move to the logs directory with ```cd vagrant/logs```, then run
```python3 logs.py``` to launch the analysis tool