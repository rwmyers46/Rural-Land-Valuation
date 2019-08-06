## Rural Land Valuation:

Rural land is a notoriously difficult asset to price. The relatively low transaction volume coupled with nebulous land features create a market with few similarly comparable properties. This project focused on quantifying land features in order to improve accuracy for investment decisions.

<p align="center">
<img src="https://github.com/rwmyers46/Rural-Land-Valuation/blob/master/images/horses.jpg" width="500" height="300"/>
</p>

###### *Photo by Christine Mendoza on Unsplash*

### Data Collection:

In order to control for geographic and legislative variation, such as topography, climate, and taxes, the sample set was chosen from a region of contiguous counties comprising the Blacksland North Texas Region. Data was sourced from [landoftexas.com](https://www.landsoftexas.com/) property listings and processed using **Beautiful Soup** and **Selenium**. In order to ensure that the data accurately represented market value, the dataset only included transacted properties.

<p align="center">
<img src="https://github.com/rwmyers46/Rural-Land-Valuation/blob/master/images/blacklands_region.png" width="500" height="300"/>
</p>

### Text Processing:

Text processing comprised a two-step procedure, one for structured and another for unstructued data. Structured property listing features with associated HMTL tags, such as "size" or "price" were stripped and saved to **Numpy** arrays and unstructured text from a listing's Property Desciption section were processed with the `featureCounts` function. The data were then combined into a dataframe with the `ArrayMaker` function.

### Assumptions & Error Sources:

A property listing's data majority was in the Description section. This results in the data's accuracy being wholly dependent on the thoroughness and veracity of the listing broker. Since landsoftexas.com owns the category for land sales in the United States, the associated error was unavoidable without employing advanced GIS and satellite image processing techniques. 

* Sale price seasonality
* Topography feature mentions proportional to reality
* Mineral right ownership claims accurate



