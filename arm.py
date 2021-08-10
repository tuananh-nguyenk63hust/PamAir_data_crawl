import requests
import json
import xlsxwriter
from datetime import datetime
workbook = xlsxwriter.Workbook('PamAir-Data-10-08-2021.xlsx')
url_='https://api.pamair.org/services/airstation'

headers_airs={
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2Mjg1ODc3ODQsImV4cCI6MTYyODU4ODA4NCwiYXVkIjoiL3NlcnZpY2VzL2FpcnN0YXRpb24iLCJzdWIiOiIzY2Y5ZDk4OC1kMmQ5LTQ1YTEtOGM5Yy0zNTUyODQ5OTA5YzciLCJpc3MiOiJwYW1haXItcGFydG5lciJ9.a_OTXeuiP-xhWcQ5YdAbsnqR3nG8mnAJqS0aOmnWZRs',
    'content-type': 'application/json',
    'clientid':'3cf9d988-d2d9-45a1-8c9c-3552849909c7'
}
result= requests.get(url_,headers=headers_airs)
res_json=result.json()
#print(res_json)
url_2="https://api.pamair.org/services/airusaqi24"
headers_airs24={
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2Mjg1ODc4MDksImV4cCI6MTYyODU4ODEwOSwiYXVkIjoiL3NlcnZpY2VzL2FpcnVzYXFpMjQiLCJzdWIiOiIzY2Y5ZDk4OC1kMmQ5LTQ1YTEtOGM5Yy0zNTUyODQ5OTA5YzciLCJpc3MiOiJwYW1haXItcGFydG5lciJ9.RbxofFUoYzBZ0i8lOuXxDU_TgRQVkStYUQWK-d93naE',
    'clientid':'3cf9d988-d2d9-45a1-8c9c-3552849909c7',
    'content-type': 'application/json'
}
list__=[]
for row in res_json["data"]:
    try:
        print(row["idst"])
        print("\n")
        payload={"idst": row["idst"]}
        str_loca=""
        if len(row["nameVi"])>31:
            for x in range(0,29):
                str_loca=str_loca+row["nameVi"][x]
            print(str_loca)
        else:
            str_loca=row["nameVi"]
        if str_loca=="Đường 1/4":
            str_loca="Đường 1-4"
        rum=1    
        try:
            rum=1
            worksheet=workbook.add_worksheet(str_loca)
        except:
            rum+=1
            worksheet=workbook.add_worksheet(str_loca+"-"+str(rum))
        res_row=requests.post(url_2,data=json.dumps(payload),headers=headers_airs24)
        res_obj=res_row.json()["aqi"]
        row_line=1
        col_line=0
        worksheet.write(0,col_line,"TIME")
        worksheet.write(0,col_line+1,"AQI")
        worksheet.write(0,col_line+2,"Location")
        worksheet.write(1,col_line+2,row["infoLo"])
        worksheet.write(0,col_line+3,"Name")
        worksheet.write(1,col_line+3,row["nameVi"])
        for x in res_obj:
            dt_obj =int(x["longtime"])
            print(type(dt_obj))
            print("\n")
            value=x["value"]
            worksheet.write(row_line,col_line,dt_obj)
            worksheet.write(row_line,col_line+1,value)
            row_line+=1
        list__.append(res_row)
    except:
        print("don't have idts")
workbook.close()
print(len(list__))




