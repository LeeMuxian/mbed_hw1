# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061114.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)

#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
Output = []
for title in ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']:
   target_data = list(filter(lambda item: item['station_id'] == title, data))
   if len(target_data) == 0:
      Output.append([title, 'None'])
   sum = 0
   N = 0
   for i in target_data:
      if i['PRES'] != '-99.000' or i['PRES'] != '-999.000':
         sum += float(i['PRES'])
         N += 1
   mean = round(sum / N, 1)
   Output.append([title, mean])
data = Output
# Retrive ten data points from the beginning.
target_data = data[:10]

#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================