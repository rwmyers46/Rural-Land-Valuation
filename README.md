## Rural Land Valuation:

Rural land is a notoriously difficult asset to price. The relatively low transaction volume coupled with nebulous land features create a market with few similarly comparable properties. This project focused on quantifying land features in order to improve accuracy for investment decisions.

<p align="center">
  <img src="https://github.com/rwmyers46/Rural-Land-Valuation/blob/master/images/horses.jpg" width="500" height="300"/>
</p>
<p align="center"><h6>
  Photo by Christine Mendoza on Unsplash
</h6></p>


### Data Collection:

In order to control for geographic and legislative variation, such as topography, climate, and taxes, the sample set was chosen from a region of contiguous counties comprising the Blacklands North Texas Region. Data was sourced from [landoftexas.com](https://www.landsoftexas.com/) property listings and processed using **Beautiful Soup** and **Selenium**. In order to ensure that the data accurately represented market value, the dataset only included transacted properties.

<p align="center">
  <b>Blacklands North Texas Region</b>
</p>

<p align="center">
<img src="https://github.com/rwmyers46/Rural-Land-Valuation/blob/master/images/blacklands_region.png" width="500" height="300"/>
</p>

### Text Processing:

Text processing was a bifurcated flow, with branches for structured and unstructued data. Structured property listing features with associated HMTL tags, such as *size* or *price*, were stripped and saved to **Numpy** arrays. Unstructured text from a listing's Property Description section were processed with `featureCounts`, a custom **Natural Language Processing** function that creates booleanized features from the presence of an approximate word. The data were then recombined into a dataframe with the `ArrayMaker` function.

### Feature Engineering:

Next to water features, elevation is perhaps the region's most sought after land feature. Properties with higher elevations are more likely to provide vistas for home sites, varied topography, and better drainage for agriculture.

To find property elevation, the **GCP** Google Map's API was employed. The `GCP_Features` function from the `Add_GIS_Features` utility file takes a dataframe argument and returns a dataframe with elevation and driving time from the nearest CBD of Dallas. For each address `GCP_Features` calls the `get_GIS` function, which first uses the Google Maps Geocode API to get the latitude & longitude for a property address, and then sends these values back to Google Maps Elevation API to fetch the elevation.

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
* Elastic Net|

Lasso, Ridge, and Simple Linear Regression demonstrated the best results in initial testing. These classes were optimized with RidgeCV & LassoCV across a range of Alpha values and visualized with Yellowbrick.

<p align="center">
  <img src="https://github.com/rwmyers46/Rural-Land-Valuation/blob/master/visualizations/CV_scores.png"/>
</p>

<p align="center">
  <img src="https://github.com/rwmyers46/Rural-Land-Valuation/blob/master/visualizations/alpha_selection.png"/>
</p>

To determine whether a higher order polynomial would yield better accuracy, a learning curve was plotted for degrees 0 to 5. In this test, the best R^2 occurred at n = 1.

<p align="center">
  <img src="https://github.com/rwmyers46/Rural-Land-Valuation/blob/master/visualizations/polydegs.png"/>
</p>

Simple Linear Regression produced the best results with an R^2 of 25.34%. The lower coefficient of determination most likely resulted from property description inaccuracy and variance. But although most variance is unexplained, the feature impact on valuation is consistent with domain knowledge:

* Water features uniformly showed the greatest premium of `$100 - $250` per acre
* Bosque & McClellan county are considered the region's two most desirable counties
* Agricultural features such as *barn* & *cattle*, which suggest flatter, more open land were discounted accordingly

<p align="center">
  <img src="https://github.com/rwmyers46/Rural-Land-Valuation/blob/master/visualizations/feature_impacts.png"/>
</p>

### Assumptions & Error Sources:

A property listing's data majority was in the Description section. This results in the data's accuracy being wholly dependent on the thoroughness and veracity of the listing broker. Since landsoftexas.com owns the category for land sales in the United States, the associated error was unavoidable without employing advanced GIS and satellite image processing techniques. 

* Sale price seasonality
* Topography feature mentions proportional to reality
* Mineral right ownership claims accurate

### Results:

Ultimately, it proved difficult to beat Simple Linear Regression. Even the best models were unable to best a 30% coefficient of determination, largely resulting from property description inaccuracy and variance. But although the models do not account for 70% of the variance, the feature impact on valuation is consistent with domain knowledge:

* Water features uniformly showed the greatest premium of $100 to $250 per acre
* Bosque & McClellan county are considered the regions best counties
* Agricultural features such as Barn & Cattle suggest land that is flat and open and were discounted accordingly

##### Surprises:

1. Oil & gas rights ownership ("minerals") negatively impacted valuations. Since mineral rights are an asset sellers prefer to retain, this finding would only make sense *if* it could be demonstrated that brokers advertise minerals to increase the appeal of less desirable land. Note: oil has not been discovered in the region.

2. Properties with a greater travel time from the Dallas CBD were generally priced higher. This relationship may be due to the desire for privacy and quiet. One tradeoff for a more remote property, absent of highway noise, is a less-navigable ingress. In the country, this usually entails a single-lane, unpaved road safe only at lower speeds.

##### Future Work:

1. Data - Collecting more data would have been the simplest way to improve model accuracy, but the source site changed design mid-project, making this untenable within the given timeline. 

2. GIS - Results could also be improved using more advanced GIS processing - not only to extract property features consistently across listings, but also to collect numerical measurements of said features: water feature size, wooded to open land ratio, and presence of high voltate transmission lines.

3. Curb Appeal - A lot can be gleaned from a property's front gate. Fence condition, visible trash, and grandness of an entrace all impact valuation and are accessible from Google's Street View API and could used to train a neural net. 
