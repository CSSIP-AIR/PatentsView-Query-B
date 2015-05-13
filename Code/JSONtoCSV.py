import json
import sys
import csv
import requests
import pprint

def convertToCSV(jsonData, keys):
    returnData = {}
    global counter
    row = []

    # Define all groups here, since they might be nested in.
    groups = ["cited_patents","inventors","application_citations","applications",\
              "assignees","citedby_patents","coinventors","cpc_subgroups", "cpc_subsections",\
              "cpcs", "ipcs","locations", "nber_subcategories","nbers","patents","uspc_mainclasses",\
              "uspc_subclasses","uspcs","years"]
    common = list(set(groups).intersection(set(keys)))
    if(len(common)>0):
        # Generate the length of maximum results, since the number of rows 
        # for each primary entity will be determined by it.
        length_dict = len(jsonData[common[0]])  
        for group in common:
            if len(jsonData[group]) > length_dict:
                length_dict = len(jsonData[group])
    else:  
        length_dict = 1
    for i in range(0, length_dict):
        row = []
        returnData[i] = {}
        for key in keys:
            if key in common:
                try:
                    index = keys.index(key)
                    tempData = jsonData[key][i]
                    tempKeys = sorted(tempData.keys())
                    for k in tempKeys:
                        returnData[i][k] = tempData[k]
                except:
                    pass
            else:
                returnData[i][key] = jsonData[key]
    return returnData


def writeCSV(a, filename):
    write = csv.writer(open(filename, 'w', newline=''))
    a = json.loads(a)
    groups = ["cited_patents","inventors","application_citations","applications",\
              "assignees","citedby_patents","coinventors","cpc_subgroups", "cpc_subsections",\
              "cpcs", "ipcs","locations", "nber_subcategories","nbers","patents","uspc_mainclasses",\
              "uspc_subclasses","uspcs","years"]
    key = list(a.keys())
    key = list(set(groups).intersection(set(key)))
    j = a[key[0]]
    i = 0
    for jsonData in j:
        keys = jsonData.keys()
        csvData = convertToCSV(jsonData, sorted(keys))
        if (i==0):
            write.writerow(list(sorted(csvData[0].keys())))
        for key in csvData.keys():
            row = []
            data = csvData[key]
            for k in sorted(data.keys()):
                row = row + [data[k]]
            write.writerow(row)
        i += 1
def main():

    baseQuery = 'http://54.175.112.29/api/'
    patentQuery = baseQuery + 'patents/query?'
    inventorQuery = baseQuery + 'inventors/query?'
    assigneeQuery = baseQuery + 'assignees/query?'
    cpcQuery = baseQuery + 'cpc_subsections/query?'
    uspcQuery = baseQuery + 'uspc_mainclasses/query?'
    nberQuery = baseQuery + 'nber_subcategories/query?'
    locationQuery = baseQuery + 'locations/query?'
    # filename = sys.argv[2]
    # a = sys.argv[1]
    query = patentQuery + 'q={"_and":[{"_contains":{"assignee_organization":"Census"}},{"_gte":{"patent_date":"2000-01-01"}},{"_lte":{"patent_date":"2010-12-31"}},{"_contains":{"uspc_mainclass_title":"Electricity"}}]}&f=["inventor_id","inventor_first_name","inventor_last_name"]'
    response = requests.get(query)
    a = response.text
    b = json.loads(a)
    with open('query_12.text', 'w', encoding='utf8') as outfile:
            json.dump(b, outfile, sort_keys=True, indent=4, ensure_ascii=False)
    filename = 'query_12.csv'
    writeCSV(a, filename)
    
        

if __name__ == '__main__':
    main()