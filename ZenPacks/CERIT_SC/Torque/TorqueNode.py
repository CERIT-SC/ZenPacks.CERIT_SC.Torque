from Globals import InitializeClass

from Products.ZenRelations.RelSchema import ToOne, ToManyCont
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_DEVICE

class TorqueNode(DeviceComponent, ManagedEntity):
    """
    Component for TorqueNode
    """
    portal_type = meta_type = 'TorqueNode'

    hostname   = ''
    np         = 0
    priority   = 0
    state      = ''
    properties = ''

    _properties = (
        dict(id='hostname',   type='string',  mode='w'),
        dict(id='np',         type='int',     mode='w'),
        dict(id='priority',   type='int',     mode='w'),
        dict(id='state',      type='string',  mode='w'),
        dict(id='properties', type='string',  mode='w'),
    )

    _relations = (
        ('torqueDevice', ToOne(ToManyCont,'Products.ZenModel.Device.Device', 'torqueNodes')),
    )

    # Screen action bindings (and tab definitions)
    factory_type_information = ({   
        'id'             : 'TorqueNode',
        'meta_type'      : 'TorqueNode',
        'description'    : 'Torque Node Description',
        'icon'           : 'Device_icon.gif',
        'actions'        : ({
            'id'            : 'perfServer',
            'name'          : 'Graphs',
            'action'        : 'viewDevicePerformance',
            'permissions'   : (ZEN_VIEW, ),
        },{
            'id'            : 'perfConf',
            'name'          : 'Template',
            'action'        : 'objTemplates',
            'permissions'   : (ZEN_CHANGE_DEVICE, ),
        },),
    },)

    def viewName(self):
        return self.hostname
    titleOrId = name = viewName

    def device(self):
        return self.torqueNodeDevice()

#    def cpuUtilization(self):
#        try:
#            return (self.np-self.npFree)*100/self.np
#        except:
#            return 0

InitializeClass(TorqueNode)
