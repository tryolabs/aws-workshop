# EC2 instances

The API of our application will run on several [AWS EC2](https://aws.amazon.com/ec2/) instances. In this sections we will create one and deploy our API there using [CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html).

First we will create a role to allow our EC2 instances access to SSM:

1. Go to **IAM** under **Security, Identity & Compliance**
2. Go to Role section and click Create Role
3. Select EC2 and click next
4. Search for AmazonSSMReadOnlyAccess, select it and click next
5. Lets call it ApiRole. Click create Role

We have already created entries in the Parameter Store. In the future we will need encrypted variables, like the password for our database. That’s why we will create an encryption key to decrypt those values. That encryption key will be attached to our admin user and to the role we just created. You can read more about SSM and secure data [here](https://aws.amazon.com/blogs/compute/managing-secrets-for-amazon-ecs-applications-using-parameter-store-and-iam-roles-for-tasks/).

1. Go to the section **Encryption keys**
2. Select the same Region that you are working on and click Create key
3. Enter `workshopkey` as alias and `this is the encryption key for the aws workshop` as description.
4. Click next step and then next step again
5. Select both your AWS CLI and console users and click next
6. Select your EC2 Role and click next
7. Click Finish

In the future, if a EC2 instance with our new role wants to access an encrypted parameter, AWS will automatically decrypt it!

## Launch your first EC2 instance

We are ready to launch our first EC2 instance. We will create a standard EC2 instance, add a [startup script](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html) and finally create a [security group](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html) that will control the outbound and inbound in our EC2 instances.

1. Go to the **EC2** under **Compute section**
2. Click on Launch Instance
3. Look for Ubuntu Server (make sure it says Free tier eligible) and click Select
4. Select t2.micro and then click on Next: Configure Instance Details
5. Select our ApiRole on **IAM role**
6. On Advance Settings, there you have to select As text in User data and paste this bash script:
    #!/bin/bash
    export LC_ALL=C.UTF-8
    apt update
    apt -y install ruby
    cd /home/ubuntu
    wget https://aws-codedeploy-us-east-1.s3.amazonaws.com/latest/install
    chmod +x ./install
    ./install auto
7. Be careful, if you leave spaces at the beginning of the script it will not work. So NO SPACES
8. Click Next: Add Storage
9. Leave the default settings and click Next: Add Tags.
10. Click Add Tag.
11. Fill Key with  `service` and in Value with `api`.
12. Let’s add another tag with Key `environment` and Value `prod`. These keys will help us identify our EC2 instances running the API later
13. Click on Next: Configure Security Group
14. You can name the security group as you want
15. Click Add Rule
16. In port range put 9000 and in Source 0.0.0.0/0. This will enable the port 9000 from and out every IP. Security groups are stateful, so if we enable port 9000 it will be available for inbound and outbound traffic
17. Click Review and Launch
18. Click Launch
19. When asked to select an existing key pair, choose `create a new key pair`, give it a name and click download. Store it in a secure place, we will use it to ssh into the instances latter.
20. Click Launch Instances.
21. Wait until it starts
22. Click on the security group and copy the group-id to use it latter

---
Next: Create a [PostgresDB on RDS](/workshop/s3-web-ec2-api-rds/03-RDS.md)
