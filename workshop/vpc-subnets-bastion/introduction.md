# VPC and *bastion* instance

The aim of this section is to improve a bit our security and redundancy. For this we are going to create a [custom VPC](https://aws.amazon.com/documentation/vpc/).

Once we have our VPC, we will create 2 private subnets (where our Auto Scaling Group will launch the web server instances) in different Availability Zones (for redundancy reasons). We will also setup 2 public subnets in the same availability zones, which are needed by the load balancer. You can read more about VPC and subnets [here](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html).

For our public subnets, we will need to setup an [Internet Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html) and create a new [Route Table](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html), so any instance in the subnet can access the Internet.

Since our application's instances will live in the **private** subnets, we also will need a [NAT Instance](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html) that will route their Internet traffic through the public subnets. We need our instances to access the Internet so that we can download packages, update our system, etc.

We need to create a new Launch Configuration and modify our Auto Scaling Group so from now on it deploys to our VPC in the right subnets. Also, our RDS (PostgreSQL database) needs to be moved to our VPC so our instances can reach it.

To access our instances through SSH from the outside world, we will add a [bastion instance](https://aws.amazon.com/blogs/security/how-to-record-ssh-sessions-established-through-a-bastion-host/). Since the bastion has direct access to the instances, we can access them by accessing the bastion first.

Finally, some changes need to be made to our CodeDeploy project so it deploys to our VPC, as expected.

So, let's get started.

---
**Next:** [create a VPC](/workshop/vpc-subnets-bastion/01-create-vpc.md).

