#!/usr/bin/python3
# You can have this code if you want it. :) kma2023 
# ErIsS
# https://github.com/aaronlumen 
# 
# A Python script that creates a *Service-Now* 'case' for a specific morpheus tenant using the 'Morpheus ID' or the 'Install Base Item' in *Service-Now*:
# No warranty, liability or otherwise concern about anyone else using this script which they do at their own pleasure and risk.  
# 
# Author [Aaron.Surina] copywrong ¤©2023 Lumen Technologies LLC.  
#
import requests
import json
#
#                                                                                                               #
# Configure the base elements such as credentials for morpheus and serviceNow as well as the endpoints needed.  #
#
#######################################################################################################################
# Morpheus API URL
morpheus_url = 'https://morpheus.example.com/api'
#######################################################################################################################
# Variable area
#######################################################################################################################
# ServiceNow API URL
servicenow_url = 'https://example.service-now.com/api/now/v2/table/incident'
#######################################################################################################################
# Morpheus credentials
morpheus_user = 'username'
morpheus_password = 'password'
#######################################################################################################################
# ServiceNow credentials
servicenow_user = 'username'
servicenow_password = 'password'
#######################################################################################################################
# Tenant ID and Morpheus ID or Install Base Item ID
tenant_id = '12345'
morpheus_id = '67890'
install_base_item_id = 'ABCD1234'
#######################################################################################################################
# Get the Morpheus Instance details based on the Morpheus ID
#######################################################################################################################
morpheus_instance_url = f'{morpheus_url}/instances/{morpheus_id}'
headers = {'Content-Type': 'application/json'}
response = requests.get(morpheus_instance_url, auth=(morpheus_user, morpheus_password), headers=headers)
morpheus_instance_data = response.json()['instance']
#######################################################################################################################
# Get the Install Base Item details from ServiceNow based on the Install Base Item ID    #
install_base_item_url = f'{servicenow_url}/alm_install_base_item/{install_base_item_id}'
headers = {'Content-Type': 'application/json'}
response = requests.get(install_base_item_url, auth=(servicenow_user, servicenow_password), headers=headers)
install_base_item_data = response.json()['result']
#######################################################################################################################
# Create the ServiceNow Case payload #
case_payload = {
    'short_description': f'Issue with {morpheus_instance_data["name"]}',
    'description': 'Please provide a detailed description of the issue...',
    'caller_id': tenant_id,
    'u_morpheus_instance_id': morpheus_id,
    'u_morpheus_instance_name': morpheus_instance_data['name'],
    'u_install_base_item': install_base_item_id,
    'u_install_base_item_name': install_base_item_data['name'],
}
#######################################################################################################################
# Create the ServiceNow Case
headers = {'Content-Type': 'application/json'}
response = requests.post(servicenow_url, auth=(servicenow_user, servicenow_password), headers=headers, json=case_payload)
case_data = response.json()['result']
#######################################################################################################################
# Print the ServiceNow Case number
print(f'###############################################################################################################################################################################################')
print(f'ServiceNow Case created: {case_data["number"]}')
print(f'Creds: {install_base_item_url,servicenow_url,servicenow_user,description,headers,response,tenant_id,morpheus_id,morpheus_instance_data,case_payload
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
# [2023 AARONLUMEN] 
#  
#########################################################################################################################
# Warning: This is free for Lumen to use as they wish.   
# ------------------------------------------------------
#########################################################################################################################
# We first define the Morpheus API URL;
# We then define the ServiceNow API URL, and then Morpheus and ServiceNow credentials;
# After which we then define the Tenant ID, Morpheus ID and/or Install Base Item ID!
#
# But wait... there's more!  
# After a little relax time, we take happy time seriously, so we prepare ourselves for the next adventure where we use the Morpheus API to get the Instance details based on the Morpheus ID
# And to be fair about it, we use the ServiceNow API to get the Install Base Item details based on the Install Base Item ID.
#
#########################################################################################################################
# HammerTime! Once ready, we create the ServiceNow Case payload with the necessary fields, including the following:
# short description, description, caller ID ( tenant ID), Morpheus Instance ID and Morpheus instance Name, and Install Base Item ID and/or Name.
#
# Now we're cooking with gas finally; 
#########################################################################################################################
# We use the ServiceNow API to create the case with the payload we just created,and we print the ServiceNow Case number once it's created which can be obtained using results, piping it out or any # 
# preferred mechanism to cache or store the output.
#
#######################################################################################################################

