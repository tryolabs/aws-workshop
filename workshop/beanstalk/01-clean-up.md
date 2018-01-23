# Clan up

We have a pretty interesting infrastructure running now so in order to integrate Beanstalk we need to remove some services to make room. Our current setup has four major components: Elastic Load Balancer (ELB), Auto Scaling Group (ASG), Virtual Private Cloud (VPC) and Relational Database Service (RDS). As powerful as it is Beanstalk [can't setup VPCs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/vpc.html) for you and [is not recommend](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.RDS.html) for RDS other than for testing environments so we are going to keep these two and remove the ELB and ASG.

To remove the ELB:

1. On your AWS Console, go to **EC2** under **Compute**
2. Click on **Load Balancers** under **LOAD BALANCING**
3. Select the load balancer we create earlier. We use the name `aws-workshop-load-balancer`
4. Click **Actions**
5. Select **Delete**
6. Click **Yes, Delete**

Now do the same for the **Target Groups**, **Launch Configurations** and **Auto Scaling Groups**.

Once you completely remove the ELB and ASG we need to terminate the EC2 instances we have running.

1. Go to **EC2** under **Compute**
2. Click on **Instances**
3. Using the checkbox at the left select all the instances that aren't the Bastion (if you have it running) and the NAT instance.
4. Click **Actions**
5. Click **Instance State**
6. Click Terminate
7. Click **Yes, Terminate**

Next we are going to setup our application with a production environment.

---
**Extra mil:** when all the instances were terminated remove all the security groups that aren't needed anymore. Could you leave your setup broken by doing this?

---
**Next:** [create a new app](/workshop/beanstalk/02-new-app-environment.md)