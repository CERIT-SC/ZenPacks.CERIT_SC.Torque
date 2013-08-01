(function(){

var ZC = Ext.ns('Zenoss.component');

var ZEvActions = Zenoss.events.EventPanelToolbarActions;

ZC.TorqueNodePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            autoExpandColumn: 'note',
            componentType: 'TorqueNode',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'status'},
                {name: 'name'},
                {name: 'np'},
                {name: 'note'},
                {name: 'queue'},
                {name: 'operStatus'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{ 
                id: 'name',
                dataIndex: 'name',
                header: _t('Hostname'),
                width: 160
            },{ 
                id: 'np',
                dataIndex: 'np',
                header: _t('Procs'),
                width: 60
            },{
                id: 'queue',
                dataIndex: 'queue',
                header: _t('Queue'),
                width: 120
            },{
                id: 'note',
                dataIndex: 'note',
                header: _t('Note'),
            },{
                id: 'status',
                dataIndex: 'status',
                header: _t('Status'),
                sortable: true,
                width: 100
            },{
                id: 'operStatus',
                dataIndex: 'operStatus',
                header: _t('Operational Status'),
                renderer: Zenoss.render.pingStatus,
                width: 100
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                sortable: true,
                width: 65
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                sortable: true,
                width: 65
            }]
        });
        ZC.TorqueNodePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('TorqueNodePanel', ZC.TorqueNodePanel);
ZC.registerName('TorqueNode', _t('Torque node'), _t('Torque nodes'));

})();

