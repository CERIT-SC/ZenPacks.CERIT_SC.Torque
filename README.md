# ZenPacks.CERIT_SC.Torque

## About

This is a [Zenoss](http://www.zenoss.com) monitoring system extension (ZenPack)
which allows to monitor [Torque](https://github.com/CESNET/torque) batch queue
system.

## Installation

Requirements server:

* Zenoss 4.0 or later
* [Advanced Device Details ZenPack](http://wiki.zenoss.org/ZenPack:Advanced_Device_Details)

Requirements hosts:

* [Torque](https://github.com/CESNET/torque) with commands:
 * `pbsnodes`
 * `/usr/bin/pbsnodes.bin`
 * `/usr/bin/qstat.bin`

### Normal Installation (packaged egg)

No prebuilt packages yet.

### Developer Installation (link mode)

    git clone https://github.com/CERIT-SC/ZenPacks.CERIT_SC.Torque.git
    zenpack --link --install ZenPacks.CERIT_SC.Torque
    zenoss restart

## Configuration

Following modelers are available:

* `CERIT_SC.cmd.pbsnodes`

Binded on device class `/Server/SSH/Linux/Torque`.

## Screenshots

* Torque nodes

![Torque nodes](https://raw.github.com/CERIT-SC/ZenPacks.CERIT_SC.Torque/master/screenshots/nodes.png)

* Torque node detail

![Detail](https://raw.github.com/CERIT-SC/ZenPacks.CERIT_SC.Torque/master/screenshots/detail.png)

* Device overview

![Overview](https://raw.github.com/CERIT-SC/ZenPacks.CERIT_SC.Torque/master/screenshots/overview.png)
