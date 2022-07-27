#%%
import requests
import pandas as pd
import json


access_token = 'Fww62xBYi2c7YrEix8-xO_EEPALnoYLG8iHfOJB4YvM'

headerss = { 
    "Content-Type":"application/json",  
    "Authorization":"Bearer Fww62xBYi2c7YrEix8-xO_EEPALnoYLG8iHfOJB4YvM"
    }

final_list = [[] for x in range(1000)]
last_position = 0

data = "sales_invoices.json?filter=state%3Aopen|late"
url = 'https://moneybird.com/api/v2/223753937777329273/{}'.format(data)

#sending request to url
response = requests.get(url=url, headers=headerss)

#printing status code: 200 means a succes
print("request-code : ", response.status_code)
df2 = json.loads(response.content)

print(df2[0]['invoice_id'])
print(df2[0]['total_price_excl_tax'])
print(df2[0]['total_unpaid'])
#%%


#input: pagenumber
def api_call(pagenumber):

    global last_position
    for i in range(1+pagenumber):
 
        
        data = "sales_invoices.json?filter=state%3Aopen|late&page={}".format(i)
        url = 'https://moneybird.com/api/v2/223753937777329273/{}'.format(data)

        #sending request to url
        response = requests.get(url=url, headers=headerss)

        #printing status code: 200 means a succes
        print("request-code : ", response.status_code)
        df2 = json.loads(response.content)

        for i in range(len(df2)):
            
            final_list[last_position + i + 1].append(df2[i]['invoice_id'])
            final_list[last_position + i].append(df2[i]['total_price_excl_tax'])
            final_list[last_position + i].append(df2[i]['total_unpaid'])

        last_position = i
    
    return final_list


#invoices[["total_unpaid","invoice_id", "state", 'events']][invoices['total_unpaid'] >= 1 ]
#invoices['state'].unique()

#%%
print(test)

#%%
paid_invoices = pd.DataFrame(invoices['id'][invoices['invoice_id']>0])
paid_invoices['invoice_id'] = invoices['invoice_id'][invoices['invoice_id']>0]
print(paid_invoices)

#%%
paid_invoices
for i in paid_invoices['id']:
    print(i)
    data_invoice = requests.get(url='https://moneybird.com/api/v2/223753937777329273/sales_invoices/{}.json'.format(int(i)), headers=headerss)
    data_invoice = json.loads(data_invoice.content)
    print(data_invoice)

    extract_unpaid = data_invoice['total_unpaid']
    extract_invoice_id = data_invoice['invoice_id']
    print('extract_unpaid: ', extract_unpaid, " invoice: ", extract_invoice_id)
