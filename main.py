from pprint import pprint
import requests
import json
import os

#CONST
BASE_URL_API = 'http://sc.kr1ps.com/api'
USER_API = 'code-test'
PWD_API= '?C8`R5`!83l/f~U%>}%V'
#CONST

#FUNCTIONS

def list_vms():
    response = requests.get(f"{BASE_URL_API}" + '/resource/vm', auth=(USER_API, PWD_API))
    #print(response.status_code)    
    #print(response.text)
    data = json.loads(response.text)
    print('')
    print('List of vms')
    for vm in data:
        print('id: ',vm['id'], ' name vm: ', vm['name'])
    print('')

def list_dns():
    response = requests.get(f"{BASE_URL_API}" + '/resource/dns', auth=(USER_API, PWD_API))
    #print(response.status_code)
    #print(response.text)
    data = json.loads(response.text)
    print('')
    print('List of dns')
    for dns in data:
        print('id ',dns['id'],' name: ', dns['name'])
    print('')

def reset_db():
    response = requests.post(f"{BASE_URL_API}" + '/reset', auth=(USER_API, PWD_API))
    print(response.status_code)
    print(response.text)
       
def get_vm_byid(vm_id):
    response = requests.get(f"{BASE_URL_API}" + '/resource/vm/' + vm_id , auth=(USER_API, PWD_API))
    #print(response.status_code)
    #print(response.text)
    data = json.loads(response.text)
    return data

def download_dns():
    response = requests.get(f"{BASE_URL_API}" + '/resource/dns', auth=(USER_API, PWD_API))
    #print(response.status_code)
    #print(response.text)
    data = json.loads(response.text)
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def get_dns_byid(dns_id):
    response = requests.get(f"{BASE_URL_API}" + '/resource/dns/' + dns_id, auth=(USER_API, PWD_API))
    #print(response.status_code)
    #print(response.text)
    data = json.loads(response.text)
    return data

def put_vm(vm_id, new_name_vm, data):
    print('vm name old ', data['name'])
    data['name'] = new_name_vm
    print('vm name new ', data['name'])
    response = requests.put(
        f"{BASE_URL_API}" + '/resource/vm/' + vm_id, json=data, auth=(USER_API, PWD_API))
    print(response.status_code)


def put_dns(dns_id, new_name_vm, data):
    print('dns name old ', data['name'])
    data['name'] = new_name_vm
    print('dns name new ', data['name'])
    response = requests.put(
        f"{BASE_URL_API}" + '/resource/dns/' + dns_id, json=data, auth=(USER_API, PWD_API))
    print(response.status_code)

def search_dns_id(name):
    print(name)
    with open('data.json') as file:
        data = json.load(file)
        for dnsName in data:            
            if str(dnsName['name']) == str(name):
                return dnsName['id']
    return None
            

def new_name_vm(name, region):
    # <name>-<8 character hex id>-<environment>-<resource type>
    data = name.split('-')
    # <name>-<8 character hex id>-<region>-<environment>-<resource type>
    rs = data[0] + '-' + data[1] + '-' + \
        new_region(region=region) + '-' + data[2] + '-' + data[3]
    return rs


def new_region(region):
    # europe-west3 -> euw3
    data = region.split('-')
    l1 = data[0]
    l2 = data[1]
    return l1[0:2]+l2[0:1]+l2[-1]



#FUNCTIONS

#MENU OPTION
menu_options ={
    1:'List VMS',
    2:'List DNS',
    3:'Update Name VMS and DNS',
    4:'Reset db',
    5:'Exit',
}

#FUNCTION CLEAR CONSOLE
clear = lambda: os.system('cls')

def print_menu():
    print('Menu options')
    for key in menu_options.keys():
        print(key,'--',menu_options[key])

def update_mv_dns_name():
    clear()
    while(True):
        option =''
        try:
            print('')
            print('Update VM and DNS')
            print('Enter VM id or number 3 for back to options')
            print('')
            option = str(input('Enter Id vm: '))
        except:
            print('')
            print('Wrong input. Please enter a number ...')

        if option == '3':
            clear()
            return False
        else:
            vm=get_vm_byid(option)
            #OLD VM NAME
            oldNameVM = vm['name']
            print('vm name: ', vm['name'], '--',' region ', vm['region'])
            # NEW NAME VM
            newname = new_name_vm(name=oldNameVM, region=vm['region'])
            print('new vm name',newname)
            #DOWNLOAD DNS DB
            download_dns()
            #SEARCH DNS ID
            dns_id= search_dns_id(oldNameVM)
            if dns_id != None:
                print('dns id ', dns_id)
                #SEARCH DNS
                dns = get_dns_byid(dns_id)
                print('dns',dns)
                #UPDATE VM 
                put_vm(vm['id'], newname, vm)
                #UPDATE DNS
                put_dns(dns_id, newname, dns)


#MAIN FUNCTION
def main():
    clear()
    while(True):
        print_menu()
        option =''
        try:
            print('')
            option = int(input('Enter your choice: '))
        except:
            print('')
            print('Wrong input. Please enter a number ...')

        if option == 1:
            list_vms()
        elif option == 2:
            list_dns()
        elif option == 3:
            update_mv_dns_name()
        elif option == 4:
            print('')
            print('Reset db')
            reset_db()
            print('')   
        elif option == 5:
            print('')
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number bewteen 1 and 3.')



if __name__ == "__main__":
    main()