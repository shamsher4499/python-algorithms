'''
Given an array, write a program to find the sum of values of 
even and odd index positions separately.
Input: array = [1, 2, 3, 4, 5, 6]
'''
# class ClassList(list):
#     def __hash__(self):
#         return 0

# def sum_value_by_index(list_data:list) -> dict:
#     _list = ClassList([1, 2, 3])
#     dict_data = {
#         _list:0,
#         'odd':0
#     }
#     for key,value in enumerate(list_data):
#         if key%2 == 0:
#             dict_data[_list] += value
#         else:
#             dict_data['odd'] += value

#     return dict_data

# array = [1, 2, 3, 4, 5, 6]
# print(sum_value_by_index(array)) 

# output = {[1, 2, 3]: 9, 'odd': 12}


# def func1(*args, **kwargs):
#     ...

# def func2(*args, **kwargs):
#     ...

# def func3(*args, **kwargs):
#     ...


# data = {
#     'type': func1(),
#     'user': func2(),
#     'user': func2(),
# }



news_sources = [
    "Livemint", "CNBC-TV18", "BBC News", "ETTravelWorld", "The Economic Times",
    "Skift", "Hindustan Times", "Travel And Leisure", "Financial Express", "CNBC",
    "Bloomberg", "DW News", "NBC News", "Global News", "WION", "India Today",
    "Brut India", "The Economist", "CBS News", "NDTV", "Forbes", "Sky News",
    "ABC News", "World Animal Protection"
]

import requests
import json

url = "https://api.travelnewsdigest.in/dashboard/create-collaborator/"

payload = json.dumps({
  "name": "BBC News"
})
headers = {
  'Authorization': 'Token e4f1f23146936d5940efdb65d47bf41621f1fefd',
  'Content-Type': 'application/json'
}

for i in news_sources:
    payload = json.dumps({
        "name": i
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response)

# print(response.text)
