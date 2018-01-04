# Create Auto Scaling Group

Production applications need to be ready to tolerate a growing number of users at the same time. For example, if you get published in a popular blog, you may receive many more users that you had expected in a short period of time, and your application may crash because it's not able to sustain all the incoming traffic.

Amazon provides [Auto Scaling Groups](https://docs.aws.amazon.com/autoscaling/latest/userguide/AutoScalingGroup.html) as way to build a more robust application which can handle increasing loads. Using these, you can setup rules so more instances serving your application

To create an Auto Scaling Group, first we need to create a [Launch Configuration Group](http://docs.aws.amazon.com/autoscaling/latest/userguide/LaunchConfiguration.html), which is basically a template that specifies properties of the instances that will be launched.

## Create Launch Configuration group
1. Go to EC2 under Compute section.
2. On left menu select Launch Configuration under AUTO SCALING.
3. Click Create launch configuration.
4. Look for Ubuntu Server (make sure it say Free tier eligible) and click Select.
5. Select `t2.micro` and then click on Next: Configure Details.
6. As name put: `aws-workshop-auto-scaling-group`.
7. As IAM Role select: ApiRole.
8. On Advanced Settings, there you have to select As text in User data and paste this bash script:
    ```
    #!/bin/bash
    export LC_ALL=C.UTF-8
    apt update
    apt -y install ruby
    cd /home/ubuntu
    wget https://aws-codedeploy-us-east-1.s3.amazonaws.com/latest/install
    chmod +x ./install
    ./install auto
    ```

9. Be careful that there are NO SPACES before every line in the script.
10. Click Next: Add Storage.
11. Click Next: Configure Security Group.
12. Click : Create new security group.
13. Security Group Name: `api-security-group`.
14. Click: Add Rule.
15. Type: All TCP.
16. Source: load-balancer-security-group and select the one suggested.
17. Click Review.
17. Click Create launch configuration.

Now that we have our **Launch configuration group** we can create our **Auto Scaling Group**.

## Create Auto Scaling Group
1. Go to EC2 under Compute section.
2. On left menu select Auto Scaling Groups under AUTO SCALING.
3. Click: Create Auto Scaling group.
4. select: `aws-workshop-auto-scaling-group` and then click Next Step.
5. On Group name put the same as in Launch configuration.
6. Group size: 2.
7. Select 2 subnets.
8. Advanced Details click on: Receive traffic from one or more load balancers.
9. on Target Groups double click and select: `aws-workshop-target-group`.
10. Click Next: Configure scaling policies.
11. Select: **Use scaling policies to adjust the capacity of this group**.
12. Between 2 and 4.
13. Target value: 80.
14. Instances need: 180.
15. Click: Next: Configure Notifications.
16. Click: Next: Configure Tags.
17. Click: Review.
18. Click: Create Auto Scaling group.
19. Click: Close.

---
**Next:** [Finishing up, modify parameters and CodeDeploy project](/workshop/elb-auto-scaling-group/03-finishing-up.md)

