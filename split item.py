import pandas as pd
import numpy as np
import os
import glob

outdir = 'C:/Users/hhng/Desktop/New folder/split item'

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
        path = os.path.join(outdir, outfilename)
        df[df['category'] == i].to_csv(path, encoding='utf-8-sig')

    print(category)

splite_data(202107)
splite_data(202108)
splite_data(202109)

