import Globals
import os.path

from Products.ZenModel.ZenPack import ZenPack as ZenPackBase
from Products.ZenUtils.Utils import unused

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Device import Device

Device._relations += (
    ('torqueNodes', ToManyCont(ToOne,
     'ZenPacks.CERIT_SC.Torque.TorqueNode','torqueDevice')),
)

unused(Globals)

class ZenPack(ZenPackBase):
    def install(self, dmd):
        ZenPackBase.install(self, dmd)
        o = dmd.Devices.createOrganizer('/Server/SSH/Linux/Torque')
#        o.setZenProperty( #+stavajici
#            'zCollectorPlugins',[
#                'CERIT_SC.cmd.pbsnodes'])

        for d in self.dmd.Devices.getSubDevices():
            d.buildRelations()

    def remove(self, dmd, leaveObjects=False):
        ZenPackBase.remove(self, dmd, leaveObjects=leaveObjects)
        Device._relations = tuple([x for x in Device._relations if x[0] not in ('torqueNodes')])
        for d in self.dmd.Devices.getSubDevices():
            d.buildRelations()
