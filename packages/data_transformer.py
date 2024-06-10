from data_extractor import Apicalls as ac
import json, csv

class Datatransform():

    def __init__(self):

        # Start the object instance
        self.prismacloud_data=ac()

        # aws data
        self.aws_protected_items=self.prismacloud_data.aws_protected_items()
        self.aws_ec2=self.prismacloud_data.aws_ec2_list()
        self.aws_s3=self.prismacloud_data.aws_s3_list()
        self.aws_rds=self.prismacloud_data.aws_rds_list()
        self.aws_ebs=self.prismacloud_data.aws_ebs_list()

        # azure data
        self.azure_protected_items=self.prismacloud_data.azure_protected_items()
        self.azure_vm=self.prismacloud_data.azure_vm_list()
        self.azure_file_shares=self.prismacloud_data.azure_storage_file_shares()

    def aws_data(self):

        self.aws_all_items=self.aws_ec2+self.aws_ebs+self.aws_s3+self.aws_rds

        awsData=[]
        for x in self.aws_all_items:
            backup=False
            for y in self.aws_protected_items:
                if len(y['id'])>len(x['id']):
                    if y['id'][-len(x['id']):].lower()==x['id'].lower():
                        backup=True
                        break
                else:
                    if x['id'][-len(y['id']):].lower()==y['id'].lower():
                        backup=True
                        break
            row={
                "ResourceName":x['name'],
                "ResourdeId":x['id'],
                "Cloud":"aws",
                "ResourceType":x['resourceType'],
                "Region":x['regionName'],
                "AccountName":x['accountName'],
                "AccountId":x['accountId'],
                "Backup":backup
            }
            awsData.append(row)
        return awsData

    def azure_data(self):

        azure_all_items=self.azure_vm+self.azure_file_shares
        azData=[]

        for x in azure_all_items:
            backup=False
            for y in self.azure_protected_items:
                if len(y['data']['properties']['sourceResourceId'])>len(x['id']):
                    if y['data']['properties']['sourceResourceId'][-len(x['id']):].lower()==x['id'].lower():
                        backup=True
                        break
                else:
                    if x['id'][-len(y['data']['properties']['sourceResourceId']):].lower()==y['data']['properties']['sourceResourceId'].lower():
                        backup=True
                        break
            row={
                "ResourceName":x['name'],
                "ResourdeId":x['id'],
                "Cloud":"azure",
                "ResourceType":x['resourceType'],
                "Region":x['regionName'],
                "AccountName":x['accountName'],
                "AccountId":x['accountId'],
                "Backup":backup
            }
            azData.append(row)
        return azData
    
    def oci_data(self):
        pass