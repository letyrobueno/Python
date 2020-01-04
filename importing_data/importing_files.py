""" Flat files consist of table data, i.e., rows where each row is a record.
    Record: row of fields or attributes
    Column: feature or attribute
    Files extension: .csv or .txt, where delimiters are commas or tabs
"""


# ****************** TXT: Importing .txt files ******************
print('\nBasic operations in a file')

# Open a file
file = open('file_example.txt', mode='r') # 'r' = for reading; 'w' = for writing

# Print all the content of the file
print(file.read())

# Check if the file is closed
print(file.closed)

file.close()


# ****************** TXT: Using context manager 'with open()' ******************
print("\nUsing context manager 'with open()'")
# Read & print the first 3 lines
with open('file_example.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

# ****************** TXT: Using NumPy to import numerical data: function loadtxt() ******************
print('\nUsing NumPy to import numerical data: function loadtxt()')
import numpy as np

# Dataset source: http://yann.lecun.com/exdb/mnist/
filename = 'MNIST.txt'

# delimiter can be ',' or '\t'; skiprows refers to skip some rows (if there is a header, for example); 
# usecols refers to take just columns 0 and 2; dtype=str can be used if we want data as string type
data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0, 2])
# print(data)


# ****************** CSV: Using NumPy to import mixed type data: function genfromtxt() ******************
print('\nUsing NumPy to import numerical data: function genfromtxt()')
import numpy as np
filename = 'titanic.csv'

# delimiter can be ',' or '\t'; dtype=None to handle with different type structures (string, int, etc)
# names=True indicates there is a header
# Because of different types, data is an object called a structured array
data = np.genfromtxt(filename, delimiter=',', names=True, dtype=None, encoding=None)
# print(data['Age'])

# ****************** CSV: Using NumPy to import mixed type data: function recfromcsv() ******************
print('\nUsing NumPy to import numerical data: function recfromcsv()')
import numpy as np
filename = 'titanic.csv'

# Default parameters: delimiter = ','; dtype = None; names = True
data = np.recfromcsv(filename, encoding=None)
# print(data)


# ****************** CSV: Using Pandas to import mixed type data ******************
# Standard and best practice in DS: use Pandas to import flat files as dataframes.
print('\nCSV: Using Pandas to import mixed type data')
import pandas as pd

filename = 'titanic.csv'
data = pd.read_csv(filename)
print(data.head())

# Converting data to a NumPy array
data_array = data.values


# ****************** Pickled files ******************
print('\nPickled files')
import pickle

with open('pickled_file.pkl', 'rb') as file:
    data = pickle.load(file)
# print(data)


# ****************** Excel spreadsheets ******************
print('\nExcel spreadsheets')
import pandas as pd

# Dataset source: https://www.prio.org/Data/Armed-Conflict/Battle-Deaths/The-Battle-Deaths-Dataset-version-30/
file = 'battledeath.xlsx'
data = pd.ExcelFile(file)

# List the names of the sheets
print(data.sheet_names)

# Choosing a sheet
df1 = data.parse('2002') # either by its name
df2 = data.parse(0) # or by its index


# ****************** SAS files (SAS: Statistical Analysis System) ******************
# SAS files are especially common in business analytics and biostatistics
print('\nSAS files (Statistical Analysis System)')
import pandas as pd
import matplotlib.pyplot as plt
from sas7bdat import SAS7BDAT

with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

print(df_sas.head())
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
# plt.show()

# ****************** Stata files (Stata: "Statistics" + "data") ******************
# Stata files are especially common in academic social sciences research, such as economics and epidemiology
print('\nStata files (Stata: Statistics + data)')
import pandas as pd
import matplotlib.pyplot as plt

# Dataset source: http://www.principlesofeconometrics.com/sas/
data = pd.read_stata('disarea.dta')

print(data.head())

pd.DataFrame.hist(data[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
# plt.show()

# ****************** HDF5 files (HDF5: Hierarchical Data Format version 5) ******************
# Standard for storing large quantities of numerical data (giga, tera or exabytes)
print('\nHDF5 files (HDF5: Hierarchical Data Format version 5)')
import h5py

# Dataset source: https://losc.ligo.org/events/GW150914/
filename = 'L-L1_LOSC_4_V1-1126259446-32.hdf5'
data = h5py.File(filename, 'r') # 'r' = reading mode

print('\nPrinting the data.keys() of the HDF5 file:')
for key in data.keys():
    print(key)

print('\nPrinting the data[meta].keys() of the HDF5 file:')
for key in data['strain'].keys():
    print(key)

# ****************** Matlab (short for Matrix Laboratory) ******************
# Powerful linear algebra and matrix capabilities
print('\nMatlab (short for Matrix Laboratory)')
import scipy.io

# Dataset source: https://www.mcb.ucdavis.edu/faculty-labs/albeck/workshop.htm
filename = 'ja_data2.mat'
mat = scipy.io.loadmat(filename)
print(mat.keys())
print(type(mat['CYratioCyt']))

data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
# plt.show()


# ****************** SQL (Structured Query Language) ******************
# Based on relational model of data; first described by Edgar Codd.
print('\nSQL (Structured Query Language)')

from sqlalchemy import create_engine
import pandas as pd

# Database source: https://github.com/lerocha/chinook-database
engine = create_engine('sqlite:///Chinook.sqlite')

# Discovering the table names inside the database
table_names = engine.table_names()
print(table_names)

# Connecting to the database
con = engine.connect()
rs = con.execute("SELECT * FROM Genre")
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys()
con.close()

# print(df.head())

# Using engine in context manager (better because we don't need to remember to close the connection):
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Genre")
    df = pd.DataFrame(rs.fetchmany(size=5))
    df.columns = rs.keys()

print(df.head())


# Another way using Pandas and one single line:
print("Another way using Pandas and one single line:")
engine = create_engine('sqlite:///Chinook.sqlite')

df = pd.read_sql_query("SELECT * FROM Genre", engine)

print(df.head())