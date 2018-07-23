# Auto Scaling Group 생성

Production applications need to be ready to tolerate a growing number of users at the same time. For example, if you get published in a popular blog, you may receive many more users that you had expected in a short period of time, and your application may crash because it's not able to sustain all the incoming traffic.

Amazon provides [Auto Scaling Groups](https://docs.aws.amazon.com/autoscaling/latest/userguide/AutoScalingGroup.html) as way to build a more robust application which can handle increasing loads. Using these, you can setup rules (scaling policies) so more instances serving your application

To create an Auto Scaling Group, first we need to create a [Launch Configuration](http://docs.aws.amazon.com/autoscaling/latest/userguide/LaunchConfiguration.html), which is basically a template that specifies properties of the instances that will be launched.

## Create Launch Configuration
1. Go to **EC2** under **Compute** section.
2. On left menu select **Launch Configuration** under **AUTO SCALING**.
3. Click **Create launch configuration**.
4. Look for Ubuntu Server (make sure it say Free tier eligible) and click Select.
5. Select `t2.micro` and then click on **Next: Configure Details**.
6. As name put: `aws-workshop-auto-scaling-group`.
7. As **IAM Role** select: `ApiRole`.
8. On **Advanced Settings**, there you have to select **As text** in **User data** and paste this bash script:
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
    Be careful that there are NO SPACES before every line in the script.
9. Click **Next: Add Storage**.
10. Click **Next: Configure Security Group**.
11. Click **Create new security group**.
12. Security Group Name: `api-security-group`.
13. Click: **Add Rule**.
14. Type: **All TCP**.
15. Source: `load-balancer-security-group` and select the one suggested.
16. Click **Review**.
17. Click **Create launch configuration** and select the key pair to used to `ssh` into future instances.

Now that we have our **Launch configuration** we can create our **Auto Scaling Group**.

## Create Auto Scaling Group
1. Go to **EC2** under **Compute** section.
2. On left menu select **Auto Scaling Groups** under **AUTO SCALING**.
3. Click: **Create Auto Scaling group**.
4. Select: `aws-workshop-auto-scaling-group` and then click **Next Step**.
5. On **Group name** put the same as in Launch configuration.
6. **Group size:** 2. At least we will have some redundancy form the start!
7. On **Subnet** add all the available options.
8. On **Advanced Details** click on: **Receive traffic from one or more load balancers**.
9. On **Target Groups** click and select: `aws-workshop-target-group`.
10. Click **Next: Configure scaling policies**.
11. Select: **Use scaling policies to adjust the capacity of this group**. We will configure a toy scaling policy only for learning. In a real system, you would have to do some benchmarking and determine your application's bottlenecks to setup an optimal scaling policy.
12. Configure it to scale between 2 and 4 instances.
13. Pick `Average CPU Utilization` as metric (imagine your app was compute intensive). In Target value, set something like 80.
14. **Instances need:** 180 seconds for warm up. See more [here](https://docs.aws.amazon.com/autoscaling/latest/userguide/as-scaling-simple-step.html#as-step-scaling-warmup).
15. Click **Next: Configure Notifications**.
16. Click **Next: Configure Tags**.
17. Click **Review**.
18. Click **Create Auto Scaling group**.
19. Click **Close**.

---
**Next:** finishing up, we need to [modify parameters and re-run CodeBuild](/workshop/elb-auto-scaling-group/03-finishing-up.md).

