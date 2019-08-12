import googlemaps
import pandas as pd
import numpy as np

def get_GIS(address):
    
    attr = dict() # property attribute dict
    myKey = 'myKey'   
    gmaps = googlemaps.Client(key = myKey)
    
    # get geocode of property address:
    geocode_result = gmaps.geocode(address)
    attr['lat'] = geocode_result[0]['geometry']['location']['lat']
    attr['lng'] = geocode_result[0]['geometry']['location']['lng']
    lat_lng = (attr['lat'], attr['lng'])
    
    # get elevation from lat / long:
    elevation_result = gmaps.elevation(lat_lng)
    attr['elevation'] = elevation_result[0]['elevation']*3.28 # convert meters to feet
    
    # get time & distance from Dallas, TX to property:
    directions_result = gmaps.distance_matrix('Dallas, TX', lat_lng)
    attr['travel_time'] = directions_result['rows'][0]['elements'][0]['duration']['value'] / 60 # convert to minutes
    attr['distance'] = directions_result['rows'][0]['elements'][0]['distance']['value']*0.000621371 # convert to miles

    return(attr)


def GCP_Features(property_dataframe):
    
    df = property_dataframe
    
    # run get_GIS for each property and clean returned values:
    header_list = list(df.columns)
    header_list.extend(['lat', 'lng', 'elevation','travel_time', 'distance'])
    df = df.reindex(columns = header_list)
    error_log = []
    
    # retrieve elevation for each property with get_GIS function:
    for ind in df.index:
        if df['address'][ind] == None:
            addr = df['zip'][ind]
        else:
            addr = df['address'][ind] + ', ' + df['zip'][ind]
        try:
            gis_attributes = get_GIS(addr)
    
    # unpack dictionary to populate attributes:
            for key, val in gis_attributes.items():
                df[key][ind] = val
        except:
            error_log.append(ind)
            
    print('Fetch Errors:', len(error_log))
    
    # replace None values with regional elevation mean:
    if df['elevation'].isna().any().sum() > 0:
        df['elevation'].fillna(df.elevation.mean(), inplace = True)
    if df['travel_time'].isna().any().sum() > 0:
        df['travel_time'].fillna(df.travel_time.mean(), inplace = True)
        
    # save retrieved data, remove obsolete columns, and inspect result:
    gis_df = df.drop(columns = ['word_count', 'address', 'zip', 'lat', 'lng', 'distance'])
    df.to_pickle('./data/post-gis.pkl')
    
    return(gis_df)
    
