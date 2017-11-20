# Bastion

Now we are going to add a Bastion so we can access thru S3 to our private instances.
A Bastion is basically a instance located in one of our public subnets, will be able to ssh provate instances because, private instances allow all traffic from the inside of our VPC.


## Create a Bastion Instance
1. Go to the **EC2** under **Compute section**
2. Click on Launch Instance
3. Look for Ubuntu Server (make sure it says Free tier eligible) and click Select
4. Select t2.micro and then click on Next: Configure Instance Details
5. on Network select your VPC
6. as subnet select 10.0.1.0-us-east-1a
8. Click Next: Add Storage
9. Leave the default settings and click Next: Add Tags.
10. Click Add Tag.
11. Fill Key with  `Name` and in Value with `bastion`.
12. Click on Next: Configure Security Group
13. Click Review and Launch
14. Click Launch
15. Select your keypair and click Launch Instances.
16. Select the Bastion on the instances list and on Actions/Networking select Change Security Groups.
17. Check the default security group of your VPC (make sure that 2 security groups are checked, the one you just created and the one you created during the creation of the bastion).

## Add pem to your bastion instance

Now you have a public instance that can be access via ssh, but what you want is to be able to access to your private instances.

1. Open your keypair (.pem file you downloaded) on your machine and copy the content of it.
2. ssh to your bastion `ssh ubuntu@<public-ip-of-the-bastion> -i <pem-file-name>`
3. Create a new file with the same name of your pem file and paste the content of it inside.
4. now run `chmod 400 <pem-file-name>`
5. now you can ssh to any of your 2 instances from your bastion: `ssh <private-ip-of-webserver-instance> -i <pem-file-name>`

---
Next: [Finishing our deploy with VPC, junt need to modify our CodeDeploy project and re-build](/workshop/vpc-subnets-bastion/08-finishing-up.md)