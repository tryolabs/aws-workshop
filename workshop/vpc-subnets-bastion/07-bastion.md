# Bastion instance

A bastion is a regular EC2 instance located in one of the public subnets, which allows incoming traffic through SSH. Through this instance, we will be able to SSH into any instance located in the private subnet (assuming they accept incoming traffic from the bastion).

## Create a Bastion Instance
1. Go to **EC2** under **Compute section**.
2. Click on Launch Instance.
3. Look for Ubuntu Server (make sure it says Free tier eligible) and click Select.
4. Select `t2.micro` and then click on Next: Configure Instance Details.
5. On Network, select your VPC.
6. As subnet, you can pick any of the two public ones. For example, `10.0.1.0-us-east-1a`.
8. Click Next: Add Storage.
9. Leave the default settings and click Next: Add Tags.
10. Click Add Tag.
11. Fill Key with `Name` and in Value with `bastion`.
12. Click on Next: Configure Security Group.
13. Click Review and Launch.
14. Click Launch.
15. Select your key pair and click Launch Instances.
16. Select the Bastion on the instances list and on Actions/Networking select Change Security Groups.
17. Check the default security group of your VPC. Make sure that 2 security groups are checked, the one you just created and the one you created during the creation of the bastion.

## Accessing private instances through the bastion

Now you have a public instance that can be accessed via SSH, but what you want is to be able to access to your private instances.

To access the instances, you need to SSH with the PEM (key pair) that you had generated when launching the first one.

### Option 1: setup SSH agent forwarding
You can read a guide [here](https://developer.github.com/v3/guides/using-ssh-agent-forwarding/). Even though the examples check access to GitHub, it's analogous to accessing our private instances.

You can setup SSH so it's easier to access protected instances going transparently through the bastion. [Here](https://www.cyberciti.biz/faq/linux-unix-ssh-proxycommand-passing-through-one-host-gateway-server/) you have a nice guide.

### Option 2: copy the PEM file from your machine to the bastion instance
Ideally, you would be using a different PEM file for the bastion and the instances (increased security).

1. Copy the file with `scp ~/.ssh/<your-pem-file>.pem ubuntu@<public-ip-of-the-bastion>:/home/ubuntu/.ssh`.
2. SSH into the bastion.
2. Make sure the file permissions are correct: `chmod 400 <pem-file-name>`.
3. SSH into the instances (from the bastion) with `ssh <private-ip-of-webserver-instance> -i <pem-file-name>`.

---

**Next:** [finish the deploy](/workshop/vpc-subnets-bastion/08-finishing-up.md).