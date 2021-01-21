import boto3
import csv

def get_client(resource):
    return boto3.client(resource)


def start_monitoring():
    ec2_client = get_client('ec2')
    cloud_watch_client = get_client('cloudwatch')

    ec2_instances_info = ec2_client.describe_instances()

    owner_id = ec2_instances_info['Reservations'][0]['OwnerId']
    instances_info = ec2_instances_info['Reservations'][0]['Instances']

    cpu_utilization = list()
    mem_utilization = list()

    print("[+] Owner Id : "+owner_id+"\n\n")

    for info in instances_info:
        cpu_utilization.append({'datapoints': cloud_watch_client.get_metric_statistics(Namespace='AWS/EC2', MetricName ='CPUUtilization', Dimensions=[{'Name': 'InstanceId', 'Value': info['InstanceId']}], StartTime='2021-1-18T23:18:00', EndTime='2021-01-19T10:30:00', Statistics=['Average'], Period=300 )['Datapoints'], 'instance_id': info['InstanceId'], 'instance_type': info['InstanceType']})
        mem_utilization.append({'datapoints': cloud_watch_client.get_metric_statistics(Namespace='CWAgent', MetricName ='mem_used_percent', Dimensions=[{'Name': 'InstanceId', 'Value': info['InstanceId']},{'Name': 'ImageId', 'Value': info['ImageId']},{ 'Name': 'InstanceType', 'Value': info['InstanceType']}], StartTime='2021-1-20T17:00:00', EndTime='2021-01-20T17:30:00', Statistics=['Average'], Period=300 )['Datapoints'], 'instance_id': info['InstanceId'], 'instance_type': info['InstanceType']})


    for instance in cpu_utilization:
        print("[+] Cpu Utilization \n\nInstanceID : "+instance['instance_id']+" InstanceType : "+instance['instance_type']+"\n\n")

        with open('cpu_data'+instance['instance_id']+'.csv', 'w', newline='') as f:
            fieldnames=['Time Stamp','Average Cpu Util']
            writer = csv.DictWriter(f, fieldnames = fieldnames)

            writer.writeheader()

            for datapoints in instance['datapoints']:
                writer.writerow({'Time Stamp':datapoints['Timestamp'],'Average Cpu Util':datapoints['Average']})


    for instance in mem_utilization:
        print("[+] Memory Utilization \n\nInstanceID : "+instance['instance_id']+" InstanceType : "+instance['instance_type']+"\n\n")
        with open('mem_data'+instance['instance_id']+'.csv', 'w', newline='') as f:
            fieldnames=['Time Stamp','Average Cpu Util']
            writer = csv.DictWriter(f, fieldnames = fieldnames)

            writer.writeheader()

            for datapoints in instance['datapoints']:
                writer.writerow({'Time Stamp':datapoints['Timestamp'],'Average Cpu Util':datapoints['Average']})

if __name__ == '__main__':
    start_monitoring()


#csv with info
# sending memory stats
#finding cost of all the instance types in a region(region will be given as a parameter)