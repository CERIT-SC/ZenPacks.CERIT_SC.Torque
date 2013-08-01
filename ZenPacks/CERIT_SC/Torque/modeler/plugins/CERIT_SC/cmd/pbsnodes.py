from xml.dom.minidom import parseString
from Products.DataCollector.plugins.CollectorPlugin import CommandPlugin


class pbsnodes(CommandPlugin):
    """
    Run psbnodes to model Torque nodes.
    """
    command = 'pbsnodes -x'
    relname = "torqueNodes"
    modname = "ZenPacks.CERIT_SC.Torque.TorqueNode"

    oses = ['Linux', 'Darwin', 'SunOS', 'AIX']

    def condition(self, device, log):
        return device.os.uname == '' or device.os.uname in self.oses

    def xmlData(self,n,t,d=None):
        try:
            return n.getElementsByTagName(t)[0].childNodes[0].data
        except:
            return d

    def process(self, device, results, log):
        log.info('Collecting pbsnodes for device %s' % device.id)
        rm = self.relMap()
        dom = parseString(results)
        for n in dom.getElementsByTagName('Node'):
            om = self.objectMap()
            om.hostname = self.xmlData(n,'name')
            om.id = self.prepId(om.hostname)
            om.np = int(self.xmlData(n,'np','0'))
            om.priority = int(self.xmlData(n,'node_priority','0'))
            om.note = self.xmlData(n,'note','')
            om.queue = self.xmlData(n,'queue','')
            om.properties = self.xmlData(n,'properties')
            rm.append(om)
        log.info(rm)
        return rm
