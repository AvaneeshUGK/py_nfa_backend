import json
from os import lchown
# from sys import last_value
import requests 
import datetime
# import requests.auth
from requests.auth import HTTPBasicAuth
from hdbcli import dbapi
from datetime import datetime
# from itertools import zip_longest
import copy
# from datetime import datetime

def hdbcliConnect():
    mydb = dbapi.connect(
        address='aa2e4798-6fdc-44d0-ae30-84587dbd062e.hana.prod-us20.hanacloud.ondemand.com',
        port=443,
        user='DBADMIN',
        password='Peol@1234',
        # encrypt='True' )
    )
    return mydb

def SourceHeaderDetails(event,context):

    Srcevtname = ''
    body ={ "url" : "https://openapi.au.cloud.ariba.com/api/retrieve-project-document/v1/prod/projectDocuments",
    "query" : "$top=100&user=puser1&passwordAdapter=PasswordAdapter1&realm=PEOLSOLUTIONSDSAPP-T&apikey=CquPilxwbZMjdsFOWiq7YyeIeYa4rsiL",
    "basis": "Basic OWExNmQ1MzktYzg4Ni00N2EzLTgxYTItNmY2NzAwMjEyNmJlOjMyd3g0dDhvbUFWQzZhd2R2S2p2N0NKYjBpTVhtSmY3"
    }   
    main_url ="https://provider-oxb1v9j3.it-cpi009-rt.cfapps.us20.hana.ondemand.com/http/aribaiflow"

    data = requests.get(main_url,json = body,auth=HTTPBasicAuth("sb-aa5edad9-ae74-47c1-a57f-08236d406c02!b5098|it-rt-provider-oxb1v9j3!b34","f36f502a-049f-4230-97f0-5771c5b84840$5euKkMrPZs_nJbPK3BTCoL-GgY1s_sNXnoXi88I6sNw="))

    data = data.json()  
    final_data = []
    for i in data['value']:

        if i['documentType'] == 'Event':
                final_data.append({
                'Srcevtname' : i['projectId'],
                "Desc":i['name'],
                "Createdby":i['owner'],
                "status":i['status'],
                "Version":i['version'],
                "event_id":i['id']
                })
            

    if Srcevtname == '':
        return {
            "data":final_data
        }
    else :
        for i in final_data:
            if i['Srcevtname'] == Srcevtname:
                final_data = i
                return {
                    "data":final_data
                }   

# def itemdetails(event , context):

#     if "event_id" in event['params']['querystring']:
#         event_id = event['params']['querystring']['event_id']

#     body ={ "url" : "https://openapi.au.cloud.ariba.com/api/sourcing-event/v2/prod/events/"+event_id+"/supplierBids",
#     "query" : "$top=500&user=puser1&passwordAdapter=PasswordAdapter1&realm=PEOLSOLUTIONSDSAPP-T&apikey=RuU300xzEClMIpw8UBalRGERG9LQZcHG&bidHistory=True",
#     "basis": "Basic NTNiMTUxY2EtOTZkYS00ZmM2LWFlNDctZGNhMzg1YjA1ZDNlOnNWUm9LWHNkZ29keXk5amVlbHp6TXF0cGFzR3ViaFIw"
#     }   
   

#     # main_url ="https://62921650trial.it-cpitrial05-rt.cfapps.us10-001.hana.ondemand.com/http/get1"+event_id+"/supplierBids"
#     main_url ="https://provider-oxb1v9j3.it-cpi009-rt.cfapps.us20.hana.ondemand.com/http/aribaiflow"

#     data = requests.get(main_url,json = body,auth=HTTPBasicAuth("sb-56ab32dd-d62c-43db-ba1e-4bd5821ba16d!b177017|it-rt-62921650trial!b26655","001425a1-04b9-4645-bf62-7bf818698f2d$Op_Yyb7LFcvMmeesOItmScAh446eCQQBsq-y6_rNNIM="))    

#     event_id = event_id
    
#     data = data.json()["root"]["payload"]
    
#     invitationId = ''

#     temp = {
#         "title":"",
#         "value":"",
#         "invitationId":""
#     }
#     usd = []
#     vendor_names = []

#     for i in data:
#         if 'item' in i :

#             if 'title' in i['item'] :
#                 temp.update({'title' : i['item']['title']})
#             if i['item']['terms'] != [] :
#                 temp.update({'value' : i['item']['terms']})#[0]['value']
#             if 'invitationId' in i :
#                 temp.update({'invitationId' : i['invitationId']}) 

#         usd.append(temp.copy())

#     final_temp = {
#         "Itemname":'',
#         "Description":'',
#         "Quantity":'',
#         "Unit":'',
#         "Vend":'',
#         "price":''
#     }
#     qna =[]

#     print(usd)
#     final_list = []
#     temp_final_list = []
#     count = 0
#     invitationId = ''

#     for i in usd:
#         if invitationId == '':
#             invitationId = i['invitationId']
#             vendor_names.append(invitationId)
#         if invitationId == i['invitationId']:
#             temp_final_list.append(i)
#         else :
#             count = count + 1
#             invitationId = i['invitationId']
#             vendor_names.append(invitationId)
#             final_list.append([temp_final_list.copy()])
#             temp_final_list.clear()
#             temp_final_list.append(i)
        
#     final_list.append([temp_final_list.copy()])
#     bidding_data_msg = []
#     bidding_data = []
#     for i in final_list:
#         # print(i[0])
#         # print(xyz)
#         for j in i[0] :
#             # print('********')
#             # print(j)
#             # print(j['title'])
#             # print(j['value'][0])
#             # print(xyz)
#             if j['value'] != '':
#                 if j['title'] == 'Price':

#                 # if j['value'][0]['title'] == 'Price':
#                     final_temp['Itemname'] = j['title']
#                     final_temp['Quantity'] = j['value'][1]['value']['quantityValue']['amount']
#                     final_temp['Unit'] = j['value'][1]['value']['quantityValue']['unitOfMeasureName']
#                     final_temp['Vend'] = j['invitationId']
#                     final_temp['price'] = j['value'][2]['value']['moneyValue']['amount']
#                     bidding_data.append(final_temp.copy()) 
#                     final_temp.clear()
#                     final_temp = {
#                     "Itemname":'',
#                     "Description":'',
#                     "Quantity":'',
#                     "Unit":'',
#                     "Vend":'',
#                     "qna":[]}
            
#             if j['title'] == 'Please give a brief overview of your Help Desk.' or j['title'] == 'Do you offer Customer Service 365 day/year?' or j['title'] == 'Do you offer Customer Service in both English and Spanish?' or j['title'] == 'What are the hours of your Help Desk?':
#                 bidding_data_msg.append({j['title']:{"value" : j['value']['value']['simpleValue']},
#                                                        "vender" : j['invitationId'] 
#                                                        })
#         # final_temp['qna'].append(bidding_data_msg.copy())
#         # bidding_data.append(final_temp.copy())
#         qna.append(bidding_data_msg.copy())
#         bidding_data_msg.clear()
#         final_temp.clear()
#         final_temp = {
#         "Itemname":'',
#         "Description":'',
#         "Quantity":'',
#         "Unit":'',
#         "Vend":''
#     }
#     print(bidding_data , qna , vendor_names)
#     headers = {"value1" : "Itemname" ,"value2" : "Description" ,"value3" : "Quantity" ,"value4" :"Unit" ,"value5" :vendor_names}
#     items = {
#         "bidding_date":bidding_data,
#         "qna":qna
#     }

#     return {
#         "status":200,
#         "data":{
#             "header":headers,
#             "items":items
#         }
#     }


def userdata(event , context):
    
    return {
    "data": {
        "items": {
            "bidding_date": [
                {
                    "Description": "",
                    "Guruprasad": 10000.0,
                    "Itemname": "Machine",
                    "Quantity": 50.0,
                    "Supplier_Demo2": 2500.0,
                    "Unit": "each"
                },
                {
                    "Description": "",
                    "Guruprasad": 300.0,
                    "Itemname": "Expenses",
                    "Quantity": 1.0,
                    "Supplier_Demo2": 500.0,
                    "Unit": "each"
                },
                {
                    "Description": "",
                    "Guruprasad": 300.0,
                    "Itemname": "Introduction",
                    "Quantity": 1.0,
                    "Supplier_Demo2": 500.0,
                    "Unit": "each"
                }
            ],
            "headers": {
                "value1": "Itemname",
                "value2": "Description",
                "value3": "Quantity",
                "value4": "Unit",
                "value5": "Guruprasad",
                "value6": "Supplier_Demo2"
            }
        }
    },
    "qns": {
        "qns_data": [
            {
                "Guruprasad": "good",
                "Supplier_Demo2": "Good",
                "question": "Please give a brief overview of your Help Desk."
            },
            {
                "Guruprasad": "true",
                "Supplier_Demo2": "true",
                "question": "Do you offer Customer Service 365 day/year?"
            },
            {
                "Guruprasad": "Yes, Both English and Spanish",
                "Supplier_Demo2": "Yes, Both English and Spanish",
                "question": "Do you offer Customer Service in both English and Spanish?"
            },
            {
                "Guruprasad": "24x7",
                "Supplier_Demo2": "24x7",
                "question": "What are the hours of your Help Desk?"
            }
        ],
        "qns_header": {
            "value1": "question",
            "value2": "Guruprasad",
            "value3": "Supplier_Demo2"
        }
    },
    "status": 200
}


def itemdetailsv1(event , context):
    # try:
    event_id = ''
    if "event_id" in event['params']['querystring']:
        event_id = event['params']['querystring']['event_id']

    body ={ "url" : "https://openapi.au.cloud.ariba.com/api/sourcing-event/v2/prod/events/"+event_id+"/supplierBids",
        "query" :"user=puser1&passwordAdapter=PasswordAdapter1&realm=PEOLSOLUTIONSDSAPP-T&apikey=RuU300xzEClMIpw8UBalRGERG9LQZcHG",
        "basis": "Basic NTNiMTUxY2EtOTZkYS00ZmM2LWFlNDctZGNhMzg1YjA1ZDNlOnNWUm9LWHNkZ29keXk5amVlbHp6TXF0cGFzR3ViaFIw"
        }     

    event_id = event_id
        
    main_url ="https://provider-oxb1v9j3.it-cpi009-rt.cfapps.us20.hana.ondemand.com/http/aribaiflow"

    # main_url ="https://62921650trial.it-cpitrial05-rt.cfapps.us10-001.hana.ondemand.com/http/get1"

    
      #main_url ="https://provider-oxb1v9j3.it-cpi009-rt.cfapps.us20.hana.ondemand.com/http/getTaskDetails"
    try:
        data = requests.get(main_url,json = body,auth=HTTPBasicAuth("sb-aa5edad9-ae74-47c1-a57f-08236d406c02!b5098|it-rt-provider-oxb1v9j3!b34","f36f502a-049f-4230-97f0-5771c5b84840$5euKkMrPZs_nJbPK3BTCoL-GgY1s_sNXnoXi88I6sNw="))
    except Exception as e:
        return e

    if data.status_code == 500:
            return []
    # else:
    data = data.json()['payload']
    # except:
    #     return []
        # # print(e)
        # # dat = json.loads(data)
        # if data.status_code == 500:
        #     data = 500
        
    
    invitationId = ''

    temp = {
        "title":"",
        "value":"",
        "invitationId":""
    }
    usd = []
    vendor_names = []

    for i in data:
        if 'item' in i :

            if 'title' in i['item'] :
                temp.update({'title' : i['item']['title']})
            if "terms" in i["item"]:
                if i['item']['terms'] != [] :
                    temp.update({'value' : i['item']['terms'],
                      'date' : i["submissionDate"],
                      'alternativeId':i["alternativeId"]
                    })#[0]['value']
            if 'invitationId' in i :
                temp.update({'invitationId' : i['invitationId']}) 
            if 'itemsWithBid' in i:
                temp.update({"itemsWithBid":i["itemsWithBid"]})

        usd.append(temp.copy())

    final_temp = {
        "Itemname":'',
        "Description":'',
        "Quantity":'',
        "Unit":'',
        "Vend":'',
        "price":'',
        "alternativeId":" ",
        "tax":" "
    }
    qna =[]

    print(usd)
    tax = []
    final_list = []
    temp_final_list = []
    count = 0
    invitationId = ''
    vendors = []

    for i in usd:
        if invitationId == '':
            invitationId = i['invitationId']
            vendor_names.append(invitationId)
        if invitationId == i['invitationId']:
            temp_final_list.append(i)
        else :
            count = count + 1
            invitationId = i['invitationId']
            vendor_names.append(invitationId)
            final_list.append([temp_final_list.copy()])
            temp_final_list.clear()
            temp_final_list.append(i)
        
    final_list.append([temp_final_list.copy()])
    bidding_data_msg = []
    bidding_data = []
    name=''
    itemname=[]
    price=[]
    quest = ['simplevalue','dateValue','simpleValues','bigDecimalValue','simpleValue']
    for i in final_list:
        for j in i[0] :
            if j['value'] != '' :
                if type(j['value'])==list:
                    if j['value'][0]['title'] == 'Price':
                        final_temp['Itemname'] = j['title']
                        final_temp['Quantity'] = j['value'][1]['value']['quantityValue']['amount']
                        final_temp['Unit'] = j['value'][1]['value']['quantityValue']['unitOfMeasureName']
                        final_temp['Vend'] = j['invitationId']
                        final_temp['price'] = j['value'][2]['value']['moneyValue']['amount']
                        final_temp['Description'] = ""
                        final_temp['tax']=j['value'][2]['historyValue']['moneyValue']['amount']
                        # final_temp['alternativeId'] = j['alternativeId']
                        # final_temp['Date']=j["date"]

                        if name and name!=j["title"]:
                            for k in range(0,len(vendors)):
                                if vendors[k]==j['invitationId']:
                                    price[k]=price[k]+j['value'][2]['value']['moneyValue']['amount']

                        if j['title'] not in itemname:
                            itemname.append(j['title'])
                            name = j['title']

                        if j["invitationId"] not in vendors:
                            vendors.append(j["invitationId"])
                            price.append(j['value'][2]['value']['moneyValue']['amount'])
                        
                        if j['value'][2]['historyValue']['moneyValue']['amount'] not in tax:
                            tax.append(j['value'][0]['value']['moneyValue']['amount'])

                        bidding_data.append(final_temp.copy())
                    
                        for row in j['value'] :
                            if row["title"]=="Tax":
                                t = float(row["value"]["moneyValue"]["amount"])
                                tax.append(t)  

                        final_temp.clear()
                        final_temp = {
                        "Itemname":"",
                        "Quantity":'',
                        "Unit":'',
                        "Vend":"",
                        "qna":[]}
                    # else:
                    #     bidding_data.append({
                    #         "Itemname":j['title'],
                    #         "Quantity":'',
                    #         "Unit":'',
                    #         "Vend":j["invitationId"],
                    #         "price":float(0),
                    #         "Description":""
                    #             })

                    #     tax.append(
                    #         {
                    #         "t": float(0)
                    #         }
                    #         )
                            
            if j['title'] == 'Please give a brief overview of your Help Desk.' or j['title'] == 'Do you offer Customer Service 365 day/year?' or j['title'] == 'Do you offer Customer Service in both English and Spanish?' or j['title'] == 'What are the hours of your Help Desk?' or j['title']=='Is your company, either presently or in the past, been involved in any litigation, bankruptcy, or reorganization for any reason? If so, please provide dates and resolution.' or j['title']=='Do you have a quality manual? If Yes, please upload it here.' or j['title'] =='What is your warranty period?' or j['title']=='What is your overall reject rate?' or j['title'] =='When can you begin servicing our company?' or j['title']=='Please indicate which of these locations you currently service. Please use the "Other" field to indicate any additional locations.' or j['title'] == 'What percentage of your deliveries are on time?':
                for k in quest:
                    if type(j['value'])==list:
                        if k in j['value'][0]['value'] :
                                if j['value'][0]['valueTypeName']=='Date':
                                    bidding_data_msg.append({j['title']:{j['invitationId']  : j['value'][0]['value'][k]}})
                                
                                else:    
                                    bidding_data_msg.append({j['title']:{j['invitationId']  : j['value'][0]['value'][k]}})
                        
                    else:
                        if k in j['value']['value']:
                            bidding_data_msg.append({j['title']:{j['invitationId']  : j['value']['value'][k]}})
                    
        # final_temp['qna'].append(bidding_data_msg.copy())
        # bidding_data.append(final_temp.copy())
        flag = int(0)
        # if not bidding_data:
        #     flag = flag+1
        #     for i in final_list:
        #         for j in i[0] :
        #             bidding_data.append({
        #             "Itemname":j['title'],
        #             "Quantity":'',
        #             "Unit":'',
        #             "Vend":j["invitationId"],
        #             "price":float(0),
        #             "Description":""
        #         })
        #         tax.append(
        #                     {
        #                       "t": float(0)
        #                     }
        #                     )
        qna.append(bidding_data_msg.copy())
        bidding_data_msg.clear()
        final_temp.clear()

        final_temp = {
        "Itemname":'',
        "Description":'',
        "Quantity":'',
        "Unit":'',
        "Vend":''}

    print(bidding_data , qna , vendor_names)

    count = int(len(bidding_data)/2)
    counter = 0

    new_temp = {
        "Itemname":'',
        "Description":'',
        "Quantity":'',
        "Unit":'',
        # 'alternativeId':[],
        # 'date':[]
        }
    
    bidding_data_final = []
    gsub = 0
    sub = 0
    for i in bidding_data:
        counter = counter + 1
        if counter <= count :
            key = i['Itemname']
            for j in bidding_data:
                if j['Itemname'] == key:
                    
                    new_temp["Itemname"] = j["Itemname"]
                    new_temp["Description"] = j["Description"]
                    new_temp["Quantity"] = j["Quantity"]
                    new_temp["Unit"] =  j["Unit"]
                    new_temp[j['Vend']] = j["price"]

                    # if j["Vend"] not in vendor_names:
                    #     vendor_names.append(j["Vend"])
                    # if j["alternativeId"] not in new_temp['alternativeId']:
                    #     new_temp["alternativeId"].append(j["alternativeId"])
                    #     new_temp['date'].append(j["Date"])
                    # new_temp.update({
                    #     "Itemname":j["Itemname"],
                    #     "Description":j["Description"],
                    #     "Quantity": j["Quantity"],
                    #     "Unit" : j["Unit"],
                    #     j['Vend']:float(j["price"]),
                    #     "alternativeId":j["alternativeId"]

                    # })
                    
            bidding_data_final.append(new_temp.copy())
        else :
            break 
    mydb = hdbcliConnect()
    bidding_data = bidding_data_final
    event_id1 = event_id
    
    with mydb.cursor() as mycursor:
        query =("select key,value from item_details1 where EVENT_ID = ?") 
        # mycursor.execute("select * from item_details1 where EVENT_ID = ?")
        mycursor.execute(query,event_id)
        dat = mycursor.fetchall()
        sql=("select id from item_details1 where event_id = ?")
        mycursor.execute(sql,event_id)
        id=mycursor.fetchone()
        # keyy=list(dat.keys())
        # vallue=list(dat.values)
        # if dat:
        #     for row in dat:
        #         delete_query ="DELETE FROM item_details1 WHERE event_id =?"
        #         mycursor.execute(delete_query,event_id)
        # print(dat)
    #     if dat:
    #         for col in dat:
    #             bidding_data.append({
    #                         # "Itemname":col["item_name"],
    #                         # "Description":col["description"],
    #                         # "Quantity": col["quantity"],
    #                         # "Unit" : col["unit"],
    #                         # vendors[0] : float(col["vendor1"]),
    #                         # vendors[1] : float(col["vendor2"])
    #                         # # vendor_names[0] : float(col["vendor1"]),
    #                         # vendor_names[1] : float(col["vendor2"]),
    #                     })
    #             # if not col:        
    #             #     bidding_data.append({
    #             #                 "Itemname":col["item_name"],
    #             #                 "Description":col["description"],
    #             #                 "Quantity": col["quantity"],
    #             #                 "Unit" : col["unit"],
    #             #                 vendors[0] : float(col["vendor1"]),
    #             #                 vendors[1] : float(col["vendor2"])
    #             #                 # vendor_names[0] : float(col["vendor1"]),
    #             #                 # vendor_names[1] : float(col["vendor2"]),
    #             #             })

                        
    #         # bidding_data.append(row)
        d = {}
        i = 'Itemname'
        f=0
        for row in dat:
            if row[0] == i: 
                f= f+1
        i =0
        for row in dat:
            d[row[0]] = row[1]
            i = i + 1
            if i == (len(dat)/f):
                i=0
                d["id"]=id[0]
                bidding_data.append(d.copy())
                d={}
                
        for k in range(0,len(vendors)):
            for row in dat:
                if row[0]==vendors[k]:
                    price[k]=price[k]+float(row[1])
                    

    sub_totalg = float(0)
    sub_total = float(0)
    copy_bidding_data = []
    # copy_bidding_data = bidding_data
    l = ["SubTotal","Tax(%)","Tax","Total"]
    g=[]
    s=[]
    # if bidding_data:
    #     for row in bidding_data:#bidding_data:
    #         # bidding_data.append(row)
    #         sub_totalg = sub_totalg+float(row[vendors[0]])
    #         sub_total = sub_total + float(row[vendors[1]])
            # g = []
    # if flag == 0:        
    #     g.append(sub_totalg)
    #             # if isinstance(tax[0],int) or isinstance(tax[0],float):
    #     g.append(2)
    #     subtotal = ((2*sub_totalg)/100)
    #     g.append(subtotal)
    #     g.append(sub_totalg+subtotal)
    #             # s=[]
    #     s.append(sub_total)
    #     s.append(6.234)
    #     subtotal = ((6.234*sub_total)/100)
    #     s.append(subtotal)
    #     s.append(sub_total+subtotal)
    #     c = 0
    #     for i in l:
    #                 # if bidding_data:
    #         bidding_data.append({
    #                         "Itemname" : " ",
    #                         "Description" : " ",
    #                         "Quantity" : " ",
    #                         vendors[0] : g[c],
    #                         vendors[1] : s[c],
    #                         "Unit" : i
    #                     })
    #         c =c+1
    np=[]
    new_temp.clear()
    new_temp = {
        "Itemname":'',
        "Description":'',
        "Quantity":'',
        "Unit":'',
        # 'alternativeId':[],
        # 'date':[]
        }
    if bidding_data:
        for i in l:
            new_temp["Unit"]=i
            for j in range(0,len(vendors)):
                if i=='SubTotal':
                    new_temp.update({vendors[j]:price[j]})
                elif i=='Tax(%)':
                    t = ((tax[j]*100)/price[j])
                    new_temp.update({vendors[j]:t})
                elif i=='Tax':
                    # tp=price[j]-tax[j]
                    new_temp.update({vendors[j]:tax[j]})
                elif i == 'Total':
                    tp=price[j]+tax[j]
                    new_temp.update({vendors[j]:tp})
            bidding_data.append(new_temp.copy())
            
                    
                    
                    
    # else:
        # bidding_data.append(
        #         {
        #               "Itemname" : " ",
        #                 "Description" : " ",
        #                 "Quantity" : " ",
        #                 vendors[0] : float(0),
        #                 vendors[1] : float(0),
        #                 "Unit" : "  "
        #         }
        #     )
    # for row in copy_bidding_data:
    #     bidding_data.append(row)                   
    header_list = ["Itemname" , "Description" , "Quantity"  , "Unit"  ]
    count = 0
    header1 ={
    }
    for i in header_list:
        count = count + 1
        header1 ["value"+str(count)] = i 
        
    for j in vendor_names:
        count = count + 1
        header1 ["value"+str(count)] = j

    headers = header1
    items = {
        "headers":headers,
        "bidding_data":bidding_data
    }

    qna_temp = {
        "question":""
    }
    
    qna_temp_final = []
    count = int(len(qna))
    for i in qna:
        for j in i:
            qsn = list(j.keys())[0]
            qna_temp["question"] = qsn
            qna_temp[list(j[qsn].keys())[0]] = j[qsn][list(j[qsn].keys())[0]]
            qna_temp_final.append(qna_temp.copy())
            qna_temp.clear()

    key = ''
    temp = {}
    temp_list = []
    count = int(len(qna_temp_final)/len(qna))
    counter = 0
    for i in qna_temp_final:
        key = i['question']
        counter = counter + 1
        if counter <=  count:
            for j in qna_temp_final:
                if j['question'] == key:
                    temp['question'] = j['question']
                    for k in vendor_names:
                        if k in j:
                            temp[k] = j[k]
            temp_list.append(temp.copy())
            temp.clear()

    mydb = hdbcliConnect()
    bidding_data = bidding_data_final
    if vendors:
        with mydb.cursor() as mycursor:
            query = "select key,value from QUESTIONAIRES where EVENT_ID = ?"
            mycursor.execute(query,event_id)
            dat = mycursor.fetchall()
            sql=("select id from Questionaires where event_id = ?")
            mycursor.execute(sql,event_id)
            id=mycursor.fetchone()
            d = {}
            i = 'question'
            f=0
            for row in dat:
                if row[0] == i: 
                    f= f+1
            i =0
            for row in dat:
                d[row[0]] = row[1]
                i = i + 1
                if i == (len(dat)/f):
                    i=0
                    d["id"]=id[0]
                    temp_list.append(d.copy())
                    d={}

    count = 0
    qna_lists = ['question'] + vendor_names
    qna_header = {}

    for i in qna_lists :
        count = count + 1
        qna_header["value"+str(count)] = i

    return {
        "status":200,
        "data":{
            "items":items
        },
        "qns":{
            "qns_header":qna_header,
            "qns_data":temp_list
        }
    }


# def itemdetailsv1post(event,context):
#     event_id = ''
#     if "event_id" in event['params']['querystring']:
#         event_id = event['params']['querystring']['event_id']

#     event_id = event_id
#     print(event_id)    
#     body = event['body-json']
#     values = list(body.values())
#     keys = list(body.keys())
#     mydb = hdbcliConnect()
#     with mydb.cursor() as mycursor:
#         qry="select * from item_details1 where EVENT_ID = ?"
#         mycursor.execute(qry,event_id)
#         dat = mycursor.fetchall()
#         if dat:
#             for row in dat:
#                 delete_query ="DELETE FROM item_details1 WHERE event_id =?"
#                 mycursor.execute(delete_query,event_id)
#         else:        
#             sql = "insert into item_details1(key,value) values(?,?,)"
#             for i in range(0,len(keys)):
#                 value=(keys[i],values[i])#,event_id)
#                 print(value)
#                 mycursor.execute(sql,tuple(value))
#                 # data = itemdetailsv1(event , context)
#         return {
#                 "status" :200,
#                 # "data":data
#             }

def itemdetailsv1post(event,context):
    event_id = ''
    if "event_id" in event['params']['querystring']:
        event_id = event['params']['querystring']['event_id']

    event_id = event_id
    print(event_id)    
    body = event['body-json']
    values = list(body.values())
    keys = list(body.keys())
    mydb = hdbcliConnect()
    with mydb.cursor() as mycursor:
        sql = "insert into item_details1(event_id,key,value) values(?,?,?)"
        for i in range(0,len(keys)):
            value=(event_id,keys[i],values[i])
            print(value)
            mycursor.execute(sql,tuple(value))
        return {
            "status" :200,
            # "data":data
        }


def itemdetailsquesPost(event,context):
    event_id = ''
    if "event_id" in event['params']['querystring']:
        event_id = event['params']['querystring']['event_id']

    event_id = event_id
    print(event_id)    
    body = event['body-json']
    values = list(body.values())
    keys = list(body.keys())
    mydb = hdbcliConnect()
    with mydb.cursor() as mycursor:
        sql = "insert into questionaires(event_id,key,value) values(?,?,?)"
        for i in range(0,len(keys)):
            value=(event_id,keys[i],values[i])
            print(value)
            mycursor.execute(sql,tuple(value))
        return {
            "status" :200,
            # "data":data
        }
def itemdetails_v1(event , context):

    vers = ''
    iid =' '
    aid = ''
    event_id = ' '
    if "event_id" in event['params']['querystring']:
        event_id = event['params']['querystring']['event_id']

    if "vers" in event['params']['querystring']:
        vers = event['params']['querystring']['vers']
    
    # body ={ "url" : "https://openapi.au.cloud.ariba.com/api/sourcing-event/v2/prod/events/"+event_id+"/supplierBids",
    #     "query" : "user=puser1&passwordAdapter=PasswordAdapter1&realm=PEOLSOLUTIONSDSAPP-T&apikey=RuU300xzEClMIpw8UBalRGERG9LQZcHG", 
    #     # &bidHistory=True",
    #     "basis": "Basic NTNiMTUxY2EtOTZkYS00ZmM2LWFlNDctZGNhMzg1YjA1ZDNlOnNWUm9LWHNkZ29keXk5amVlbHp6TXF0cGFzR3ViaFIw"
    #     }     
    
    event_id = event_id

    # main_url ="https://provider-oxb1v9j3.it-cpi009-rt.cfapps.us20.hana.ondemand.com/http/aribaiflow"

    # data = requests.get(main_url,json = body,auth=HTTPBasicAuth("sb-56ab32dd-d62c-43db-ba1e-4bd5821ba16d!b177017|it-rt-62921650trial!b26655","001425a1-04b9-4645-bf62-7bf818698f2d$Op_Yyb7LFcvMmeesOItmScAh446eCQQBsq-y6_rNNIM="))
        
    # data = data.json()['root']['payload']

    body ={ "url" : "https://openapi.au.cloud.ariba.com/api/sourcing-event/v2/prod/events/"+event_id+"/supplierBids",
        "query" : "user=puser1&passwordAdapter=PasswordAdapter1&realm=PEOLSOLUTIONSDSAPP-T&apikey=RuU300xzEClMIpw8UBalRGERG9LQZcHG&bidHistory=True",
        "basis": "Basic NTNiMTUxY2EtOTZkYS00ZmM2LWFlNDctZGNhMzg1YjA1ZDNlOnNWUm9LWHNkZ29keXk5amVlbHp6TXF0cGFzR3ViaFIw"
        }     

    main_url ="https://provider-oxb1v9j3.it-cpi009-rt.cfapps.us20.hana.ondemand.com/http/aribaiflow"

    data1 = requests.get(main_url,json = body,auth=HTTPBasicAuth("sb-aa5edad9-ae74-47c1-a57f-08236d406c02!b5098|it-rt-provider-oxb1v9j3!b34","f36f502a-049f-4230-97f0-5771c5b84840$5euKkMrPZs_nJbPK3BTCoL-GgY1s_sNXnoXi88I6sNw="))
        
    data1 = data1.json()['payload']
    i =0
    # data2 = itemdetailsv1(event , context)
    i = i + 1
    ver = []
    date = []
    # invId= []

    sub_totalg = 0
    subtotal = float(0)
    final=[]
    a=0
    l=[]
    i=1
    j=1
    for row in data1:     
        if "terms" in row["item"]:           
            if row["item"]["terms"]!=" " and type(row["item"]["terms"])==list and len(row["item"]["terms"])!=0:
                if row["item"]["terms"][0]["title"]=="Price":
                    if j==1:
                        subtotal = subtotal + float(row["item"]["terms"][0]['value']['moneyValue']['amount'])
                        iid=row["invitationId"]
                        aid=row["alternativeId"]
                        date=row["submissionDate"]
                    elif iid==row["invitationId"] and aid!=row["alternativeId"]:
                        l.append({
                            "invitationId":row["invitationId"],
                            "alternativeId":row["alternativeId"],
                            "price":subtotal,
                            "Version":"Version"+str(i)
                        })
                        date=row["submissionDate"]
                        subtotal=float(row["item"]["terms"][0]['value']['moneyValue']['amount'])
                        i = i+1
                    # elif iid==row["invitationId"] and date>row["submissionDate"]:
                    #     subtotal=float(row["item"]["terms"][0]['value']['moneyValue']['amount'])
                    #     i = i+1
                    #     aid=row["alternativeId"]
                    elif iid!=row["invitationId"]:
                        l.append({
                            "invitationId":iid,
                            "alternativeId":aid,
                            "price":subtotal,
                            "Version":"Version"+str(i)
                        })
                        if i>a:
                            a=i
                        i=1
                        final.append(l)
                        l=[]
                        subtotal=float(row["item"]["terms"][0]['value']['moneyValue']['amount'])
                        iid=row["invitationId"]
                        aid=row["alternativeId"]
                        date=row["submissionDate"]
                    j=j+1
    final.append(l)
    print(final)
    final_data=[]
    # data3=final[0]
    # data4=final[1]
    # n=len(data3)
    # j=0
    # subtotal=float(0)
    # sub_totalg=float(0)
    # for row in data3:
            
    #         for col in data4:
    #             if j==n-1 and row["Version"]==col["Version"]:
    #                 subtotal=subtotal+col["price"]
    #                 sub_totalg=sub_totalg+row["price"]
    #                 if sub_totalg>subtotal:
    #                     low="Supplier_Demo2"
    #                 else:
    #                     low="Guruprasad"
    #                 final_data.append({
    #                 "Version":row["Version"],
    #                 "Guruprasad":row["price"],
    #                 "Supplier_Demo2":col["price"],
    #                 "low":low
    #                 })
    #             elif row["Version"]==col["Version"]:
    #                 final_data.append({
    #                 "Version":row["Version"],
    #                 "Guruprasad":row["price"],
    #                 "Supplier_Demo2":col["price"]
    #                 })
    #                 subtotal=subtotal+col["price"]
    #                 sub_totalg=sub_totalg+row["price"]
    #         j=j+1

    n=0
    verss=[]
    for n in range(0,i):
        final_data1={}
        final_data1["Version"]='Version'+str(n+1)
        for row in final:
            j=0
            for col in row:
                if col["Version"] not in verss:
                    # final_data1["Version"]=col["Version"]
                    final_data1.update({col["invitationId"]:col["price"]})
                    j=1
                    break
            if j==0:
                final_data1.update({col["invitationId"]:float(0)})
        final_data.append(final_data1.copy())
        verss.append(final_data1["Version"])
            

    if vers:
        for row in final_data:
            if row["Version"]=="Version"+vers:
                return row
    print(final_data)
    if final_data:
        return {
            "data":final_data
        }
    else:
        return{
            "data":"not found"
        }

#     # datetime_objects = [datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f%z") for timestamp in date]
#     # min_timestamp = min(datetime_objects)
#     # max_timestamp = max(datetime_objects)

#     # print(min_timestamp)
#     # print(max_timestamp)


#     # combined_list = list(zip_longest(ver, date))
#     # print(combined_list)

# # print(combined_list)

    # for col in ver:
    #     sub_totalg = 0
    #     subtotal = 0
    #     for row in data1:     
    #         if "terms" in row["item"]:           
    #             if row["item"]["terms"]!=" " and type(row["item"]["terms"])==list:
    #                 if row["item"]["terms"][0]["title"]=="Price":
    #                     # print('iiiiiiiiiiiiii',row["invitationId"])
    #                     if row["invitationId"]=="Guruprasad":
    #                         sub_totalg = sub_totalg + float(row["item"]["terms"][0]['value']['moneyValue']['amount'])
    #                         print('ssssssssssss',sub_totalg)
    #                         combined_list = list(zip_longest(ver, date))
    #                         def get_date_from_response(response):
    #                             return datetime.strptime(response[1], "%Y-%m-%dT%H:%M:%S.%f%z")
    #                         sorted_responses = sorted(combined_list, key=get_date_from_response)
    #                             # ,reverse=True)

    #                         x = list(enumerate(sorted_responses))
    #                         dynamic_version_data = [(f"Version{index+1}", data) for index, data in x]
    #                         print("final_data",dynamic_version_data)

def previewDet(event,context):
    prevData=itemdetailsv1(event,context)
    final_preview=[]
    total = []
    final_pr = []
    low_flag =[]
    unit=[]
    final_temp = [
        "Itemname",
        "Description",
        "Quantity",
        "Unit",
        "Vend"]
    tax=0.0
    # final_p={
    #     "Itemname":''
    # }
    v1,v2 = 0.0,0.0
    for i in range(len( prevData['data']['items']['bidding_data'])):
        temp=prevData['data']['items']['bidding_data'][i]
        values=list(temp.values())
        key2=list(temp.keys())
        if temp["Unit"] != "SubTotal" and temp["Unit"] !="Tax(%)" and temp["Unit"] !="Tax" and temp["Unit"] !="Total":
            # key2[-2]=values[-2]
            final_p={
                "Itemname":''
            }
            # key2[-1]=values[-1]
            if prevData['data']['items']['bidding_data'][i]['Itemname'] != ' ': 
                final_p['Itemname']=prevData['data']['items']['bidding_data'][i]['Itemname']
                for j in range(0,len(key2)):    
                    if key2[j] not in final_temp:
                        final_p.update({key2[j]:values[j]})
                              
                final_preview.append(final_p.copy())

                # vendor1_value = float(values[-2]) if isinstance(values[-2], str) else values[-2]
                # v1 = v1+float(values[-2])
                # vendor2_value = float(values[-1]) if isinstance(values[-1], str) else values[-1]
                # v2 = v2+float(values[-1])

        
                # if v1<v2:
                #     low_flag = key2[-2]
                # else:
                #     low_flag = key2[-1]
        if temp["Unit"] =="Tax" : 
            unit={
                "Itemname":"Tax",
            }
            for j in range(0,len(key2)):    
                    if key2[j] not in final_temp:
                        # final_p['Itemname']=prevData['data']['items']['bidding_data'][i]['Itemname']
                        unit.update({key2[j]:values[j]})
                        
        if temp["Unit"] =="Total": 
            keys=[]
            value=[]
            low_flag='' 
            v=float(0)
            for j in range(0,len(key2)):    
                    if key2[j] not in final_temp:
                        keys.append(key2[j])
                        value.append(values[j])
                        if v==0:
                            v=float(values[j])
                            low_flag=key2[j]  
                        elif v>float(values[j]):
                            v=float(values[j])
                            low_flag=key2[j]          
            final_pr={
                                "Itemname":"Total"
                                # "low_flag":low_flag  
    
                            }
            for j in range(0,len(keys)):
                final_pr.update({keys[j]:float(value[j])})
    final_preview.append(unit.copy())                              
    final_preview.append(final_pr.copy())
    
    if final_preview:
        return{
            "data":final_preview,
            "question":prevData['qns']['qns_data']
        }
                    
    else:
                return{
                "data":"not found"}

def documentUpload(event , context):

    # pdf_data = event['body-json']['data']
    # pdf_name = event['params']['querystring']['filename']

    pdf_data = event['body-json']['base64Content']
    pdf_name = event['body-json']['filename']
    pr_id = event['body-json']['Srcevtname']


    xml_data = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:Ariba:Sourcing:vrealm_400346">
    <soapenv:Header>
        <urn:Headers>
            <!--You may enter the following 2 items in any order-->
            <!--Optional:-->
            <urn:variant>vrealm_400346</urn:variant>
            <!--Optional:-->
            <urn:partition>prealm_400346</urn:partition>
        </urn:Headers>
    </soapenv:Header>
    <soapenv:Body>
        <urn:DocumentImportRequest partition="prealm_400346" variant="vrealm_400346">
            <!--Optional:-->
            <urn:WSDocumentInputBean_Item>
                <!--Optional:-->
                <urn:item>
                <!--You may enter the following 7 items in any order-->
                <urn:Action>Create</urn:Action>
                <urn:Contents>{}
                </urn:Contents>
                <urn:DocumentId></urn:DocumentId>
                <urn:DocumentName>{}</urn:DocumentName>
                <urn:OnBehalfUserId>puser1</urn:OnBehalfUserId>
                <!--Optional:-->
                <urn:WorkspaceId>{}</urn:WorkspaceId>
                </urn:item>
            </urn:WSDocumentInputBean_Item>
        </urn:DocumentImportRequest>
    </soapenv:Body>
    </soapenv:Envelope>
    """.format(pdf_data,pdf_name,pr_id)

    # URL to which the POST request will be sent
    url = "https://s1.au.cloud.ariba.com/Sourcing/soap/PEOLSOLUTIONSDSAPP-T/DocumentImport"

    # Headers for the request
    headers = {
        "Content-Type": "application/xml",  # Specify content type as XML
        "Authorization": "Basic puser1:Ariba1234Ariba",  # If you need authorization
    }

    # Make the POST request
    response = requests.post(url, data=xml_data, headers=headers)

    # Check the response
    print(response.text)
    if response.status_code == 200:
        return {
            "status":200,
            "message":"document uploaded successfully"
        }
    else:
        return {
            "status":403,
            "message":"document uploaded failed"
        }

def questiondelete(event,context):
    event_id = ''
    if "event_id" in event['params']['querystring']:
        event_id = event['params']['querystring']['event_id']
    body = event['body-json']
    values = list(body.values())
    keys = list(body.keys())
    mydb = hdbcliConnect()
    with mydb.cursor() as mycursor:
        sql = "delete from questionaires where event_id = ? and key = ? and value = ?"
        for i in range(0,len(keys)):
            value=(event_id,keys[i],values[i])
            print(value)
            mycursor.execute(sql,tuple(value))
        return {
            "status" :200,
            "data":"deleted successfully"
            # "data":data
        }

def itemdelete(event,context):
    event_id = ''
    if "event_id" in event['params']['querystring']:
        event_id = event['params']['querystring']['event_id']
    body = event['body-json']
    values = list(body.values())
    keys = list(body.keys())
    mydb = hdbcliConnect()
    with mydb.cursor() as mycursor:
        sql = "delete from item_details1 where event_id = ? and key = ? and value = ?"
        for i in range(0,len(keys)):
            value=(event_id,keys[i],values[i])
            print(value)
            mycursor.execute(sql,tuple(value))
        return {
            "status" :200,
            "data":"deleted successfully"
            # "data":data
        }

def questionedit(event,context):
    event_id = ''
    if "event_id" in event['params']['querystring']:
        event_id = event['params']['querystring']['event_id']
    body = event['body-json']
    prevdata = body["prevdata"]
    currentdata = body["currentdata"]
    prevkeys = list(prevdata.keys())
    curkeys = list(currentdata.keys())
    prevalues = list(prevdata.values())
    curvalues = list(currentdata.values())
    mydb = hdbcliConnect()
    with mydb.cursor() as mycursor:
        sql = "update questionaires set value = ? where event_id = ? and key = ? and value = ?"
        for i in range(0,len(prevkeys)):
            value = (curvalues[i],event_id,prevkeys[i],prevalues[i])
            print(value)
            mycursor.execute(sql,tuple(value))
        return {
            "status" :200,
            # "data":data
        }
        
    
def edititem(event,context):
    event_id = ''
    if "event_id" in event['params']['querystring']:
        event_id = event['params']['querystring']['event_id']
    body = event['body-json']
    prevdata = body["prevdata"]
    currentdata = body["currentdata"]
    prevkeys = list(prevdata.keys())
    curkeys = list(currentdata.keys())
    prevalues = list(prevdata.values())
    curvalues = list(currentdata.values())
    mydb = hdbcliConnect()
    with mydb.cursor() as mycursor:
        sql = "update item_details1 set value = ? where event_id = ? and key = ? and value = ?"
        for i in range(0,len(prevkeys)):
            value = (curvalues[i],event_id,prevkeys[i],prevalues[i])
            print(value)
            mycursor.execute(sql,tuple(value))
        return {
            "status" :200,
            # "data":data
        }



            