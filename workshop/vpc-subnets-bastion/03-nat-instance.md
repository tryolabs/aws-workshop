# Nat Instance

Until now we have 2 public subnets and 2 private subnets, in our private subnets we will deploy the Webserver instances that will be accesible via a Load Balancer.
Even if this instances doesn't need to be reachable from outiside of the VPC, they need to have internet access to download and update packages. For this reason we need a Nat to route all external outbound traffic thru it.

About Nat options, AWS offer us two options [Nat Instance](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html) and [Nat Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html).
Nat Gateway is newer and easier than Nat Instance and automatically scales, but for a pricing reason we will select Nat Instance (we can create a Nat Instance for free).

## Create Nat Instance
1. Go to EC2 under Computer section
2. click on Instances on the left menu
3. click Launch Instance
4.  select Community AMIs
5. type nat and then  hit Enter
6. select the first one that appear:
  1. Root device type: ebs 
  2. Virtualization type: hvm 
  3. ENA Enabled: No
7. select t2.micro and click Next: Configure Instace Details
8. on Network select your VPC
9. as subnet select 10.0.1.0-us-east-1a
10. click Next: Add Storage
11. click Next: Add Tag
12. as Key put Name and as Value : MyNat
13. click Next: Configure Security Group
14. select: Create a new security group
15. as **Security group name** put natsecuritygroup
16. add 3 rules: SSH, HTTP, HTTPS
17. click: Review and Launch
18. click: Next
19. click: Launch
20. select your keypair and click Launch Instances
21. click View Instances
22. select your Nat instance
23. go to Actions - Networking and click on **Chance Source/Dest. Check**
24. click Yes, Disable

## Create a Route for private subnets thru Nat the instance
1. Go to VPC under Networking & Content Delivery
2. Go to Route Tables on the left section
3. select the Main subnet of awsworkshopvpc
4. On the bottom section go to the Routes tab
5. click Edit
6. click Add another Route
7. As Destination put: 0.0.0.0/0
8. and as Target select your Nat Instance
9. click Save

---
**Next:** [Create new Load Balancer](/workshop/vpc-subnets-bastion/04-load-balancer.md)
