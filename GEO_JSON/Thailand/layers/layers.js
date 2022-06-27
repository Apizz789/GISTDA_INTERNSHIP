var wms_layers = [];

var format_PV_CLEANSING_0 = new ol.format.GeoJSON();
var features_PV_CLEANSING_0 = format_PV_CLEANSING_0.readFeatures(json_PV_CLEANSING_0, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_PV_CLEANSING_0 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_PV_CLEANSING_0.addFeatures(features_PV_CLEANSING_0);
var lyr_PV_CLEANSING_0 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_PV_CLEANSING_0, 
                style: style_PV_CLEANSING_0,
                interactive: true,
                title: '<img src="styles/legend/PV_CLEANSING_0.png" /> PV_CLEANSING'
            });

lyr_PV_CLEANSING_0.setVisible(true);
var layersList = [lyr_PV_CLEANSING_0];
lyr_PV_CLEANSING_0.set('fieldAliases', {'PV_TN': 'PV_TN', 'TH': 'TH', });
lyr_PV_CLEANSING_0.set('fieldImages', {'PV_TN': 'TextEdit', 'TH': 'TextEdit', });
lyr_PV_CLEANSING_0.set('fieldLabels', {'PV_TN': 'no label', 'TH': 'header label', });
lyr_PV_CLEANSING_0.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});