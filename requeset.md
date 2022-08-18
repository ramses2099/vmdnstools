# Systems Test

All steps taken should be documented in Markdown

## Preparation:
Set up k3s cluster and apply the Concatenated.yml to prep the scenario.
Document how you set it up

## Tasks

### 1. Scenario: Developers are having problem with deployed app

The developers are having problems updating a deployment of the application backend-creative-dev. You need to make ensure the application is up and running 
and is reachable both internally and through the ingre
ss IP.

Document steps taken to identify and solve the developers problem.

### 2. Code Test

The code test should be completed using go, python or bash. You will need to know how to install the any required dependencies.

python -m pip install <Module Name>
python -m pip install requests


#### Challenge Description

Your task is to update the names of VMs so they comply with the new name standard, and change any DNS records to use the new VM name.

The shortened region name should include the first two letters of the first section and the first letter of the second section as well as any
 trailing numbers. example: europe-west3 -> euw3

Old name standard:
<name>-<8 character hex id>-<environment>-<resource type>


New name standard:
<name>-<8 character hex id>-<region>-<environment>-<resource type>


1. Update the VMs.
2. Update the DNS records.

#### Running the Code Test API Server

Apply the CodeTestDeploy.yml file to the k3s cluster you set up for the systems test and connect to the API using basic AUTH included as a k8s secret.

You can find a basic documentation of the API in the file Api.md