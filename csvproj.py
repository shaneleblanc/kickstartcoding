#   street,city,zip,state,beds,baths,sq__ft,type,sale_date,price,latitude,longitude
import pandas as pd
import statistics
datafile = pd.read_csv("/home/shane/projects/kickstartcoding/sac_realestate.csv")

def data_cruncher(pandas_datafile):
    df = pandas_datafile
    cols = ['beds', 'sq__ft', 'baths', 'price']
    crunched_data = { 'beds': {'median': statistics.median(df.beds), 'mean': statistics.mean(df.beds), 'mode': statistics.mode(df.beds)},
                    'baths': {'median': statistics.median(df.baths), 'mean': statistics.mean(df.baths), 'mode': statistics.mode(df.baths)},
                     'sq__ft': {'median': statistics.median(df.sq__ft), 'mean': statistics.mean(df.sq__ft), 'mode': statistics.mode(df.sq__ft)},
                     'price': {'median': statistics.median(df.price), 'mean': statistics.mean(df.price), 'mode': statistics.mode(df.price)}}

    return crunched_data
print(data_cruncher(datafile))

def writer(data, filename):
    columns = list(data)
    new_entry = []
    for col in columns:
        user_input = input(col + '? ')
        new_entry.append(user_input)
    print(new_entry)
    df2 = pd.DataFrame(new_entry,columns)
    data.append(df2)
    print(data.tail())

writer(datafile, "test.csv")
