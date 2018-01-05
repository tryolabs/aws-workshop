# Auto Scaling Group

We are going to create a new Launch Configuration and Auto Scaling Group so that all our instances start only in our private subnets.

## Create Launch Configuration group
1. Go to EC2 under Compute.
2. Go to Auto Scaling Groups on the left menu.
3. Delete the existing Auto Scaling group.
4. Go to Launch Configuration on the left menu.
5. Delete existing Launch Configuration group.
6. Repeat the same steps from this [section](/workshop/elb-auto-scaling-group/02-auto-scaling-group.md), but select the default security group of your VPC.

## Create Auto Scaling Group
1. Go to EC2 under Compute section.
2. On left menu select Auto Scaling Groups under AUTO SCALING.
3. Click: Create Auto Scaling group.
4. Select: `aws-workshop-auto-scaling-group` and then click Next Step.
5. On Group name put the same as in Launch configuration.
6. Group size: 2.
7. Network: `awsworkshopvpc`.
8. Subnet: `10.0.2.0-us-east-1a` and `10.0.4.0-us-east-1b`.
9. Advanced Details click on: Receive traffic from one or more load balancers.
10. On Target Groups double click and select: `aws-workshop-target-group-vpc`.
11. Click Next: Configure scaling policies.
12. Select: **Use scaling policies to adjust the capacity of this group**.
13. Between 2 and 4.
14. Target value: 80.
15. Instances need: 180.
16. Click: Next: Configure Notifications.
17. Click: Next: Configure Tags.
18. Click: Review.
19. Click: Create Auto Scaling group.
20. Click: close.

---
**Next:** [create a Bastion](/workshop/vpc-subnets-bastion/07-bastion.md) to be able to SSH into the private instances.
