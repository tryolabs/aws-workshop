# Internet Gateway

We already have our VPC with 4 subnets, until now the four subnets are privates. To turn public 2 of them, we need a Internet Gateway for our VPC and create a Route Table to route all external traffic thru the Internet Gateway.
Finally associate 2 of our subnets to this route table and assign them a public IP, so they turn into public subnets (accept traffic from outside the VPC).

## Create a Internet Gateway
1. Go to Internet Gateways on the left section
2. click Create Internet Gateway
3. as Name tag put: awsworkshopIGW
4. click: Yes, Create
5. click Attach to VPC
6. click: Yes, Attach


## Create Route tables
1. Go to Route Tables on the left section
2. Click Create Route Table
3. As Name tag: awsWorkshopPublicRT
4. click Yes, Create
5. on the bottom section select Routes tab
6. then click on Edit button
7. click on Add another Route
8. as **Destination** put 0.0.0.0/0
9. as **Target** select your internet gateway
10. click Save
11. now select Subnet Associations tab
12. click on Edit
13. select 10.0.1.0-us-east-1a and 10.0.3.0-us-east-1b
14. click save

## Assign public IP to our public subnet
1. Go to Subnets on the left section
2. Select the 10.0.1.0-us-east-1a
3. click on Subnet Actions
4. Select Modify auto-assign IP settings
5. check: Enable auto-assign public IPv4 address
6. click Save
7. click Close
8. Repeat steps 2-7 with 10.0.3.0-us-east-1b

---
**Next:** [Create a Nat Instance](/workshop/vpc-subnets-bastion/03-nat-instance.md)
