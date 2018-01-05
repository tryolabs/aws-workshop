# VPC

We are going to create our VPC with 4 subnets (2 private and 2 public).

## Create a VPC
1. Go to VPC under Networking & Content Delivery.
2. Go to Your VPCs on the left section.
3. Click on Create VPC.
4. As **Name** **tag** put: `awsworkshopvpc`.
5. As **IPv4 CIDR** **block** put: `10.0.0.0/16`.
6. Then click: Yes, Create.

## Create 4 subnets
1. Go to Subnets on the left section.
2. Click Create Subnet.
3. As **Name tag** put: `10.0.1.0-us-east-1a`.
4. **Availability Zone**: `us-east-1a`.
5. As **IPv4 CIDR** **block** put: `10.0.1.0/24`. CIDR block for any subnet will be a subset of the VPC CIDR block.
6. Then click in Yes, Create.
7. Repeat steps 2-6 using as **Name tag**: `10.0.2.0-us-east-1a`, **Availability Zone**: `us-east-1a` and **IPv4 CIDR block**: `10.0.2.0/24`.
8. Repeat steps 2-6 using as **Name tag**: `10.0.3.0-us-east-1b`, **Availability Zone**: `us-east-1b` and **IPv4 CIDR block**: `10.0.3.0/24`.
9. Repeat steps 2-6 using as **Name tag**: `10.0.4.0-us-east-1b`, **Availability Zone**: `us-east-1b` and **IPv4 CIDR block**: `10.0.4.0/24`.

---
**Next:** [create an Internet Gateway and a public Routes table](/workshop/vpc-subnets-bastion/02-internet-gateway.md).

