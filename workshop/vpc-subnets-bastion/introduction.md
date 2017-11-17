# Create a VPC, public and private subnets and a bastion to access to the instances thru SSH


## Create a VPC
1. Go to VPC under Networking & Content Delivery
2. go to Your VPCs on the left section
3. click on Create VPC
4. As **Name** **tag** put : awsworkshopvpc
5. As **IPv4 CIDR** **block*** put : 10.0.0.0/16
6. then click:  Yes, Create


## Create 4 subnets (2 public and 2 private)
1. Go to Subnets on the left section
2. Click Create Subnet
3. as **Name tag** put: 10.0.1.0-us-east-1a
4. **Availability Zone**: us-east-1a
5. As **IPv4 CIDR** **block** put :10.0.1.0/24
6. then click in Yes, Create
7. repeat steps 2-6 using as **Name tag**: 10.0.2.0-us-east-1a, **Availability Zone**: us-east-1a and **IPv4 CIDR block**: 10.0.2.0/24
8. repeat steps 2-6 using as **Name tag**: 10.0.3.0-us-east-1b, **Availability Zone**: us-east-1b and **IPv4 CIDR block**: 10.0.3.0/24
9. repeat steps 2-6 using as **Name tag**: 10.0.4.0-us-east-1b, **Availability Zone**: us-east-1b and **IPv4 CIDR block**: 10.0.4.0/24


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


## Create Nat Instances
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
## Create a new Load Balancer
1. Go to EC2 under Computer section
2. click on Load Balancers
3. click Create Load Balancer
4. click Create on Application Load Balancer
5. As Name put: aws-workshop-load-balancer-vpc
6. On Availability Zones on VPC select awsworkshopvpc
7. click on us-east-1a
8. click on 10.0.1.0-us-east-1a
9. Repeat steps 7 and 8 for us-east-1b and 10.0.3.0-us-east-1b
10. click Next: Configure Security Settings
11. click Next: Configure Security Groups
12. select Create a **new** security group and then click Next: Configure Routing
13. as name put: aws-workshop-target-group-vpc
14. as Port: 9000
15. as path: /api/tags
16. click Next: Register Targets
17. click Next: Review
18. click: Create
19. click: Close
20. select the new load balancer
21. Go to Description on bottom and find Security
22. Click Edit security groups
23. select default (both security groups must be select)
24. click Save
25. Delete old Load Balancer


## Create Launch Configuration group
1. Go to EC2 under Compute
2. Go to Auto Scaling  Groups on the left menu
3. Delete current Auto Scaling group
4. go to Launch Configuration on the left menu
5. Delete current launch configuration group
6. Repeat the same steps on the this [section](/doc/AWS-step-by-step-QGz9JlByckihA5wECLa0t#:uid=667829228291196733706042&h2=Create-Launch-Configuration-gr) but select the default security group of your VPC


## Modify ALLOWED_HOSTS and modify API_URL
1. Repeat the steps of [this section](/doc/AWS-step-by-step-QGz9JlByckihA5wECLa0t#:uid=592345444282380594079288&h2=Create-ALLOWED_HOSTS-and-modif) but modifying ALLOWED_HOSTS instead of creating it again.


## Move RDS to your VPC
1. Open the [Amazon RDS console](https://console.aws.amazon.com/rds) and choose Subnet Groups from the left navigation pane.
2. Choose **Create DB Subnet Group**.
3. Enter the subnet name: vpcsubnetgroup
4. As VPC ID: your VPC
5. Then choose Availability Zone us-east-1a and Subnet Id : 10.0.2.0-us-east-1a and click Add
6. Then choose Availability Zone us-east-1b and Subnet Id : 10.0.4.0-us-east-1a and click Add
7. Click **Create**.
8. Go to Instances, select your RDS instance and on Instance Actions select Modify
9. As Subnet Group select your vpcsubnetgroup
10. Security Group: default
11. Check Apply Immediately
12. Click Continue
13. Click Modify DB Instance
## Create Auto Scaling Group
1. Go to EC2 under Compute section
2. On left menu select Auto Scaling Groups under AUTO SCALING
3. click : Create Auto Scaling group
4. select: aws-workshop-auto-scaling-group and then click Next Step 
5. On Group name put the same as in Launch configuration
6. Group size: 2
7. Network: awsworkshopvpc
8. Subnet: 10.0.2.0-us-east-1a and 10.0.4.0-us-east-1b
9. Advanced Details click on: Receive traffic from one or more load balancers
10. on Target Groups double click and select : aws-workshop-target-group-vpc
11. click Next: Configure scaling policies
12. select: **Use scaling policies to adjust the capacity of this group**
13. between 2 and 4
14. Target value: 80
15. Instances need: 180
16. click: Next: Configure Notifications
17. click: Next: Configure Tags
18. click: Review
19. click: Create Auto Scaling group
20. click: close
## Modify the CodeDeploy project
1. Go to CodeDeploy under Developer Tools
2. click your application name
3. select your deployment group and on Actions select Edit
4. On Environment configuration select your Auto Scaling Group on Auto Scaling groups tag
5. Go to Amazon EC2 instances tag and delete all tag groups
6. check the Enable load balancing
7. on Load balancer select your target group on the drop down
8. click Save
9. select your deployment group and on Actions click Deploy new version
10. on Repository type select : My application is stored in github
11. Repository Name: tryolabs/aws-workshop
12. select last commit id
13. then click Deploy


## Re-run CodeBuild
1. Go to CodeBuild under Developer Tools
2. click Start build
3. click Start build
