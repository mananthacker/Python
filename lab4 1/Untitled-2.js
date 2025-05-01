// Define the point of interest (latitude, longitude)
var point = ee.Geometry.Point([77.22868, 28.59145]); // Replace with your desired location

// Define the time ranges for each year from 2020 to 2024
var dateRanges = [
  ['2020-01-01', '2020-01-31'],
  ['2020-02-01', '2020-02-29'],
  ['2020-03-01', '2020-03-31'],
  ['2020-04-01', '2020-04-30'],
  // Continue this pattern for each month till 2024-12-31
  ['2024-11-01', '2024-11-30'],
  ['2024-12-01', '2024-12-31']
];

// Initialize an empty list to store mean cloud fraction values
var meanCloudFractions = [];

// Loop through each date range and compute the mean cloud fraction
dateRanges.forEach(function(range) {
  var dataset = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_CLOUD')
                  .filterBounds(point)
                  .filterDate(range[0], range[1])
                  .select('surface_albedo'); // Selecting the cloud fraction band

  var meanCloudFraction = dataset.mean().reduceRegion({
    reducer: ee.Reducer.mean(),
    geometry: point,
    scale: 1113, // Sentinel-5P resolution is approximately 1km
    maxPixels