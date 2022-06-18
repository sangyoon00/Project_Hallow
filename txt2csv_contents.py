import csv
import os
import re

def RemoveSymbol(src):
    dest = ""
    for elem in src:
        if str.isalpha(elem) or str.isspace(elem) or str.isalnum(elem):
            dest+=elem
    return dest
    
def listToString(str_list):
    result = ""
    for s in str_list:
        result += s + " "
    return result.strip()


with open('C:\\Users\\SANGYOON\\Project_Hallow\\case5\\판례내용\\64983_소유권이전등기·소유권이전등기말소등기.txt','r') as textfile:
    list=[]
    result_list=[]
    for row in textfile:
        row=re.sub(r"[\t\"]*","",row)
        newstr=row.strip()
        new_string=RemoveSymbol(newstr)

        list.append(new_string)
    result=listToString(list)

    result_list.append(result)
    print(result_list[0])
    


output_file=open('result1.csv','a')
wr=csv.writer(output_file,delimiter = ",", quoting=csv.QUOTE_ALL)
wr.writerow(result_list)