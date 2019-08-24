import json
import os.path

class JsonHandler:
    def __init__(self):
        pass

    def add_sheets(self, id_saerch, sheet):
        self.id_saerch=id_saerch
        self.sheet=sheet
        with open('customer_list.json') as f:
            data=json.load(f)
            if id_saerch in data:
                with open('customer_list.json', 'w') as f:
                    data[id_saerch]['supply']=data[id_saerch]['supply'] + sheet
                    f.write(json.dumps(data))                  
                return True
            else:
                return False

    def sub_sheets(self,id_saerch,sheet):
        self.id_saerch=id_saerch
        self.sheet=sheet
        with open('customer_list.json') as f:
            data=json.load(f)
            if (id_saerch in data) and (data[id_saerch]['supply'] > sheet):
                with open('customer_list.json', 'w') as f:
                    data[id_saerch]['supply']=data[id_saerch]['supply'] - sheet
                    f.write(json.dumps(data))
                return True
            else:
                return False
            
                
    def withdraw(self,id_saerch):
        self.id_saerch=id_saerch
        with open('customer_list.json') as f:
            data=json.load(f)
            if id_saerch in data:
                with open('customer_list.json','w') as f:
                    data.pop(id_saerch)
                    f.write(json.dumps(data))
                return True
            else:
                return False


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
            
