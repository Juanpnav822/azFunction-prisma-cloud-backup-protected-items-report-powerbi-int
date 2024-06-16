import requests, os, json

# region API calls
class Apicalls():

    def __init__(self):
        # Global Variables / Api call attributes
        self.__ak=os.environ.get('ACCESS_KEYA')
        self.__secret=os.environ.get('SECRET')
        self.__region="api4"
    
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
    
    # region Microsoft Azure
    def azure_protected_items(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'azure-recovery-service-backup-protected-item' and resource.status = Active",
            "withResourceJson": True
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000,"withResourceJson": True}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
    def azure_vm_list(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'azure-vm-list' and resource.status = Active",
            "limit":10000,
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
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
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
    def azure_mysql_flexible_server(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'azure-mysql-flexible-server' and resource.status = Active"
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000, "withResourceJson": True}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
    def azure_postgresql_flexible_server(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'azure-postgresql-flexible-server' and resource.status = Active"
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000, "withResourceJson": True}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
    def azure_postgresql_server(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'azure-postgresql-server' and resource.status = Active"
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000, "withResourceJson": True}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
    def azure_postgresql_server(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'azure-sql-server-list' and resource.status = Active"
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000, "withResourceJson": True}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
    # region AWS
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
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000,"withResourceJson": True}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
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
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
    def aws_rds_instance_list(self):
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
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000,"withResourceJson": True}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
    def aws_rds_cluster_list(self):
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
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000,"withResourceJson": True}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
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
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
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
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
    # region OCI
    def oci_protected_boot_volumes(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'oci-compute-boot-volume-backup' and resource.status = Active",
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000,"withResourceJson": True}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
    def oci_protected_volumes(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'oci-block-storage-volume-backup' and resource.status = Active",
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000,"withResourceJson": True}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
    def oci_boot_volumes(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'oci-block-storage-boot-volume' and resource.status = Active",
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000,"withResourceJson": True}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response
    
    def oci_volumes(self):
        url="https://{}.prismacloud.io/search/api/v2/config".format(self.__region)
        payload={
            "query":"config from cloud.resource where api.name = 'oci-block-storage-volume' and resource.status = Active",
        }
        headers={
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': self.__token()
        }
        response=requests.request("POST",url,headers=headers,json=payload)
        response=json.loads(response.content)
        url2="https://{}.prismacloud.io/search/config/page".format(self.__region)
        nextResponse=requests.request("POST",url2,headers=headers,data=json.dumps({"pageToken":response['nextPageToken'],"limit":10000,"withResourceJson": True}))
        nextResponse=json.loads(nextResponse.content)
        
        response=nextResponse['items']
        
        return response