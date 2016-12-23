# Liam Byrne
# Data 602 Final
# Data load file to aggregate housing sales for all 5 boroughs in NYC
# for the years 2008 - 2015

# xldr module required in pd.read_excel call
import pandas as pd

# URL structure for GitHub data
url = ""
url_base = "https://github.com/Liam-O/Data602/blob/master/FinalProject/data/"
url_seed = ""
url_tail = ".xls?raw=true"

# pd.read variables
col_sub = [0,1,2,11,12,13,15,17,18,19]
head_row = 0

# variables for .xls file name structure
boroughs = ["manhattan", "bronx", "brooklyn", "queens", "statenisland"]
years = range(2008,2015)

# temp and properties data frame
tmp_df = pd.DataFrame()
prop_df = pd.DataFrame()

# loop through all files in repo (40) and append to properties data frame
for y in years:
    for b in boroughs:
        url_seed = "{}_{}".format(y,b)
        url = url_base + url_seed + url_tail
        
        if y < 2011:
            head_row = 3
        else:
            head_row = 4
        
        tmp_df = pd.read_excel(url, header = head_row, parse_cols = col_sub)
        tmp_df['year'] = [y]*len(tmp_df.index)
        # remove \n in some header files
        tmp_df.columns = tmp_df.columns.str.replace('\n', '')
        tmp_df.columns = tmp_df.columns.str.replace('\s+', '_')
        prop_df = prop_df.append(tmp_df, ignore_index = True)
        
prop_df.to_csv("nyc_HousingSales")