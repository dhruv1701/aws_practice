import boto3
# import pprint
#
ec2 = boto3.client('ec2')
# cloud_watch = boto3.client('cloudwatch')
# print(cloud_watch.get_metric_statistics(Namespace='CWAgent', MetricName ='mem_used_percent', Dimensions=[{'Name': 'InstanceId', 'Value': 'i-0357e8c6b27bfecfc'}, { 'Name': 'ImageId', 'Value': 'ami-04b1ddd35fd71475a'},{ 'Name': 'InstanceType', 'Value': 't2.micro'}], StartTime='2021-1-20T17:00:00', EndTime='2021-01-20T17:30:00', Statistics=['Average'], Period=300 ))

instances = ec2.describe_instances()

print(instances['Reservations'][0]['Instances'])
print(instances['Reservations'][0]['OwnerId'])

# for instances_info in instances_list:
#     print(instances_info['InstanceId']+" "+instances_info['InstanceType'])

# instance id tick
# cpu util tick
# meme cpu False
# acc no iam_instance_profile
# current instance size 
# graph
