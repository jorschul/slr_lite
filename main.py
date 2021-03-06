from functions import get_access_token, get_auth_file
import json

with open("config.json") as config_json:
	config_dict = json.load(config_json)

client_id = config_dict["client_id"]
client_secret = config_dict["client_secret"]
username = config_dict["username"]
password = config_dict["password"]
smartAccountDomain = config_dict["smartAccountDomain"]
virtualAccountName = config_dict["virtualAccountName"]

with open("hosts.json") as hosts_json:
	host_dict = json.load(hosts_json)

access_token = get_access_token(client_id, client_secret, username, password)

for hostname in host_dict.keys():
	serialNumber = host_dict[hostname][0]
	reservationCode = host_dict[hostname][1]
	tagList = host_dict[hostname][2]

	print("Processing "+hostname+" - SN:"+serialNumber)

	output = get_auth_file(smartAccountDomain, virtualAccountName, access_token, hostname, serialNumber, reservationCode, tagList)

	print(output)