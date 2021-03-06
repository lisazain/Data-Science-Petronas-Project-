import streamlit as st
import pandas as pd
import plotly.express as px


header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()

global df

with header:
    st.title('Covid-19 in Malaysia')

with dataset:
    st.header('Covid-19 cases by state')

    covid_19= pd.read_csv('https://raw.githubusercontent.com/lisazain/Data-Science-Petronas-Project-/main/Covid-19.csv')
    st.write(covid_19)

# confirmed cases chart (bubble plot)
    
    cases = pd.DataFrame(covid_19.groupby('Malaysia')['Cases'].sum().nlargest(10).sort_values(ascending = False))        
    fig = px.bar(cases, x = cases.index, y = 'Cases', height = 600, color = cases.index, title = 'Confirmed Cases in state',
    color_continuous_scale = px.colors.sequential.Viridis)
    st.write(fig)
    
   
# deaths chart (h-Bar plot)

death = pd.DataFrame(covid_19.groupby('Malaysia')['Death'].sum().nlargest(10).sort_values(ascending = True))
fig2 = px.bar(death, x = 'Death', y = death.index, height = 600, color = 'Death', orientation = 'h',
color_continuous_scale = ['deepskyblue','red'], title = 'Death Cases in States')
st.write(fig2)


# recovery chart (Bar plot)

recovery = pd.DataFrame(covid_19.groupby('Malaysia')['Recovery'].sum().nlargest(10).sort_values(ascending = False))
fig3 = px.bar(recovery, x = recovery.index, y = 'Recovery', height = 600, color = 'Recovery',
             title = 'Recovered Cases in States', color_continuous_scale = px.colors.sequential.Viridis)
st.write(fig3)

# hospital admission

hospital_admission = pd.DataFrame(covid_19.groupby('Malaysia')['Admitted'].sum().nlargest(10).sort_values(ascending = True))
fig4 = px.bar(hospital_admission, x = 'Admitted', y = hospital_admission.index, height = 600, color = 'Admitted', orientation = 'h',
             color_continuous_scale = ['paleturquoise','blue'], title = 'Hospital Admission')
st.write(fig4)
