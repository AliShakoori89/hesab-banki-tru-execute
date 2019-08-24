import json
import os.path

class JsonHandler:
    def __init__(self):
        pass
    
    def open_search(self,id_search):
        with open("customer_list.json")as f:
            data=json.load(f)
            if id_search in data:
                return data        
            else: 
                return False

    def add_sheets(self,list_dic, id_search,sheet):
        self.sheet=sheet
        self.id_search=id_search
        with open('customer_list.json','w')as f:
            list_dic[id_search]['supply']=list_dic[id_search]['supply'] + sheet
            f.write(json.dumps(list_dic))               

    def sub_sheets(self,list_dic,id_search,sheet):
        self.id_search=id_search
        self.sheet=sheet
        if list_dic[id_search]['supply'] > sheet:
            with open('customer_list.json', 'w') as f:
                list_dic[id_search]['supply']=list_dic[id_search]['supply'] - sheet
                f.write(json.dumps(list_dic))
            return True
        else:
            return False
            
                
    def withdraw(self,list_dic,id_search):
        self.id_search=id_search
        with open('customer_list.json') as f:
            data=json.load(f)
            if id_search in data:
                with open('customer_list.json','w') as f:
                    del data[id_search]
                    f.write(json.dumps(data))
                return True
            else:
                return False

    def show(self):
        with open('customer_list.json', "r") as f:
            data=json.load(f)
            #print(data)
            return data


    def add(self, dictionary):
        if not os.path.isfile('customer_list.json'): 
            with open('customer_list.json', 'w')as f:
                f.write(json.dumps(dictionary))
        else:
            with open('customer_list.json')as f:
                feeds = json.load(f)
            feeds.update(dictionary)
            with open('customer_list.json', 'w') as f:
                f.write(json.dumps(feeds))
            

            
