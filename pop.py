import pandas as pd
import numpy as np

df = pd.read_csv('population.csv')

df = df[df.YEAR == 12]

df = df.groupby(by=['STNAME', 'AGEGRP']).sum().reset_index()

df['H_MALE'] = df['H_MALE'] + df['H_FEMALE']
df['NHWA_MALE'] = df['NHWA_MALE'] + df['NHWA_FEMALE']
df['NHBA_MALE'] = df['NHBA_MALE'] + df['NHBA_FEMALE']
df['Other'] = df['NHIA_MALE'] + df['NHIA_FEMALE'] + df['NHAA_MALE'] + df['NHAA_FEMALE'] + df['NHNA_MALE'] +df['NHNA_FEMALE'] +df['NHTOM_MALE']

df.drop(['SUMLEV',
    'STATE',
    'COUNTY',
    'WA_MALE',
    'WA_FEMALE',
    'BA_MALE',
    'BA_FEMALE',
    'IA_MALE',
    'IA_FEMALE',
    'AA_MALE',
    'AA_FEMALE',
    'NA_MALE',
    'NA_FEMALE',
    'TOM_MALE',
    'TOM_FEMALE',
    'WAC_MALE',
    'WAC_FEMALE',
    'BAC_MALE',
    'BAC_FEMALE',
    'IAC_MALE',
    'IAC_FEMALE',
    'AAC_MALE',
    'AAC_FEMALE',
    'NAC_MALE',
    'NAC_FEMALE',
    'HWA_MALE',
    'HWA_FEMALE',
    'HBA_MALE',
    'HBA_FEMALE',
    'HIA_MALE',
    'HIA_FEMALE',
    'HAA_MALE',
    'HAA_FEMALE',
    'HNA_MALE',
    'HNA_FEMALE',
    'HTOM_MALE',
    'HTOM_FEMALE',
    'HWAC_MALE',
    'HWAC_FEMALE',
    'HBAC_MALE',
    'HBAC_FEMALE',
    'HIAC_MALE',
    'HIAC_FEMALE',
    'HAAC_MALE',
    'HAAC_FEMALE',
    'HNAC_MALE',
    'HNAC_FEMALE',
    'NHTOM_FEMALE',
    'NHWAC_MALE',
    'NHWAC_FEMALE',
    'NHBAC_MALE',
    'NHBAC_FEMALE',
    'NHIAC_MALE',
    'NHIAC_FEMALE',
    'NHAAC_MALE',
    'NHAAC_FEMALE',
    'NHNAC_MALE',
    'NHNAC_FEMALE',
    'NH_MALE',
    'NH_FEMALE',
    'H_FEMALE',
    'NHWA_FEMALE',
    'NHBA_FEMALE',
    'NHIA_MALE',
    'NHIA_FEMALE',
    'NHAA_MALE',
    'NHAA_FEMALE',
    'NHNA_MALE',
    'NHNA_FEMALE',
    'NHTOM_MALE'], axis='columns', inplace=True)

df['AGEGRP'].mask(df['AGEGRP'] == 1, '0-4', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 2, '5-9', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 3, '10-14', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 4, '15-19', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 5, '20-24', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 6, '25-29', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 7, '30-34', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 8, '35-39', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 9, '40-44', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 10, '45-49', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 11, '50-54', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 12, '55-59', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 13, '60-64', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 14, '65-69', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 15, '70-74', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 16, '75-79', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 17, '80-84', inplace=True)
df['AGEGRP'].mask(df['AGEGRP'] == 18, '85+', inplace=True)

df = df[df['AGEGRP'] != 0]

df.rename(columns={
    "STNAME": 'State',
    "YEAR": 'Year',
    "AGEGRP": 'Age',
    "TOT_POP": "Total",
    "TOT_MALE": "Male",
    "TOT_FEMALE": "Female",
    "H_MALE": "Hispanic/Latino",
    "NHWA_MALE": "European-American/White",
    "NHBA_MALE": "African-American/Black"
}, inplace=True)

df.to_csv('pop.csv', index=False)
