# Auto Scaling Group

We are going to create a new Launch Configuration and Auto Scaling Group so that all our instances start only in our private subnets.

## Create a new Launch Configuration
1. Go to EC2 under Compute.
2. Go to Auto Scaling Groups on the left menu.
3. Delete the existing Auto Scaling group.
4. Go to Launch Configuration on the left menu.
5. Delete existing Launch Configuration.

Now, you need to create a new Launch Configuration that is almost identical to the one that you just deleted except for one thing: instead of creating a Security Group you need to choose the default one for your VPC.

There is no simple way to find it because your AWS account already has a default VPC with its default security group and at this stage of the Launch Configuration wizard there is no way to distinguish between your VPC's default group and the default group for the default VPC (🤔). To find the security group:

1. Go to **VPC** under **Networking & Content Delivery**.
2. Select **Security Groups** on the **Security** section on the left.
3. Search for a group with name `default` and VPC `vpc-ugly-id | awsworkshopvpc`.
4. Copy the **Group ID** value.

Once you have this Security Group Id, start the Launch Configuration creation wizard. Once you reach the _Click Next: Configure Security Group._ step, instead of creating a new security group choose **Select an existing security group** and look for the group with name _default_ and the same Id that you have. You can check the [previous instructions](/workshop/elb-auto-scaling-group/02-auto-scaling-group.md) if you need.

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
**Extra mile:**

- Why is the ASG only available on two subnets and not all of them?
- Why do we need this configuration of subnets anyway? (2 public and 2 private).

---
**Next:** [create a Bastion](/workshop/vpc-subnets-bastion/07-bastion.md) to be able to SSH into the private instances.

# Auto Scaling Group

우리의 모든 인스턴스가 우리의 개인 서브넷에서만 시작되도록 새로운 Launch Configuration and Auto Scaling Group을 만들 것입니다.

## Create a new Launch Configuration
1. AWS Management Console 에서 Compute 의 EC2 를 Click 하세요.
2. 왼쪽 메뉴 아래에 Auto Scaling Groups 를 Click 하세요.
3. 기존의 Auto Scaling group 은 삭제하세요.
4. 왼쪽 메뉴에서 Launch Configuration 을 Click 하세요.
5. Delete existing Launch Configuration.

Now, you need to create a new Launch Configuration that is almost identical to the one that you just deleted except for one thing: instead of creating a Security Group you need to choose the default one for your VPC.

There is no simple way to find it because your AWS account already has a default VPC with its default security group and at this stage of the Launch Configuration wizard there is no way to distinguish between your VPC's default group and the default group for the default VPC (🤔). To find the security group:

1. Go to **VPC** under **Networking & Content Delivery**.
2. Select **Security Groups** on the **Security** section on the left.
3. Search for a group with name `default` and VPC `vpc-ugly-id | awsworkshopvpc`.
4. Copy the **Group ID** value.

Once you have this Security Group Id, start the Launch Configuration creation wizard. Once you reach the _Click Next: Configure Security Group._ step, instead of creating a new security group choose **Select an existing security group** and look for the group with name _default_ and the same Id that you have. You can check the [previous instructions](/workshop/elb-auto-scaling-group/02-auto-scaling-group.md) if you need.

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
**Extra mile:**

- Why is the ASG only available on two subnets and not all of them?
- Why do we need this configuration of subnets anyway? (2 public and 2 private).

---
**Next:** [create a Bastion](/workshop/vpc-subnets-bastion/07-bastion.md) to be able to SSH into the private instances.