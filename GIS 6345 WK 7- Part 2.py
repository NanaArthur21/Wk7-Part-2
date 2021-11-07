#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


with open('some.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print row


# In[3]:


with open('some.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)


# In[4]:


import csv


# In[5]:


with open('some.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)


# In[6]:


import csv
from shapely.geometry import Point
with open('some.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        point = Point(float(row['lon']), float(row['lat']))


# In[7]:


import csv


# In[8]:


from shapely.geometry import Point
with open('some.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        point = Point(float(row['lon']), float(row['lat']))


# In[9]:


from shapely.geometry import Point
with open('some.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        point = Point(float(row['lon']), float(row['lat']))


# In[10]:


from shapely.geometry import Point
with open('some.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        point = Point(float(row['lon']), float(row['lat']))


# In[1]:


import csv


# In[2]:


from shapely.geometry import Point
with open('some.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        point = Point(float(row['lon']), float(row['lat']))


# In[3]:


$ pip install shapely


# In[4]:


pip install Shapely


# In[1]:


import csv


# In[2]:


from shapely.geometry import Point
with open('some.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        point = Point(float(row['lon']), float(row['lat']))


# In[3]:


from shapely.geometry import Point
with open('some.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        point = Point(float(row['lon']), float(row['lat']))


# In[4]:


from shapely.geometry import Point
with open('some.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        point = Point(float(row['Lon']), float(row['Lat']))


# In[5]:


import csv


# In[6]:


from shapely.geometry import Point, mapping


# In[7]:


pip install Fiona


# In[8]:


from fiona import collection


# In[9]:


pip install Fiona


# In[1]:


from fiona import collection


# In[2]:


pip install Fiona


# In[3]:


conda install -c conda-forge fiona


# In[1]:


import csv


# In[2]:


from shapely.geometry import Point, mapping


# In[3]:


from fiona import collection


# In[4]:


schema = { 'geometry': 'Point', 'properties': { 'name': 'str' } }
with collection("some.shp", "w", "ESRI Shapefile", schema) as output:
    with open('some.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['Lon']), float(row['Lat']))
            output.write({'properties': {'name': row['name']},'geometry': mapping(point)})


# In[5]:


schema = { 'geometry': 'Point', 'properties': { 'name': 'str' } }
with collection("some.shp", "w", "ESRI Shapefile", schema) as output:
    with open('some.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['Lon']), float(row['Lat']))
            output.write({'properties': {'Name': row['Name']},'geometry': mapping(point)})


# In[6]:


schema = { 'geometry': 'Point', 'properties': { 'name': 'str' } }
with collection("some.shp", "w", "ESRI Shapefile", schema) as output:
    with open('some.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['Lon']), float(row['Lat']))
            output.write({'properties': {'name': row['Name']},'geometry': mapping(point)})


# In[7]:


schema = { 'geometry': 'Point', 'properties': { 'name': 'str' } }


# In[8]:


with collection("some.shp", "w", "ESRI Shapefile", schema) as output:
    with open('some.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['Lon']), float(row['Lat']))
            output.write({'properties': {'name': row['Name']},'geometry': mapping(point)})


# In[9]:


import csv


# In[10]:


from shapely.geometry import Point, mapping


# In[11]:


from fiona import collection


# In[12]:


schema = { 'geometry': 'Point', 'properties': { 'name': 'str' } }


# In[13]:


with collection(
    "some.shp", "w", "ESRI Shapefile", schema) as output:
    with open('some.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['Lon']), float(row['Lat']))
            output.write({
                'properties': {
                    'name': row['Name']
                },
                'geometry': mapping(point)
            })


# In[14]:


with collection(
    "some.shp", "w", "ESRI Shapefile", schema) as output:
    with open('some.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['Lon']), float(row['Lat']))
            output.write({
                'properties': {
                    'name': row['name']
                },
                'geometry': mapping(point)
            })


# In[15]:


import csv


# In[16]:


with open('some.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print row


# In[17]:


with open('some.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)


# In[18]:


with open('some.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)


# In[19]:


import csv


# In[20]:


from shapely.geometry import Point


# In[21]:


with open('some.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        point = Point(float(row['Lon']), float(row['Lat']))


# In[22]:


import csv


# In[23]:


from shapely.geometry import Point, mapping


# In[24]:


from fiona import collection


# In[25]:


schema = { 'geometry': 'Point', 'properties': { 'name': 'str' } }


# In[26]:


with collection(
    "some.shp", "w", "ESRI Shapefile", schema) as output:
    with open('some.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['Lon']), float(row['Lat']))
            output.write({
                'properties': {
                    'name': row['name']
                },
                'geometry': mapping(point)


# In[27]:


with collection(
    "some.shp", "w", "ESRI Shapefile", schema) as output:
    with open('some.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['Lon']), float(row['Lat']))
            output.write({
                'properties': {
                    'name': row['Name']
                },
                'geometry': mapping(point)


# In[29]:


with collection(
    "some.shp", "w", "ESRI Shapefile", schema) as output:
    with open('some.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['Lon']), float(row['Lat']))
            output.write({
                'properties': {
                    'name': row['Name']
                },
                'geometry': mapping(point)
            })


# In[ ]:




