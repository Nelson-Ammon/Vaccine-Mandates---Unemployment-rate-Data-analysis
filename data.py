#%%
# import all packages 
import pandas as pd
import altair as alt
from altair_saver import save
import numpy as np
#%% # read in the data 
job_data = pd.read_csv("ststdsadata.csv")
vaccineDat = pd.read_csv("owid-covid-data.csv")
mandate = pd.read_csv("raw_data.csv")


#%%
# mandates ordered by state and position
###########################
mandate1= (mandate.sort_values(by= ['state','position']))
#%% 
# drop the text column
###########################
mandate2 = mandate1.drop('text',axis=1,inplace= False)
# mandates by state chart
bar = alt.Chart(mandate2).mark_point().encode(
    alt.Y('position',title="Mandates in place?"),
    alt.X('state' ,title="State"),
    color = alt.condition(
        alt.datum.position == 'Yes',
        alt.value('green'),
        alt.value('black')
    ),
)
bar 

#%%
# mandate numbers chart
##############################

Data = {'Position':['Yes','No','Prohibited'],
                'Value':[21,16,13]}
df = pd.DataFrame(Data)
print(df)
#%% 
# mandates by number chart
number_bar = alt.Chart(df).mark_bar().encode(
    alt.Y("Position:N", 
    title="Mandate of COVID Vaccine",
    sort='x'),
    alt.X("Value:Q", title = "Number Of States", scale = alt.Scale(domain=(0,24))),
    color= alt.condition(
        alt.datum.Position == "Yes",
        alt.value("green"),
        alt.value('red')
    )
)
number_bar
# number_bar.save("number_bar.png",scale_factor=2.0)
#%%
job_data.sort_values(by=['State_area','Year','percent_unemployed'])
new= job_data.filter(items=["FIPS Code","State_area","Year","Month","percent_unemployed"])
new.reset_index(drop=True)
new1 = new.rename(columns={'FIPS Code': 'fips_code','State_area':'state','Year':'year'})
#%%
# chart for cali
################
cali = new1[(new1.state == "California") & (new1.year >= 2016)]
cali.reset_index(drop=True,inplace=True)
cali['index']=cali.index

cali_chart = alt.Chart(cali).mark_line(point=False).encode(
    alt.X('index', axis=None),
    alt.Y('percent_unemployed',title="Percent Unemployed", scale= alt.Scale(domain=(1,18)))).properties(
        title = {
            "text": ["California Unemployment since 2016 - Present"],
            "subtitle": ["California COVID Mandate Status = REQUIRED, Required for all gov. jobs/ and in schools."]
        }
    )
    
line = alt.Chart(pd.DataFrame({'x': [50], 'y':[4.5]})).mark_point(point=True).encode(x='x',y='y', color=alt.value("red"))
line1 = alt.Chart(pd.DataFrame({'x': [12,24,36,48,60]})).mark_rule().encode(x='x', color=alt.condition(
    alt.datum.x >= 50,
    alt.value("red"),
    alt.value("green")
))
text = alt.Chart({'values':[{'x': 55, 'y': 17}]}).mark_text( 
    text='COVID Pandemic Hits the US', angle = 0 
).encode( 
    x='x:Q', y='y:Q' 
) 
year0 = alt.Chart({'values':[{'x': 11, 'y': 2}]}).mark_text( 
    text='2017', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
)
year2 = alt.Chart({'values':[{'x': 23, 'y': 2}]}).mark_text( 
    text='2018', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
)  
year3 = alt.Chart({'values':[{'x': 35, 'y': 2}]}).mark_text( 
    text='2019', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 
year4 = alt.Chart({'values':[{'x': 47, 'y': 2}]}).mark_text( 
    text='2020', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 
year5 = alt.Chart({'values':[{'x': 59, 'y': 2}]}).mark_text( 
    text='2021', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 

cali_final=(text + line + cali_chart + line1+ year0 + year2+year3+year4 + year5)

cali_final
# cali_final.save("cali_final.png",scale_factor=2.0)

# %%
#IDAHO 
##################
idaho = new1[(new1.state == "Idaho") & (new1.year >= 2016)]
idaho.reset_index(drop=True,inplace=True)
idaho['index']=idaho.index

idaho_chart = alt.Chart(idaho).mark_line().encode(
    alt.X('index', axis=None),
    alt.Y('percent_unemployed',title="Percent Unemployed", scale= alt.Scale(domain=(1,18)))
    ).properties(
        title = {
            "text": ["Idaho Unemployment since 2016 - Present"],
            "subtitle": ["Idaho COVID Mandate Status = PROHIBITED, for all gov. jobs/ and in schools."]
        }
    )
line = alt.Chart(pd.DataFrame({'x': [50], 'y':[2.8]})).mark_point(point=True).encode(x='x',y='y', color=alt.value("red"))

line1 = alt.Chart(pd.DataFrame({'x': [12,24,36,48,60]})).mark_rule().encode(x='x', color=alt.condition(
    alt.datum.x >= 50,
    alt.value("red"),
    alt.value("green")
))
text = alt.Chart({'values':[{'x': 55, 'y': 13}]}).mark_text( 
    text='COVID Pandemic Hits the US', angle = 0 
).encode( 
    x='x:Q', y='y:Q' 
) 
year0 = alt.Chart({'values':[{'x': 11, 'y': 1}]}).mark_text( 
    text='2017', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
)
year2 = alt.Chart({'values':[{'x': 23, 'y': 1}]}).mark_text( 
    text='2018', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
)  
year3 = alt.Chart({'values':[{'x': 35, 'y': 1}]}).mark_text( 
    text='2019', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 
year4 = alt.Chart({'values':[{'x': 47, 'y': 1}]}).mark_text( 
    text='2020', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 
year5 = alt.Chart({'values':[{'x': 59, 'y': 1}]}).mark_text( 
    text='2021', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 
idaho_final = (text + line + idaho_chart + line1+ year0 + year2+year3+year4 + year5)
idaho_final
# idaho_final.save("idaho_final.png")
#%%
york= new1[(new1.state == "New York") & (new1.year >= 2020) & (new1.Month == 4)]
tx= new1[(new1.state == "Texas") & (new1.year >= 2020)]
florida = new1[(new1.state == "Florida") & (new1.year >= 2020) & (new1.Month == 4)]
hawaii = new1[(new1.state == "Hawaii") & (new1.year >= 2020) & (new1.Month == 4)]

# %%
york = new1[(new1.state == "New York") & (new1.year >= 2016)]
york.reset_index(drop=True,inplace=True)
york['index']=york.index

york_chart = alt.Chart(york).mark_line().encode(
    alt.X('index', axis=None),
    alt.Y('percent_unemployed',title="Percent Unemployed", scale= alt.Scale(domain=(1,18)))).properties(
        title = {
            "text": ["New York Unemployment since 2016 - Present"],
            "subtitle": ["New York COVID Mandate Status = REQUIRED, for all gov. jobs/ and in schools."]
        }
    )
line = alt.Chart(pd.DataFrame({'x': [50], 'y':[4]})).mark_point(point=True).encode(x='x',y='y', color=alt.value("red"))

line1 = alt.Chart(pd.DataFrame({'x': [12,24,36,48,60]})).mark_rule().encode(x='x', color=alt.condition(
    alt.datum.x >= 50,
    alt.value("red"),
    alt.value("green")
))
text = alt.Chart({'values':[{'x': 55, 'y': 17}]}).mark_text( 
    text='COVID Pandemic Hits the US', angle = 0 
).encode( 
    x='x:Q', y='y:Q' 
) 
year0 = alt.Chart({'values':[{'x': 11, 'y': 1}]}).mark_text( 
    text='2017', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
)
year2 = alt.Chart({'values':[{'x': 23, 'y': 1}]}).mark_text( 
    text='2018', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
)  
year3 = alt.Chart({'values':[{'x': 35, 'y': 1}]}).mark_text( 
    text='2019', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 
year4 = alt.Chart({'values':[{'x': 47, 'y': 1}]}).mark_text( 
    text='2020', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 
year5 = alt.Chart({'values':[{'x': 59, 'y': 1}]}).mark_text( 
    text='2021', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 


york_final = (text + line + york_chart + line1+ year0 + year2+year3+year4 + year5)

york_final
# york_final.save("york_final.png")
# %%
tx = new1[(new1.state == "Texas") & (new1.year >= 2016)]
tx.reset_index(drop=True,inplace=True)
tx['index']=tx.index

tx_chart = alt.Chart(tx).mark_line().encode(
    alt.X('index', axis=None),
    alt.Y('percent_unemployed',title="Percent Unemployed", scale= alt.Scale(domain=(1,18)))).properties(
        title = {
            "text": ["Texas Unemployment since 2016 - Present"],
            "subtitle": ["Texas COVID Mandate Status = PROHIBITED, for all gov. jobs/ and in schools."]
        }
    )
line = alt.Chart(pd.DataFrame({'x': [49], 'y':[3.8]})).mark_point(point=True).encode(x='x',y='y', color=alt.value("red"))

line1 = alt.Chart(pd.DataFrame({'x': [12,24,36,48,60]})).mark_rule().encode(x='x', color=alt.condition(
    alt.datum.x >= 50,
    alt.value("red"),
    alt.value("green")
))
text = alt.Chart({'values':[{'x': 55, 'y': 17}]}).mark_text( 
    text='COVID Pandemic Hits the US', angle = 0 
).encode( 
    x='x:Q', y='y:Q' 
) 
year0 = alt.Chart({'values':[{'x': 11, 'y': 1}]}).mark_text( 
    text='2017', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
)
year2 = alt.Chart({'values':[{'x': 23, 'y': 1}]}).mark_text( 
    text='2018', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
)  
year3 = alt.Chart({'values':[{'x': 35, 'y': 1}]}).mark_text( 
    text='2019', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 
year4 = alt.Chart({'values':[{'x': 47, 'y': 1}]}).mark_text( 
    text='2020', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 
year5 = alt.Chart({'values':[{'x': 59, 'y': 1}]}).mark_text( 
    text='2021', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 


tx_chart_final = (text + line + tx_chart + line1+ year0 + year2+year3+year4 + year5)
tx_chart_final
# tx_chart_final.save("tx_chart_final.png")
#%%
florida = new1[(new1.state == "Florida") & (new1.year >= 2016)]
florida.reset_index(drop=True,inplace=True)
florida['index']=florida.index

florida_chart = alt.Chart(florida).mark_line().encode(
    alt.X('index', axis=None),
    alt.Y('percent_unemployed',title="Percent Unemployed", scale= alt.Scale(domain=(1,18)))).properties(
        title = {
            "text": ["Florida Unemployment since 2016 - Present"],
            "subtitle": ["Florida COVID Mandate Status = PROHIBITED, for all gov. jobs/ and in schools."]
        }
    )
line = alt.Chart(pd.DataFrame({'x': [49], 'y':[3.4]})).mark_point(point=True).encode(x='x',y='y', color=alt.value("red"))

line1 = alt.Chart(pd.DataFrame({'x': [12,24,36,48,60]})).mark_rule().encode(x='x', color=alt.condition(
    alt.datum.x >= 50,
    alt.value("red"),
    alt.value("green")
))
text = alt.Chart({'values':[{'x': 55, 'y': 17}]}).mark_text( 
    text='COVID Pandemic Hits the US', angle = 0 
).encode( 
    x='x:Q', y='y:Q' 
) 
year0 = alt.Chart({'values':[{'x': 11, 'y': 1}]}).mark_text( 
    text='2017', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
)
year2 = alt.Chart({'values':[{'x': 23, 'y': 1}]}).mark_text( 
    text='2018', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
)  
year3 = alt.Chart({'values':[{'x': 35, 'y': 1}]}).mark_text( 
    text='2019', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 
year4 = alt.Chart({'values':[{'x': 47, 'y': 1}]}).mark_text( 
    text='2020', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 
year5 = alt.Chart({'values':[{'x': 59, 'y': 1}]}).mark_text( 
    text='2021', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 

florida_chart_final = (text + line + florida_chart + line1+ year0 + year2+year3+year4 + year5)
florida_chart_final
# %%
hawaii = new1[(new1.state == "Hawaii") & (new1.year >= 2016)]
hawaii.reset_index(drop=True,inplace=True)
hawaii['index']=hawaii.index

hawaii_chart = alt.Chart(hawaii).mark_line().encode(
    alt.X('index', axis=None),
    alt.Y('percent_unemployed',title="Percent Unemployed", scale= alt.Scale(domain=(1,23)))).properties(
        title = {
            "text": ["Hawaii Unemployment since 2016 - Present"],
            "subtitle": ["Hawaii COVID Mandate Status = REQUIRED, for all gov. jobs/ and in schools."]
        }
    )
line = alt.Chart(pd.DataFrame({'x': [50], 'y':[2.1]})).mark_point(point=True).encode(x='x',y='y', color=alt.value("red"))

line1 = alt.Chart(pd.DataFrame({'x': [12,24,36,48,60]})).mark_rule().encode(x='x', color=alt.condition(
    alt.datum.x >= 50,
    alt.value("red"),
    alt.value("green")
))
text = alt.Chart({'values':[{'x': 55, 'y': 23}]}).mark_text( 
    text='COVID Pandemic Hits the US', angle = 0 
).encode( 
    x='x:Q', y='y:Q' 
) 
year0 = alt.Chart({'values':[{'x': 11, 'y': 1}]}).mark_text( 
    text='2017', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
)
year2 = alt.Chart({'values':[{'x': 23, 'y': 1}]}).mark_text( 
    text='2018', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
)  
year3 = alt.Chart({'values':[{'x': 35, 'y': 1}]}).mark_text( 
    text='2019', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 
year4 = alt.Chart({'values':[{'x': 47, 'y': 1}]}).mark_text( 
    text='2020', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 
year5 = alt.Chart({'values':[{'x': 59, 'y': 1}]}).mark_text( 
    text='2021', angle = 270
).encode( 
    x='x:Q', y='y:Q' 
) 


hawaii_chart_final = (text + line + hawaii_chart + line1+ year0 + year2+year3+year4 + year5)
hawaii_chart_final
# %%
big = new1(new1.state == "Hawaii", new1.state == "Texas") & (new1.year >= 2016)
big.reset_index(drop=True,inplace=True)
big['index']=big.index
big_chart =alt.Chart(big).mark_line().encode(
    alt.X('index', axis=None),
    alt.Y('percent_unemployed',title="Percent Unemployed", scale= alt.Scale(domain=(1,23)))).properties(
        title = {
            "text": ["Hawaii Unemployment since 2016 - Present"],
            "subtitle": ["Hawaii COVID Mandate Status = REQUIRED, for all gov. jobs/ and in schools."]
        }
    )
# %%
