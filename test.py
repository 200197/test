import pandas as pd
import numpy as np
import os
import glob

def splite_data(date):
    num = str(date)
    extension = 'xlsx'
    files = glob.glob('*.{}'.format(extension))
    files_xls = [f for f in files if f[-18:-12] == num]

    df = pd.DataFrame()
    for f in files_xls:
        data = pd.read_excel(f, index_col=0, engine='openpyxl')
        data['salesnumber'] = data['salesnumber'].str.replace(',', '').astype(np.float64)
        data['category'] = data['category'].str.replace("/", "")
        df = df.append(data)

    category = df['category'].unique()

    for i in category:
        outfilename = i + num + '.csv'
        df[df['category'] == i].to_csv(outfilename, encoding='utf-8-sig')

splite_data(202107)
