# Api Docs

Each API call requires you to use basic authentication, the username and password is included as a k8s secret in the deploy manifest.

## Data Structures

### VM

An example <VM> object looks like this:
{
  "name": "envoy-1c942599-stage-vm",
  "id": "1214",
  "ip": "10.10.1.236",
  "region": "eu-north1",
  "labels": {
    "dns-zone": "example.org"
  }
}


### A Record

An example DNS <Record> object:
{
    "id": "1943",
    "name": "envoy-1c942599-stage-vm",
    "ip": "10.10.1.236",
    "zone": "example.org"
}


# API Enpoints

## Reset Data
POST /reset

If you for some reason need to reset the database to the original values, you can either use this endpoint or restart the binary.

## Dump Test Result

GET /dump

TODO Document dump endpoint

## List VMS
GET /resource/vm


RESPONSE: A list of <VM> objects

## List DNS Records
GET /resource/dns

RESPONSE: A list of dns <Record> objects

## GET VM
GET /resource/vm/<id>


RESPONSE: A <VM> object for the ID

## GET DNS Record
GET /resource/dns/<id>


RESPONSE: A <Record> object for the ID

## PUT VM
PUT /resource/vm/<id>

REQUEST BODY: <VM>

## PUT DNS Record
PUT /resource/dns/<id>


REQUEST BODY: <Record>