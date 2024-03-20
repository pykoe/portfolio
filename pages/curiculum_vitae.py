import streamlit as st

st.set_page_config(layout="wide")

# Three columns with different widths
col1, col2 = st.columns([2,1])
# col1 is wider

# Using 'with' notation:
with col1:
    st.title('Pierre-Yves Koenig')
    st.subheader('Senior Datascientis')

    st.markdown('''
# :blue[Experience]
### **Freelance**, Black River Mauritius — *Senior Data Scientist*
*:gray[September 2023 - Present]* 
- EdgeRyders - Network Scientist - data analysis and visualization
    ''')

    st.markdown('''
### **Airbus**, Toulouse — *Senior Data Scientist*  \n:gray[*February 2016 - September 2023*]  
- **Solution Innovator Manager** in Sustainable Operation Squad - assessment of the feasibility of initiative in term of benedict for the planet (CO2 and ressources)
- Life cycle assessment of end to end digital tool (SPM)
- **Analyze airline network**, recompute and optimize flight planning in case of disruption (**constraint programming** ORtool) to minimize airline loss (cost, impact on passenger) based on AWS  (S3, RDS, EKS)
- Full stack Predictive Maintenance and **Anomaly detection** of avionic systems based on manufacturing and in service data - **kafka** (data feeding), **oozie** (scheduler), **HBASE** (time serie), **mongo** (event), **spark** (computation), **grafana** (visu and alerting)
- **Fraud detection** based on access log analysis, text documents  and graph analysis - **Failure detection** on production chain
    '
### **LaetiPaniers**, Toulouse — *CTO and Full stack developer*  \n:gray[*September 2018 - September 2023*]  
Full stack development backend, frontend (Spring), hosting, deployment and data analytics tools (logs). laetipaniers.fr is an  ecommerce platform dedicated to seasonal and local products delivered by bicycle.
    
### **Valtech / Alyotech**, Toulouse— *Data Scientist*  
:gray[*April 2010 -  February 2016*]  
- **Sanofi**, molecule huge network analysis for drugs discovery (similarity search, clustering, interactive visualization)
- Insurances, statistical analysis, client segmentation, recommendation engine based on structured and unstructured data (web features, connection log, text)
- Valtech training, Big Data formation (Hadoop ecosystem courses and practice), Biological Data Visualization  techniques explain and implements with d3.js
  
# :blue[Education]
  
### **University of Montpellier** — PhD Computer Science  
:gray[Septembre 2006 - October 2009]  
Information Visualization : paradigmes of multiscale navigation and “focus+context” approaches (http://pykoenig.free.fr/lirmm/).
    ''')

with col2:
    st.markdown('''
### :blue[CONTACT]
Black River, Mauritius  
+230 55 07 26 88  
pykoenig@gmail.com  
linkedin

### :blue[SKILLS]
**Python** (Keras, PyTorch, TenserFlow, Scikit-learn, Pandas, NumPy, Spark)  
Database SQL and NoSQL  
Feature extraction (Opencv)  
ML algorithms  
Data Visualization (Seaborn, MatplotLib, d3.js)  
Data Platform (Hadoop, Knime, AWS Cloud, Foundry, DataIku)  
Web Application (back end: Java Spring MVC, front end: jsp, react,  js typescript redux)  
LCA study

### :blue[EXTRAS]

Dataviz http://pykoenig.free.fr/dataviz/Interactive visualization of ontology (open data) for geographical data

Award Traffic and Flitter Challenge  
Innovative Visualization and Excellent Description Representation of Uncertainty in Rules & in Visualization

### :blue[LANGUAGES]
English -  fluence  
French - native speaker  
Mauritian creol - fluence

### :blue[HOBBIES]
Guitar, Amateur Oenologist

''')