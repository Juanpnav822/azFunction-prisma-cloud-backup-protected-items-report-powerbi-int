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
        self.aws_rds=self.prismacloud_data.aws_rds_instance_list()+self.prismacloud_data.aws_rds_cluster_list()
        self.aws_ebs=self.prismacloud_data.aws_ebs_list()

        # azure data
        self.azure_protected_items=self.prismacloud_data.azure_protected_items()
        self.azure_vm=self.prismacloud_data.azure_vm_list()
        self.azure_file_shares=self.prismacloud_data.azure_storage_file_shares()

        # oci data
        self.oci_protected_boot_volumes=self.prismacloud_data.oci_protected_boot_volumes()
        self.oci_protected_volumes=self.prismacloud_data.oci_protected_volumes()
        self.oci_boot_volumes=self.prismacloud_data.oci_boot_volumes()
        self.oci_volumes=self.prismacloud_data.oci_volumes()

    #region AWS
    def aws_data_rds(self):

        awsDataRds=[]
        for x in self.aws_rds:
            backup=False
            for y in self.aws_protected_items:
                try:
                    if x['data']['dbinstanceArn']==y['data']['ResourceArn']:
                        backup=True
                        break
                except:
                    pass
                try:
                    if x['data']['dbclusterArn']==y['data']['ResourceArn']:
                        backup=True
                        break
                except:
                    pass
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
            awsDataRds.append(row)
        return awsDataRds

    def aws_data(self):

        self.aws_all_items=self.aws_ec2+self.aws_ebs+self.aws_s3

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
        return awsData+self.aws_data_rds()
    
    # region Azure
    def azure_data_db_flexible(self):
        azData=[]
        az_db_flexible=self.prismacloud_data.azure_postgresql_flexible_server()+self.prismacloud_data.azure_mysql_flexible_server()
        backup=True
        for x in az_db_flexible:
            if x['data']['properties']['backup']['backupRetentionDays']<0:
                backup=False
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
                    elif y['data']['properties']['sourceResourceId'][0:(len(x['id'])-1)].lower()==x['id'].lower():
                        backup=True
                        break
                else:
                    if x['id'][-len(y['data']['properties']['sourceResourceId']):].lower()==y['data']['properties']['sourceResourceId'].lower():
                        backup=True
                        break
                    elif x['id'][0:len(y['data']['properties']['sourceResourceId'])].lower()==y['data']['properties']['sourceResourceId'].lower():
                        backup=True
                        break
                    elif x['id'].lower()==y['data']['properties']['sourceResourceId'].lower():
                        backup=True
                        break

            if x['regionName']=='':
                x['regionName']="global"
            if x['resourceType']=="Other":
                x['resourceType']=x['service']+"/"+x['resourceType']

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
        azData=azData+self.azure_data_db_flexible()
        return azData
    
    def oci_data(self):
        ociData=[]
        
        #BootVolumes
        print(json.dumps(self.oci_boot_volumes))
        for x in self.oci_boot_volumes:
            backup=False
            for y in self.oci_protected_boot_volumes:
                if x['data']['id']==y['data']['bootVolumeId']:
                    backup=True
                    break
            row={
                "ResourceName":x['name'],
                "ResourdeId":x['id'],
                "Cloud":"oci",
                "ResourceType":x['resourceType'],
                "Region":x['regionName'],
                "AccountName":x['accountName'],
                "AccountId":x['accountId'],
                "Backup":backup
            }
            ociData.append(row)

        #Volumes
        for x in self.oci_volumes:
            backup=False
            for y in self.oci_protected_volumes:
                if x['data']['id']==y['data']['volumeId']:
                    backup=True
                    break
            row={
                "ResourceName":x['name'],
                "ResourdeId":x['id'],
                "Cloud":"oci",
                "ResourceType":x['resourceType'],
                "Region":x['regionName'],
                "AccountName":x['accountName'],
                "AccountId":x['accountId'],
                "Backup":backup
            }
            ociData.append(row)
        return ociData