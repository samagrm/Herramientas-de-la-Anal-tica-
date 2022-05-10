#!/usr/bin/env python
# coding: utf-8

# Importa pandas.
# Lee el archivo .csv usando la función read_csv.
# Observa las primeras líneas usando la función head.
# Obtén diferentes combinaciones de columnas y datos.
# Revisa los datos obtenidos por la función  describe.
# Responde las preguntas de la sección anterior.
# 

# In[3]:


import pandas as pd
datos = pd.read_csv("avocado.csv")
datos.head()


# Obtén diferentes combinaciones de columnas y datos.

# In[12]:


datos.iloc[1:, 0:5]


# In[13]:


datos.iloc[1:, [1,3,6,7,9]]


# Revisa los datos obtenidos por la función  describe.

# In[14]:


df.describe()


# ¿Cuántos objetos hay?

# In[10]:


df = pd.DataFrame(datos)
print(df.count())


# ¿Cuál es el valor de la variable 2 del objeto 15?

# In[5]:


datos.iloc[15, 2]


# ¿Cuál es el mínimo y máximo de la variable 3?

# min:8.456000e+01
# max:6.250565e+07
# 
