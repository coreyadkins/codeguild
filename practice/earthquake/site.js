'use strict';
/*
This program creates a world map and adds tokens for each earthquake in the past
7 days. The tokens vary in size based on magnitude of the earthquake (larger
token, larger magnitude), and in opacity based on age (older earthquake: more
opaque).
It uses OpenLayers to create the map and map objects. The EarthquakeData is
sorurced from usgs.gov.
 */

/**
 * Fixes linter issues with OpenLayers.
 */
if (!window.ol) {
  var ol = {};
}

var ACCESS_TIME_UTC = new Date().getTime();


/**
 * Inputs new Earthquake Data from usgs.gov.
 */
function getEarthquakeData() {
  var url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson';
  return Promise.resolve($.ajax({
    dataType: 'json',
    url: url
  }));
}

/**
 * Data Transformation- Pulls magnitude, longitude, latitude, and time of each
 * earthquake into an array and maps them together into an array of arrays.
 * @param  {JSON object} earthquakeData: geoJSON object containing all
 * earthquakeData for the previous week.
 * @return {Array}                array of arrays containing magnitude,
 *                                 coordinates, and time of each earthquake.
 */
function getEqCoordsMagsAndTimes(earthquakeData) {
  var features = earthquakeData.features;
  return _.map(features, function(feature) {
    var magnitude = feature.properties.mag;
    var longitude = feature.geometry.coordinates[0];
    var latitude = feature.geometry.coordinates[1];
    var time = feature.properties.time;
    return [magnitude, longitude, latitude, time];
  });
}
/**
 * Creates the OpenLayers map which the Earthquake tokens will be placed onto.
 * @return {Object} Instanced 'map' OpenLayers object which represents the map
 * background on which earthquake tokens will be placed.
 */
function createMap() {
  var map = new ol.Map({
    view: new ol.View({
      center: [0, 0],
      zoom: 1,
      projection: 'EPSG:4326'
    }),
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      }),
    ],
    target: 'map'
  });
  return map;
}

/**
 * Calculates the opacity of a token based on its age since time of access.
 * @param  {number} time Time of earthquake, in UTC time (milliseconds since
 * 01-01-1970)
 * @return {number}      Opacity of object based on how recently it ocurred,
 * with 1 meaning it occurred the moment of access.
 */
function calculateOpacity(time) {
  var weekUTC = 604800000;
  var timeBeforeAccess = (time - ACCESS_TIME_UTC) * -1;
  return timeBeforeAccess / weekUTC;
}

/**
 * Calculates the scale of a token based on the magnitude size of earthquake.
 * @param  {number} magnitude Richter scale measurement of the earthquake size
 *                            (1-10)
 *         {number} scaleMax  Maximum value of scale for desired visual output.
 * @return {number}           Scale number of object.
 */
function calculateScale(magnitude) {
  var percentOfMax = magnitude / 10;
  var scaleMax = .75;
  return percentOfMax * scaleMax;
}

/**
 * Takes in transformed earthquake data and creates a .Feature OpenLayers
 * object which contains the coordinates of the earthquake, its time, and its
 * magnitude.
 * @param  {array} eqCoordsMagsAndTimes Array of arrays containing earthquake data.
 * @return {Object}                  OpenLayers.Feature object containing data.
 */
function getPlotPoints(eqCoordsMagsAndTimes) {
  return _.map(eqCoordsMagsAndTimes, function(eqCoordMagAndTime) {
    return new ol.Feature({
      geometry: new ol.geom.Point([eqCoordMagAndTime[1],eqCoordMagAndTime[2]]),
      magnitude: eqCoordMagAndTime[0],
      time: eqCoordMagAndTime[3]
    });
  });
}

/**
 * Creates a new layer and adds individual points to the layer, applying style
 * based on the magnitude and time of the earthquake.
 * @param {array} plotPoints    Array of objects containing each individual
 * .Feature object which correspond to each earthquake in data.
 * @param {object} map           Instanced ol.Map object.
 */
function addPointsToMap(plotPoints, map) {
  var vectorSource = new ol.source.Vector({});
  for (var i = 0; i < plotPoints.length; i += 1) {
    vectorSource.addFeature(plotPoints[i]);
  }
  var newLayer = new ol.layer.Vector({
    source: vectorSource,
    style: function(feature) {
      return new ol.style.Style({
        image: new ol.style.Icon({
          opacity: calculateOpacity(feature.get('time')),
          scale: calculateScale(feature.get('magnitude')),
          size: [250, 250],
          src: '../earthquake/earthquake.png'
        })
      });
    }
  });
  map.addLayer(newLayer);
}

/**
 * Piping function which transforms earthquakeData, gets OpenLayers plot points
 * from this data, then plots these points onto the map.
 * @param  {JSON object} earthquakeData geoJSON object which contains all
 * earthquake data from the past week.
 * @param  {[type]} map            Instanced ol.Map object.
 */
function plotEarthquakePoints(earthquakeData, map) {
  var eqCoordsMagsAndTimes = getEqCoordsMagsAndTimes(earthquakeData);
  var plotPoints = getPlotPoints(eqCoordsMagsAndTimes);
  addPointsToMap(plotPoints, map);
}

/**
 * Initiates the creation of map, and running of plotEarthQuakePoints function
 * after page is loaded, holds promises to ensure proper order of loading.
 */
function initiateEventHandlers() {
  var map = createMap();
  getEarthquakeData().
    then(function(earthquakeData) {
      plotEarthquakePoints(earthquakeData, map);
    });
}


$(document).ready(initiateEventHandlers);
