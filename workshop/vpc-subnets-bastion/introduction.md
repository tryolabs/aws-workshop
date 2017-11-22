# Create a VPC, public and private subnets and a bastion to access to the instances thru SSH

In this section we want to improve a bit our security and redundancy. For this we are going to create a [custom VPC](https://aws.amazon.com/documentation/vpc/).

So this is what we are going to do, we will create our custom VPC, then we are going to create 2 private subnets (where our auto-scaling-group will put the Webserver instances) in different Availability Zones (for redundancy reasons).
Also we need 2 public subnets in the same availability zones (needed by the load balancer).

Then we will need a [Internet Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html) and create a new [Route Table](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html) so our public subnets are accesibles from outside.
We also will need a [Nat Instance](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html) so our Webservice Instances (inside our private subnets) can access to the internet (for example to be able to download needed packages).

We need to create a new configuration group and modify our auto-scaling-group so now on it deploy into our VPC in the right subnets.
Our RDC need to be moved to our VPC so our instances can reach it.

Then will add a [bastion instance](https://aws.amazon.com/blogs/security/how-to-record-ssh-sessions-established-through-a-bastion-host/) so we can access through ssh to our private instances.

Finally some changes need to be made on our CodeDeploy project so it deploy on our VPC as expected.

So, let's get started.

---
Next: [Create a VPC](/workshop/vpc-subnets-bastion/01-create-vpc.md)

