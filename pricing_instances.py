import boto3
import json

def get_price(region, os, instance_type):

  pricing_client = boto3.client('pricing')
  
  data=pricing_client.get_products(ServiceCode='AmazonEC2',Filters=[{'Type' :'TERM_MATCH', 'Field':'location','Value':region},{'Field': 'instanceType', 'Value': instance_type, 'Type': 'TERM_MATCH'},{'Field': 'tenancy', 'Value': 'shared', 'Type': 'TERM_MATCH'},{'Field': 'preInstalledSw', 'Value': 'NA', 'Type': 'TERM_MATCH'},{'Field': 'capacityStatus', 'Value': 'Used', 'Type': 'TERM_MATCH'},{'Field': 'operatingSystem', 'Value': os, 'Type': 'TERM_MATCH'}])
  
  od=json.loads(data['PriceList'][0])['terms']['OnDemand']
  id1 = list(od)[0]
  id2 = list(od[id1]['priceDimensions'])[0]
  
  print(od[id1]['priceDimensions'][id2]['pricePerUnit']['USD'])

if __name__ == '__main__':
  get_price('Asia Pacific (Mumbai)','Linux','t2.micro')
