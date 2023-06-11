#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

#membaca/import database
db = pd.read_csv("data bank.csv")

#jenis diagram
plt.scatter(db['age'], db['balance'])

#judul scatter plot
plt.title("Data Bank")

#menentukan sumbu x dan y
plt.xlabel('age')
plt.ylabel('balance')

#menampilkan diagram
plt.show


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

#membaca/import database
db = pd.read_csv("data bank.csv")

#penentuan jenis diagram
plt.plot(db['age'])
plt.plot(db['balance'])


#judul scatter plot
plt.title("Data Bank")

#menentukan sumbu x dan y
plt.xlabel('age')
plt.ylabel('balance')

#menampilkan diagram
plt.show


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

#membaca/import database
db = pd.read_csv("data bank.csv")

#jenis diagram
plt.bar(db['age'], db['balance'])

#judul scatter plot
plt.title("Data Bank")

#menentukan sumbu x dan y
plt.xlabel('age')
plt.ylabel('balance')

#menampilkan diagram
plt.show


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

#membaca/import database
db = pd.read_csv("data bank.csv")

#jenis diagram
plt.hist(db['age'])

#judul scatter plot
plt.title("Data Bank")

#menampilkan diagram
plt.show


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt

#membaca/import database
db = pd.read_csv("data bank.csv")

#jenis diagram
sales = ['age','balance']
datasales = [25, 15]
plt.pie(datasales, labels=sales)

#judul scatter plot
plt.title("Data Bank")

#menampilkan diagram
plt.show


# In[ ]:




