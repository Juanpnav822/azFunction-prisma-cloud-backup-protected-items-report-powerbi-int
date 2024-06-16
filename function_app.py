import azure.functions as func
import datetime
import logging, os
import packages.data_loader as dl
from azure.storage.blob import BlobServiceClient
from packages.data_transformer import Datatransform as dt

app = func.FunctionApp()

#Global Variable
connection_string=os.environ.get('CONNECTION_STRING')
container_name1='prismacloudrecursos'
container_name2='historial'

@app.timer_trigger(schedule="0 0 1 * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

    data=dt()
    dataAll=data.azure_data()+data.aws_data()+data.oci_data()
    
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    nowvalue = datetime.datetime.now()
    dt_string = nowvalue.strftime("%Y-%m-%d")

    dl.send_dicts_to_blob_storage(dataAll,blob_service_client,container_name1,'reporte-prisma-cloud-backup.csv')
    dl.send_dicts_to_blob_storage(dataAll,blob_service_client,container_name2,'reporte-prisma-cloud-backup'+dt_string+".csv")

    logging.info('Blob created successfully!')
