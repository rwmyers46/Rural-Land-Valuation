## Rural Land Valuation:

Rural land is a notoriously difficult asset to price. The relatively low transaction volume coupled with nebulous land features create a market with few similarly comparable properties. This project focused on quantifying land features in order to improve accuracy for investment decisions.

<p align="center">
<img src="https://github.com/rwmyers46/Rural-Land-Valuation/blob/master/images/horses.jpg" width="500" height="300"/>
</p>

###### *Photo by Christine Mendoza on Unsplash*

### Data Collection:

In order to control for geographic and legislative variation, such as topography, climate, and taxes, the sample set was chosen from a region of contiguous counties comprising the Blacklands North Texas Region. Data was sourced from [landoftexas.com](https://www.landsoftexas.com/) property listings and processed using **Beautiful Soup** and **Selenium**. In order to ensure that the data accurately represented market value, the dataset only included transacted properties.

<p align="center">
<img src="https://github.com/rwmyers46/Rural-Land-Valuation/blob/master/images/blacklands_region.png" width="500" height="300"/>
</p>

### Text Processing:

Text processing was a bifurcated flow, with branches for structured and unstructued data. Structured property listing features with associated HMTL tags, such as *size* or *price*, were stripped and saved to **Numpy** arrays. Unstructured text from a listing's Property Description section were processed with `featureCounts`, a custom **Natural Language Processing** function that creates booleanized features from the presence of an approximate word. The data were then recombined into a dataframe with the `ArrayMaker` function.

### Feature Engineering:

Next to water features, elevation is perhaps the region's most sought after land feature. Properties with higher elevations are more likely to provide vistas for home sites, varied topography, and better drainage for agriculture.

To find property elevation, Google Maps API was employed. The `GCP_Features` function from the `Add_GIS_Features` utility file takes a dataframe argument and returns a dataframe with elevation and driving time from the nearest CBD of Dallas. For each address `GCP_Features` calls the `get_GIS` function, which first uses the Google Maps Geocode API to get the latitude & longitude for a property address, and then sends these values back to Google Maps Elevation API to fetch the elevation.

### Model:

The following model regression model classes were evaluated with cross validation:

* Linear Regression
* Ridge
* Lasso
* Random Forest
* XG Boost
* K-Nearest Neighbors
* Multilayer Perception
* Polynomial
* Elastic Net

Simple Linear Regression produced the best results with an R^2 of 25.34%. The lower coefficient of determination most likely resulted from property description inaccuracy and variance. But although most variance is unexplained, the feature impact on valuation is consistent with domain knowledge:

* Water features uniformly showed the greatest premium of `$100 - $250` per acre
* Bosque & McClellan county are considered the region's two most desirable counties
* Agricultural features such as *barn* & *cattle*, which suggest flatter, more open land were discounted accordingly

### Assumptions & Error Sources:

A property listing's data majority was in the Description section. This results in the data's accuracy being wholly dependent on the thoroughness and veracity of the listing broker. Since landsoftexas.com owns the category for land sales in the United States, the associated error was unavoidable without employing advanced GIS and satellite image processing techniques. 

* Sale price seasonality
* Topography feature mentions proportional to reality
* Mineral right ownership claims accurate



