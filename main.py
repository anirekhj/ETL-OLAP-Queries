import csv
import os
import pprint

def wrapper_function(lst, header):
  for item in lst:
    print('\t'+item + '\t\t\t\t\t\t' + str(sum(list(map(int, [(i[4] if i[header] == item else 0) for i in records])))))

def wrapper_function_2a(lst_1, lst_2, header_1, header_2):
  for item_1 in lst_1:
    for item_2 in lst_2:
      # print(records);
      print('\t'+item_1+"-"+item_2 + '\t\t\t\t\t\t' + str(sum(list(map(int, [(i[4] if (i[header_1] == item_1 and i[header_2] == item_2) else 0) for i in records])))))

def wrapper_function_2b(lst_1, lst_2, header_1, header_2):
  for item_1 in lst_1:
    print(item_1);
    for item_2 in lst_2:
      # print(records);
      print('\t'+item_2 + '\t\t\t\t\t\t' + str(sum(list(map(int, [(i[4] if (i[header_1] == item_1 and i[header_2] == item_2) else 0) for i in records])))))

def wrapper_function_3a(lst_1, lst_2, lst_3, header_1, header_2, header_3):
  for item_1 in lst_1:
    print('\n'+item_1);
    for item_2 in lst_2:
      print('\t\t\t\t\t\t'+item_2)
      for item_3 in lst_3:
        print('\t'+'\t\t\t\t\t\t\t\t\t\t\t\t'+item_3 + '\t\t\t\t\t\t' + str(sum(list(map(int, [(i[4] if (i[header_1] == item_1 and i[header_2] == item_2 and i[header_3] == item_3) else 0) for i in records])))))

def wrapper_function_3b(lst_1, lst_2, lst_3, header_1, header_2, header_3):
  for item_1 in lst_1:
    for item_2 in lst_2:
      print('\n'+item_1+'-'+item_2)
      for item_3 in lst_3:
        print('\t'+'\t\t\t\t\t\t\t\t\t\t\t\t'+item_3 + '\t\t\t\t\t\t' + str(sum(list(map(int, [(i[4] if (i[header_1] == item_1 and i[header_2] == item_2 and i[header_3] == item_3) else 0) for i in records])))))

def wrapper_function_3c(lst_1, lst_2, lst_3, header_1, header_2, header_3):
  for item_1 in lst_1:
    print('\n'+item_1);
    for item_2 in lst_2:
      for item_3 in lst_3:
        print(item_2+'-'+item_3 + '\t\t\t\t\t\t' + str(sum(list(map(int, [(i[4] if (i[header_1] == item_1 and i[header_2] == item_2 and i[header_3] == item_3) else 0) for i in records])))))

def wrapper_function_4(lst_1, lst_2, lst_3, lst_4, header_1, header_2, header_3, header_4):
  for item_1 in lst_1:
    print('\n'+item_1);
    for item_2 in lst_2:
      for item_3 in lst_3:
        print('\t\t\t\t'+item_2+'-'+item_3);
        for item_4 in lst_4:
          print('\t\t\t\t\t\t\t\t\t\t\t'+item_4 + '\t\t\t\t\t\t' + str(sum(list(map(int, [(i[4] if (i[header_1] == item_1 and i[header_2] == item_2 and i[header_3] == item_3 and i[header_4] == item_4) else 0) for i in records])))))


os.system( 'clear' )

records = []
headers = []
with open('Car_Sales_Data_Set.csv', newline='', encoding='utf-8-sig') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',')
  for row in spamreader:
    records.append(row);

headers = records[0]
records = records[1:]
records = sorted(records, key=lambda x:(x[0]))

with open('Car_Sales_Data_Set_First_Sorting.csv', 'w', newline='') as csvfile:
  wr = csv.writer(csvfile)
  wr.writerow(headers)
  wr.writerows(records)

records = sorted(records, key=lambda x:(x[0],x[1]))

with open('Car_Sales_Data_Set_Second_Sorting.csv', 'w', newline='') as csvfile:
  wr = csv.writer(csvfile)
  wr.writerow(headers)
  wr.writerows(records)

records = sorted(records, key=lambda x:(x[0],x[1],x[2]))

with open('Car_Sales_Data_Set_Third_Sorting.csv', 'w', newline='') as csvfile:
  wr = csv.writer(csvfile)
  wr.writerow(headers)
  wr.writerows(records)

print("1.()\n\n2.(Country)\n\n3.(Time_Year)\n\n4.(Time_Quarter-Time_Year)\n\n5.(Car_Manufacturer)\n\n6.(Country, Time_Year)\n\n7.(Country, Time_Quarter-Time_Year)\n\n8.(Country, Car_Manufacturer)\n\n9.(Time_Year, Car_Manufacturer)\n\n10.(Time_Quarter-Time_Year, Car_Manufacturer)\n\n11.(Country, Time_Year, Car_Manufacturer)\n\n12.(Country, Time_Quarter-Time_Year, Car_Manufacturer)\n")

try:
    user=int(input("Type a number: "))
except ValueError:
    print("This is not a whole number.")

dictionary = {headers[0]: list(set([i[0] for i in records])),
              headers[1]: list(set([i[1] for i in records])),
              headers[2]: list(set([i[2] for i in records])),
              headers[3]: list(set([i[3] for i in records]))}
# print("\nDictionary with the use of Mixed Keys: ")
# pprint.pprint(dictionary)

if (user == 1):
  pprint.pprint(headers+records)

elif (user == 2):
  print('\n'+headers[0]+'\t\t\t\t\t\t\t'+headers[4])
  wrapper_function(dictionary[headers[0]],0)

elif (user == 3):
  print('\n'+headers[1]+'\t\t\t\t\t'+headers[4])
  wrapper_function(dictionary[headers[1]],1)

elif (user == 4):
  print('\n'+headers[2]+'-'+headers[1]+'\t\t'+headers[4])
  wrapper_function_2a(dictionary[headers[2]],dictionary[headers[1]],2,1)

elif (user == 5):
  print('\n'+headers[3]+'\t\t\t\t'+headers[4])
  wrapper_function(dictionary[headers[3]],3)

elif (user == 6):
  print('\n'+headers[0]+'-'+headers[1]+'\t\t\t\t\t'+headers[4])
  wrapper_function_2b(dictionary[headers[0]],dictionary[headers[1]],0,1)

elif (user == 7):
  print('\n'+headers[0]+'\t\t\t\t\t'+headers[2]+'-'+headers[1])
  wrapper_function_3c(dictionary[headers[0]],dictionary[headers[2]],dictionary[headers[1]],0,2,1)

elif (user == 8):
  print('\n'+headers[0]+'-'+headers[3]+'\t\t\t'+headers[4])
  wrapper_function_2b(dictionary[headers[0]],dictionary[headers[3]],0,3)

elif (user == 9):
  print('\n'+headers[1]+'-'+headers[3]+'\t\t\t\t\t'+headers[4])
  wrapper_function_2b(dictionary[headers[1]],dictionary[headers[3]],1,3)

elif (user == 10):
  print('\n'+headers[2]+'-'+headers[1]+'\t\t\t\t\t\t\t'+headers[3])
  wrapper_function_3b(dictionary[headers[2]],dictionary[headers[1]],dictionary[headers[3]],2,1,3)

elif (user == 11):
  print('\n'+headers[0]+'\t\t\t\t\t'+headers[1]+'\t\t\t\t\t'+headers[3])
  wrapper_function_3a(dictionary[headers[0]],dictionary[headers[1]],dictionary[headers[3]],0,1,3)

elif (user == 12):
  print('\n'+headers[0]+'\t\t\t'+headers[2]+'-'+headers[1]+'\t\t'+headers[3]+'\t\t'+headers[4])
  wrapper_function_4(dictionary[headers[0]],dictionary[headers[2]],dictionary[headers[1]],dictionary[headers[3]],0,2,1,3)
