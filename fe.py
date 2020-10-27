import pandas as pd
import numpy as np

fatal_encounters_df = pd.read_csv('fatal-encounters_2.csv')

# Drop unwanted columns
fatal_encounters_df = fatal_encounters_df.drop(
    ["Unique ID",
     "Subject's name",
     "URL of image of deceased",
     "Location of injury (address)",
     "Full Address",
     "A brief description of the circumstances surrounding the death",
     "Dispositions/Exclusions INTERNAL USE, NOT FOR ANALYSIS",
     "Link to news article or photo of official document",
     "Video",
     "Brief description",
     "Unique ID formula",
     "Unique identifier (redundant)",
     "Date (Year)",
     "URL of image (PLS NO HOTLINKS)",
     "Unnamed: 24",
     "Unnamed: 25",
     "Supporting document link",
     "Location of death (zip code)",
     "Imputation probability",
     "Location of death (city)",
     "Location of death (county)",
     "Race",
     "Latitude",
     "Longitude",
     "Name"],
     axis='columns', errors='ignore')

# Rename
fatal_encounters_df.rename(columns={
    "Subject's age": "Age",
    "Subject's gender": "Gender",
    "Race with imputations": "Race",
    "Date of injury resulting in death (month/day/year)": "Date",
    "Intended use of force (Developing)": "Intended use of force",
    "Location of death (state)": "State",
    "Foreknowledge of mental illness? INTERNAL USE, NOT FOR ANALYSIS": "Mental illness"
}, inplace=True)

# Drop missing
fatal_encounters_df.dropna(inplace=True)

# Age
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '3 days', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '2 months', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '3 months', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '4 months', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '6 months', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '7 months', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '8 months', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '9 months', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '10 months', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '18 months', '1', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '55.', '55', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '20s', '25', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '30s', '35', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '40s', '45', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '50s', '55', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '60s', '65', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '70s', '75', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '18-25', '20', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '40-50', '45', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '46/53', '50', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '20s-30s', '30', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '.25', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '0.25', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '.8', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '0.8', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '.5', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '.17', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '.75', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '.66', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '.58', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '.33', '0', inplace=True)
fatal_encounters_df['Age'].mask(fatal_encounters_df['Age'] == '.08', '0', inplace=True)

fatal_encounters_df.Age = fatal_encounters_df.Age.astype('int')
fatal_encounters_df = fatal_encounters_df[fatal_encounters_df['Age'] < 100]

age_bins = [-1,4,9,14,19,24,29,34,39,44,49,54,59,64,69,74,79,84,89,94,99]
age_labels = ['00-04','05-09', '10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85-89','90-94','95-99']
fatal_encounters_df['Age Group'] = pd.cut(fatal_encounters_df.Age, age_bins, labels=age_labels)

# # Gender
fatal_encounters_df = fatal_encounters_df[fatal_encounters_df['Gender'] != 'Transgender']

# Race
fatal_encounters_df['Race'].mask(fatal_encounters_df['Race'] == 'Asian/Pacific Islander', 'Other', inplace=True)
fatal_encounters_df['Race'].mask(fatal_encounters_df['Race'] == 'Middle Eastern', 'Other', inplace=True)
fatal_encounters_df['Race'].mask(fatal_encounters_df['Race'] == 'Native American/Alaskan', 'Other', inplace=True)
fatal_encounters_df['Race'].mask(fatal_encounters_df['Race'] == 'Race unspecified', 'Other', inplace=True)

# Date
fatal_encounters_df[['Month', 'Day', 'Year']] = fatal_encounters_df.Date.str.split('/', expand=True)
fatal_encounters_df.Date = fatal_encounters_df[['Year','Month']].apply(lambda x: '-'.join(x), axis=1)
fatal_encounters_df = fatal_encounters_df[fatal_encounters_df['Year'] != '2020']
# fatal_encounters_df['Month'].mask(fatal_encounters_df['Month'] == '01', 'Jan', inplace=True)
# fatal_encounters_df['Month'].mask(fatal_encounters_df['Month'] == '02', 'Feb', inplace=True)
# fatal_encounters_df['Month'].mask(fatal_encounters_df['Month'] == '03', 'Mar', inplace=True)
# fatal_encounters_df['Month'].mask(fatal_encounters_df['Month'] == '04', 'Apr', inplace=True)
# fatal_encounters_df['Month'].mask(fatal_encounters_df['Month'] == '05', 'May', inplace=True)
# fatal_encounters_df['Month'].mask(fatal_encounters_df['Month'] == '06', 'Jun', inplace=True)
# fatal_encounters_df['Month'].mask(fatal_encounters_df['Month'] == '07', 'Jul', inplace=True)
# fatal_encounters_df['Month'].mask(fatal_encounters_df['Month'] == '08', 'Aug', inplace=True)
# fatal_encounters_df['Month'].mask(fatal_encounters_df['Month'] == '09', 'Sep', inplace=True)
# fatal_encounters_df['Month'].mask(fatal_encounters_df['Month'] == '10', 'Oct', inplace=True)
# fatal_encounters_df['Month'].mask(fatal_encounters_df['Month'] == '11', 'Nov', inplace=True)
# fatal_encounters_df['Month'].mask(fatal_encounters_df['Month'] == '12', 'Dec', inplace=True)

# States
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'AL', 'Alabama', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'AK', 'Alaska', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'AZ', 'Arizona', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'AR', 'Arkansas', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'CA', 'California', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'CO', 'Colorado', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'CT', 'Connecticut', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'DE', 'Delaware', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'DC', 'District of Columbia', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'FL', 'Florida', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'GA', 'Georgia', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'HI', 'Hawaii', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'ID', 'Idaho', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'IL', 'Illinois', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'IN', 'Indiana', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'IA', 'Iowa', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'KS', 'Kansas', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'KY', 'Kentucky', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'LA', 'Louisiana', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'ME', 'Maine', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'MD', 'Maryland', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'MA', 'Massachusetts', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'MI', 'Michigan', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'MN', 'Minnesota', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'MS', 'Mississippi', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'MO', 'Missouri', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'MT', 'Montana', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'NE', 'Nebraska', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'NV', 'Nevada', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'NH', 'New Hampshire', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'NJ', 'New Jersey', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'NM', 'New Mexico', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'NY', 'New York', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'NC', 'North Carolina', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'ND', 'North Dakota', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'OH', 'Ohio', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'OK', 'Oklahoma', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'OR', 'Oregon', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'PA', 'Pennsylvania', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'RI', 'Rhode Island', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'SC', 'South Carolina', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'SD', 'South Dakota', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'TN', 'Tennessee', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'TX', 'Texas', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'UT', 'Utah', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'VT', 'Vermont', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'VA', 'Virginia', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'WA', 'Washington', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'WV', 'West Virginia', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'WI', 'Wisconsin', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'WY', 'Wyoming', inplace=True)
fatal_encounters_df['State'].mask(fatal_encounters_df['State'] == 'AL', 'Alabama', inplace=True)

fatal_encounters_df['Intended use of force'].mask(fatal_encounters_df['Intended use of force'] == 'Vehic/Purs', 'Vehicle/Pursuit', inplace=True)
fatal_encounters_df['Intended use of force'].mask(fatal_encounters_df['Intended use of force'] == 'Vehicle', 'Vehicle/Pursuit', inplace=True)
fatal_encounters_df['Intended use of force'].mask(fatal_encounters_df['Intended use of force'] == 'Pursuit', 'Vehicle/Pursuit', inplace=True)

fatal_encounters_df.drop(columns=['Date', 'Agency or agencies involved', 'Day'], inplace=True)

fatal_encounters_df.to_csv('fatal.csv', index=False)