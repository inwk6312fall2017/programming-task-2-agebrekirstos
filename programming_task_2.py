import csv
def hrm_crime():
    """ list the crime count in Halifax HRM"""
    with open("Crime.csv", 'r') as myfile:
        crime_csv = csv.reader(myfile, delimiter = ',')
        crime_types = []
        crime_IDs = []
        crime_counts = []

        for row in crime_csv:
            crime_type = row[8]
            crime_ID = row[2]
            crime_count = row[7]
            crime_types.append(crime_type)
            crime_IDs.append(crime_ID)
            crime_counts.append(crime_count)
        print("Crime Type",'\t', "Crime ID", '\t' , "Crime Count")
        print("==========",'\t', "========", '\t',  "============")
        for i in range(1,len(crime_counts)-1):
            print(crime_types[i], crime_IDs[i], crime_counts[i])





hrm_crime()