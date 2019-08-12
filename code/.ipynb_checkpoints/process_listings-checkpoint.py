import numpy as np
import pandas as pd

def featureCounts(prop_desc):   
    '''
    Builds a list of dicionaries for property attributes from listing description

    Args:
        prop_desc: list of property descriptions

    Returns:
        prop_features: list of dictionaries with boolean values for presence of feature
    '''

    # create a list of property attributes to serve as keys for features dictionary: 
    prop_keys = ['home','lake','pond','water','minerals','topo','game_fence','auto_gate','windmill',\
                 'barn','well', 'exemption','easement','paved','cattle', 'word_count']

    # boolean list for home, features, minerals, water
    prop_features = dict.fromkeys(prop_keys, 0)

    if prop_desc == 0:
        return(prop_features)

    # build lists of qualifying words to determine the presence of an attribute
    else:

        home_qual = ['house','home','bathroom','laundry','kitchen','porch','quarters','room','den']
        topo_list = ['elevation','view','hill','sloped','slopes','gullied']
        structure_list = ['windmill','barn','well','easement','lake','paved','cattle']
        mineral_list = ['oil','gas','mineral','minerals']
        water_list = ['water','river','creek','spring']
        pond_list = ['pond','tank','ponds','tanks']
        game_fence = ['game-fence','game fence','game fences','gamed fenced','high fence','high fences','high-fenced']
        ag_exempt = ['exemption','exempt']
        auto_gate = ['automatic gate','electronic gate']
        dump_list = ['the', 'and','with','for','this','has','your','will','very','acres',\
             'acre','along','beautiful','perfect','open','make','but','two','sq.',\
             'over','would','that','good','side','all','just','large','there','located',\
             'one','are','from','ft.','off','lots','great']    # unuseful values to discard

        new_list = [str(i).lower().strip('.').split(' ') for i in prop_desc]    # description list split by word
        new_list = sum(new_list, [])
        prop_features['word_count'] = len(new_list)   # word count of description

        # booleanize attributes by comparing property descriptions to qualifying lists:
        for j, i in enumerate(new_list):
            word_pair = new_list[j-1] + ' ' + new_list[j]
            if word_pair in game_fence:
                prop_features['game_fence'] = 1
            if word_pair in auto_gate:
                prop_features['auto_gate'] = 1
            if i in home_qual:
                prop_features['home'] = 1
            if i in mineral_list:
                prop_features['minerals'] = 1
            if i in water_list:
                prop_features['water'] = 1
            if i in pond_list:
                prop_features['pond'] = 1
            if i in topo_list:
                prop_features['topo'] = 1
            if i in ag_exempt:
                prop_features['exemption'] = 1 
            if i in structure_list:
                prop_features[i] = 1

        # return dictionary with boolean values for property attributes:
        return(prop_features)   
        
def ArrayMaker(data_input):
        '''
        Creates dataframe from property attribute arrays

        Args:
            data_input: list of lists and boolean dictionary of attributes

        Returns:
            df: dataframe of attributes by property
        '''

        # separate list attributes into numpy arrays:
        prop_id = np.array([i for i in data_input[0::9]])    
        prop_size = np.array([i for i in data_input[1::9]])
        prop_price = np.array([i for i in data_input[2::9]])
        prop_address = np.array([i for i in data_input[3::9]])
        prop_county = np.array([i for i in data_input[4::9]])
        zip_code = np.array([i for i in data_input[5::9]])
        prop_title = np.array([i for i in data_input[6::9]])
        prop_link = np.array([i for i in data_input[7::9]])
        prop_features = [i for i in data_input[8::9]]

        # create dataframes from the attribute lists:
        df = pd.DataFrame([prop_id, prop_size, prop_price, prop_address, prop_county, zip_code])
        df = df.T
        df.columns = ['id','size','price','address','county','zip']

        # property title and link text were not processed and required individual df:
        df_misc = pd.DataFrame([prop_title, prop_link])
        df_misc = df_misc.T
        df_misc.columns = ['title','link']

        # all dataframes concatenated to build master df: 
        df_county = pd.get_dummies(df['county'], drop_first = True, dtype = int)    # default is County of Bell
        df_features = pd.DataFrame(prop_features)
        df = pd.concat([df, df_features, df_county, df_misc], axis = 1)    

        return(df)