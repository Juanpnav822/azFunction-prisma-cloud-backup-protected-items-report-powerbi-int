from data_extractor import Apicalls

class Datatransform():

    def __init__(self):
        self.prismacloud_data=Apicalls()
        self.aws_protected_items=self.prismacloud_data.aws_protected_items()
        self.aws_ec2=self.prismacloud_data.aws_ec2_list()
        self.aws_s3=self.prismacloud_data.aws_s3_list()
        self.aws_rds=self.prismacloud_data.aws_rds_list()
        self.aws_ebs=self.prismacloud_data.aws_ebs_list()
        self.aws_all_items=self.aws_ec2+self.aws_ebs+self.aws_s3+self.aws_rds

    def aws_data(self):
        data=[]
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
            data.append(row)
        return data

    def azure_data(self):
        pass

    def oci_data(self):
        pass