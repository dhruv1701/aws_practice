import boto3
ec2 = boto3.resource('ec2',region_name='ap-south-1')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-04b1ddd35fd71475a',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='ec2-keypair'
 )