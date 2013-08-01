from Globals import InitializeClass

from Products.ZenRelations.RelSchema import ToOne, ToManyCont
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_DEVICE
from ZenPacks.community.deviceAdvDetail.HWStatus import *

class TorqueNode(DeviceComponent, ManagedEntity, HWStatus):
    """
    Component for TorqueNode
    """
    portal_type = meta_type = 'TorqueNode'

    hostname   = ''
    np         = 0
    priority   = 0
    note       = ''
    queue      = ''
    properties = ''
    status     = 1

    statusmap = {
        1:  (DOT_GREY,   SEV_WARNING,  'Unknown'),
        2:  (DOT_GREEN,  SEV_CLEAN,    'Free'),
        3:  (DOT_YELLOW, SEV_WARNING,  'Offline'),
        4:  (DOT_ORANGE, SEV_ERROR,    'Down'),
        5:  (DOT_GREEN,  SEV_CLEAN,    'Reserve'),
        6:  (DOT_GREEN,  SEV_CLEAN,    'Job-exclusive'),
        7:  (DOT_GREEN,  SEV_CLEAN,    'Job-sharing'),
        8:  (DOT_GREEN,  SEV_CLEAN,    'Busy'),
        9:  (DOT_ORANGE, SEV_ERROR,    'Frozen'),
        10: (DOT_GREEN,  SEV_CLEAN,    'Time-shared'),
    }

    _properties = (
        {'id':'hostname',   'type':'string',    'mode':'w'},
        {'id':'np',         'type':'int',       'mode':'w'},
        {'id':'priority',   'type':'int',       'mode':'w'},
        {'id':'note',       'type':'string',    'mode':'w'},
        {'id':'queue',      'type':'string',    'mode':'w'},
        {'id':'properties', 'type':'string',    'mode':'w'},
        {'id':'status',     'type':'int',       'mode':'w'},
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

    def getRRDTemplates(self):
        templates = []
        for tname in [self.__class__.__name__]:
            templ = self.getRRDTemplateByName(tname)
            if templ: templates.append(templ)
        return templates

    def viewName(self):
        return self.hostname
    titleOrId = name = viewName

    def device(self):
        return self.torqueDevice()

InitializeClass(TorqueNode)
