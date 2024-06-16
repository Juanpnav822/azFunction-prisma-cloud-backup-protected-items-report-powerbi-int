import csv, logging
from io import StringIO

def send_dicts_to_blob_storage(data, blob_service_client, container_name, blob_name):
    desired_order = ['ResourceName','ResourdeId','Cloud','ResourceType','Region','AccountName','AccountId','Backup']
    reordered_list = []
    for item in data:
        reordered_dict = {key: item[key] for key in desired_order if key in item}
        reordered_list.append(reordered_dict)
    data=reordered_list

    csv_string = StringIO()
    writer = csv.writer(csv_string)
    writer.writerow(data[0].keys())  # Write header row
    for item in data:
        writer.writerow(list(item.values()))

    #Upload the CSV data to the blob
    try:
        blob_client = blob_service_client.get_blob_client(container_name, blob_name)
        blob_client.upload_blob(csv_string.getvalue(), content_type="text/csv", overwrite=True)
        print(f"Data successfully uploaded to blob '{blob_name}' in container '{container_name}'.")
        logging.info(f"Data successfully uploaded to blob '{blob_name}' in container '{container_name}'.")
    except Exception as e:
        print(f"Error uploading data: {e}")
        logging.info(f"Error uploading data: {e}")