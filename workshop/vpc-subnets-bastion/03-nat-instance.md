# NAT Instance

Until now we have 2 public subnets and 2 private subnets. In the private ones, we will deploy the webserver instances that will be accessible via a Load Balancer.

Even if these instances don't need to be reachable from outside of the VPC, they need to have Internet access to download and update packages. For this reason, we need a NAT through which we can route all external outbound traffic.

AWS offers two options for NAT: [NAT Instance](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html) and [NAT Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html).
The Gateway offering is newer and easier to setup than the NAT Instance, and also automatically scales. However, for this tutorial, will go for the NAT Instance purely because it's cheaper (we don't want to be billed too much!).

## Create Nat Instance
1. Go to EC2 under Computer section.
2. Click on Instances on the left menu.
3. Click Launch Instance.
4. Select Community AMIs.
5. Type NAT and then hit Enter.
6. Select the first option that appears:
  1. Root device type: `ebs`
  2. Virtualization type: `hvm`
  3. ENA Enabled: `No`.
7. Select `t2.micro` and click Next: Configure Instance Details.
8. On Network, select your VPC.
9. As subnet, select `10.0.1.0-us-east-1a`
10. Click Next: Add Storage.
11. Click Next: Add Tag.
12. As Key put `Name` and as Value `MyNat`.
13. Click Next: Configure Security Group.
14. Select: Create a new security group.
15. As **Security group name** put `natsecuritygroup`.
16. Add 3 rules: SSH, HTTP, HTTPS.
17. Click: Review and Launch.
18. Click: Next.
19. Click: Launch.
20. Select your key pair and click Launch Instances.
21. Click View Instances.
22. Select your NAT instance.
23. Go to Actions - Networking and click on **Change Source/Dest. Check**.
24. Click Yes, Disable.

## Create a route for private subnets through the NAT instance
1. Go to VPC under Networking & Content Delivery.
2. Go to Route Tables on the left section.
3. Select the Main subnet of `awsworkshopvpc`.
4. On the bottom section go to the Routes tab.
5. Click Edit.
6. Click Add another Route.
7. As Destination put: `0.0.0.0/0`.
8. As Target select your NAT Instance.
9. Click Save.

---
**Next:** [create new Load Balancer](/workshop/vpc-subnets-bastion/04-load-balancer.md).
