import requests
import json
class CatParse:
    __data={}
    __response_data=""

    def __init__(self):
        pass

    def set_conn_params(self,url):
        headers = {'Content-type': 'application/json'}
        response = requests.get(url,headers = headers,verify=False)
        self.__response_data=response.json()
        return self.__response_data

    def get_facts_name(self,data,**kwargs):
        facts_list=[]
        facts_obj=[]

        for items in data['all']:
            name=items['user']['name']
            if "fname" in kwargs:
                if name['first']==kwargs['fname']:
                    facts_obj.append(items)
            if "lname" in kwargs:
                if name['last']==kwargs['lname']:
                    facts_obj.append(items['text'])
        return facts_obj

    def get_data(self):
        facts_list=[]
        dict_selected_facts={}
        for items in self.__response_data['all']:
            try:
                name=items['user']['name']
            except:
                continue
            full_name=' '.join(name.values())
            if ord(full_name[0])%2!=0:
                facts_list.append(items)
        dict_selected_facts['all']=facts_list
        return dict_selected_facts

    def post_server(self,data):
        headers = {'Content-type': 'application/json'}
        data_json = json.dumps(data)
        url = 'http://localhost:80/facts'
        response = requests.post(url, data=data_json,headers = headers,verify=False)

    def display_output(self, data,mode):
        if mode=="JSON":
            print "Facts OUTPUT .....",data
        if mode=="YAML":
            print "YAML"

    def delete_facts(self,data):
        headers = {'Content-type': 'application/json'}
        data_json = json.dumps(data)
        url = 'http://localhost:80/facts'
        response = requests.delete(url, data=data_json,headers = headers,verify=False)
