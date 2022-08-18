from pprint import pprint
import requests
import json

BASE_URL_API = 'http://sc.kr1ps.com/api'
user = 'code-test'
pwd = '?C8`R5`!83l/f~U%>}%V'


def list_vms(metodo):
    response = requests.get(f"{BASE_URL_API}" + metodo, auth=(user, pwd))
    print(response.status_code)
    print(response.text)


def get_vm_byid(metodo):
    response = requests.get(f"{BASE_URL_API}" + metodo, auth=(user, pwd))
    print(response.status_code)
    print(response.text)
    data = json.loads(response.text)
    return data


def list_dns(metodo):
    response = requests.get(f"{BASE_URL_API}" + metodo, auth=(user, pwd))
    print(response.status_code)
    print(response.text)
    data = json.loads(response.text)
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


def get_dns_byid(metodo):
    response = requests.get(f"{BASE_URL_API}" + metodo, auth=(user, pwd))
    print(response.status_code)
    print(response.text)
    data = json.loads(response.text)
    return data


def put_vm(metodo, data):
    response = requests.put(
        f"{BASE_URL_API}" + metodo, json=data, auth=(user, pwd))
    print(response.status_code)


def put_dns(metodo, data):
    response = requests.put(
        f"{BASE_URL_API}" + metodo, json=data, auth=(user, pwd))
    print(response.status_code)


def search_dns_id(name):
    print(name)
    with open('data.json') as file:
        data = json.load(file)
        for dnsName in data:
            print(dnsName['name'])
            if str(dnsName['name']) == str(name):
                return dnsName['id']
            else:
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


# STEP 1 LIST ALL VM
"""
metodoAllVM = '/resource/vm'
print(f"{BASE_URL_API}" + metodoAllVM)
list_vms(metodo=metodoAllVM)

"""
# STEP 2 ID VM TO CHANGE
# GET By ID

vm_id = '1492'

metodoVMById = '/resource/vm/' + vm_id
print(f"{BASE_URL_API}" + metodoVMById)
dt = get_vm_byid(metodo=metodoVMById)

#oldNameVM = dt['name']
print(dt['name'])
print(dt['region'])


# NEW NAME VM
newname = new_name_vm(name=oldNameVM, region=dt['region'])
print(newname)

# DOWNLOAD DATA DNS
# GET LIST DNS
metodoAllDNS = '/resource/dns'
print(f"{BASE_URL_API}" + metodoAllDNS)
list_dns(metodo=metodoAllDNS)

# SEARCH DNS ID
dns_id = search_dns_id(str(oldNameVM))
print(dns_id)
# 1663

# SEARCH DNS OBJECT
# GET DNS Record by ID
metodoDNSByID = '/resource/dns/'+dns_id
print(f"{BASE_URL_API}" + metodoDNSByID)
dns = get_dns_byid(metodo=metodoDNSByID)


# UPDATE VM
# PUT VM
metodoPutVM = '/resource/vm/' + vm_id
dataVM = {
    "name": newname,
    "id": vm_id,
    "ip": dt['ip'],
    "region": dt['region'],
    "labels": {
        "dns-zone": "example.org"
    }
}

print(dataVM)

print(f"{BASE_URL_API}" + metodoPutVM)

# put_vm(metodo=metodoPutVM, data=dataVM)

# UPDATE DNS
# PUT DNS

metodoPutDNS = '/resource/dns/'+dns_id
dataDNS = {
    "id": dns['id'],
    "name": newname,
    "ip": dns['ip'],
    "zone": dns['zone']
}

print(dataDNS)

print(f"{BASE_URL_API}" + metodoPutDNS)
# put_dns(metodo=metodoPutDNS, data=dataDNS)


# print(f"{BASE_URL_API}" + metodoVMById)
# get_vm_byid(metodo=metodoVMById)

# END"""
