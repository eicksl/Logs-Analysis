# Logs Analysis

This tool uses psycopg2 to connect to a PostreSQL database and perform various
queries to answer certain questions about the data.

This tool uses Vagrant. Download it from
[vagrantup.com](https://www.vagrantup.com/downloads.html), then follow these
steps after installation:

* Download the virtual machine configuration [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)

* Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

* Move both the data and the Logs-Analysis-master directory into ```FSND-Virtual-Machine/vagrant```

* Navigate to the above directory on the command line and run ```vagrant up```
to connect to the virtual machine, then log in with ```vagrant ssh```

* Move to the vagrant directory with ```cd /vagrant```, then run ```pqsl -d news -f newsdata.sql```

* Move to ```cd /logs-analysis-master```, then run ```python3 logs.py``` to launch the analysis tool

For inquiries, post an issue on the [github repository page](https://github.com/eicksl/Logs-Analysis/issues).
