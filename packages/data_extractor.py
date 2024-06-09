import requests, os, json

# region API calls
class Apicalls():

    def __init__(self):
        # Global Variables / Api call attributes
        self.__ak=os.environ.get('ACCESS_KEY')
        self.__secret=os.environ.get('SECRET')
        self.__region="api2"
    
    # Methods
    def __token(self):
        url="https://{}.prismacloud.io/login".format(self.__region)
        payload={
            "username":self.__ak,
            "password":self.__secret
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8'
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        return response['token']
    
    def azure_protected_items(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'azure-recovery-service-backup-protected-item' and resource.status = Active"
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        return response['items']
    
    def azure_vm_list(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'azure-vm-list' and resource.status = Active"
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        return response['items']
    
    def azure_storage_file_shares(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'azure-storage-file-shares' and resource.status = Active"
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        return response['items']
    
    def aws_protected_items(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'aws-backup-protected-resources' and resource.status = Active"
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        return response['items']
    
    def aws_ec2_list(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'aws-ec2-describe-instances' and resource.status = Active",
            #"withResourceJson": True
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        return response['items']
    
    def aws_rds_list(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'aws-rds-describe-db-instances' and resource.status = Active",
            "withResourceJson": True
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        return response['items']
    
    def aws_ebs_list(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'aws-ec2-describe-volumes' and resource.status = Active",
            #"withResourceJson": True
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        return response['items']
    
    def aws_s3_list(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'aws-s3api-get-bucket-acl' and resource.status = Active",
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        return response['items']