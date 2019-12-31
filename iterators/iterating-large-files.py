""" Using iterators to load large files in chunks
"""
import pandas as pd

# ************* Summing up the values of a column *************
result = [] # initializing a list

for chunk in pd.read_csv('imdb-top-250.csv', chunksize=50):
    result.append(sum(chunk['rank']))
total = sum(result)
print(total)

# OR YET:
total = 0
for chunk in pd.read_csv('imdb-top-250.csv', chunksize=50):
    total += sum(chunk['rank'])
print(total)


# ************* Counting the number of films for each release year *************
count = {}  # initializing a dictionary

# Iterating the file
for chunk in pd.read_csv('imdb-top-250.csv', chunksize=50):

    # Iterating over a column in the dataframe chunk
    for entry in chunk['release_year']:
        if entry in count.keys():
            count[entry] += 1
        else:
            count[entry] = 1

# Print dictionary
print(count)


# ************* Function to count number of occurrences of values in a given column *************
def count_values(csv_file, c_size, colname):
    """Return a dictionary with number of occurrences of values for a column."""
    
    count = {}

    # Iterating csv_file
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterating over colname in the dataframe chunk
        for entry in chunk[colname]:
            if entry in count.keys():
                count[entry] += 1
            else:
                count[entry] = 1

    return count

result = count_values('imdb-top-250.csv', 50, 'rank')
print(result)