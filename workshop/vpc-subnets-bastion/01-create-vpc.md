# VPC

Here we are going to create our VPC with 4 subnets.

## Create a VPC
1. Go to VPC under Networking & Content Delivery
2. go to Your VPCs on the left section
3. click on Create VPC
4. As **Name** **tag** put : awsworkshopvpc
5. As **IPv4 CIDR** **block*** put : 10.0.0.0/16
6. then click:  Yes, Create


## Create 4 subnets
1. Go to Subnets on the left section
2. Click Create Subnet
3. as **Name tag** put: 10.0.1.0-us-east-1a
4. **Availability Zone**: us-east-1a
5. As **IPv4 CIDR** **block** put :10.0.1.0/24
6. then click in Yes, Create
7. repeat steps 2-6 using as **Name tag**: 10.0.2.0-us-east-1a, **Availability Zone**: us-east-1a and **IPv4 CIDR block**: 10.0.2.0/24
8. repeat steps 2-6 using as **Name tag**: 10.0.3.0-us-east-1b, **Availability Zone**: us-east-1b and **IPv4 CIDR block**: 10.0.3.0/24
9. repeat steps 2-6 using as **Name tag**: 10.0.4.0-us-east-1b, **Availability Zone**: us-east-1b and **IPv4 CIDR block**: 10.0.4.0/24

---
Next: [Create Internet Gateway and Public Routes Table](/workshop/vpc-subnets-bastion/02-internet-gateway.md)

