import csv

# data format: 2d list
def create_csv_file(file_name, data):
	f = open(file_name,"w")  
	w = csv.writer(f)  
	w.writerows(data)  
	f.close()