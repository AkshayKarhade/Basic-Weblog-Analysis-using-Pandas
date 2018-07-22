import pandas as pd

#read the input website log (.csv) from its location.
csv_data = pd.read_csv('C:\\Users\\Akshay Karhade\\Desktop\\log_data1.csv')

#slice out the ip address and time stamp from the first column and store it in new columns "ip_add" and :time_stamp".
csv_data['ip_add'] = csv_data.apply(lambda x: x['ip_add_uname_pass_time_stamp'][:16], axis=1)
csv_data['time_stamp'] = csv_data.apply(lambda x: x['ip_add_uname_pass_time_stamp'][-29:-1], axis=1)

csv_final = csv_data[['ip_add','time_stamp','source']]#Save the required information in a new variable csv_final.
csv_final.head(5)#display the first 5 entries.

#Final output
print(csv_final)
