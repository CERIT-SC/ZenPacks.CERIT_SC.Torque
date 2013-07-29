from xml.dom.minidom import parseString
from Products.DataCollector.plugins.CollectorPlugin import CommandPlugin

def xmlData(n,t,d=None):
    try:
        return n.getElementsByTagName(t)[0].childNodes[0].data
    except:
        return d

class pbsnodes(CommandPlugin):
    """
    Run psbnodes to model Torque nodes.
    """
    command = 'pbsnodes -x'
    relname = "pbsNodes"
    modname = "ZenPacks.CERIT_SC.Torque.PbsNode"

    oses = ['Linux', 'Darwin', 'SunOS', 'AIX']

    def condition(self, device, log):
        return device.os.uname == '' or device.os.uname in self.oses

    def process(self, device, results, log):
        log.info('Collecting pbsnodes for device %s' % device.id)
        rm = self.relMap()
        dom = parseString(results)
        for n in dom.getElementsByTagName('Node'):
            om = self.objectMap()
            om.hostname     = xmlData(n,'name')
            #om.id           = self.prepId(str('%s_%s' % (om.hostname)))
            #om.id           = self.prepId(str('%s' % (om.hostname)))
            om.id           = self.prepId(om.hostname))
            om.np           = int(xmlData(n,'np','0'))
            om.npFree       = int(xmlData(n,'npfree','0'))
            om.state        = xmlData(n,'state')
            om.properties   = xmlData(n,'properties')
            rm.append(om)
        log.info(rm)
        return rm
