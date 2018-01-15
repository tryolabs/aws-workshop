# EC2 instances

The API of our application will run on several [AWS EC2](https://aws.amazon.com/ec2/) instances. In the sections that follow, we will create one and deploy our API there using [CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html).

First we will create a role to allow our EC2 instances access to SSM:

1. Go to **IAM** under **Security, Identity & Compliance**.
2. Go to Role section and click Create Role.
3. Select **AWS Service** and then **EC2**.
4. Under **Select your use case**, select the one that says _"Allows EC2 instances to call AWS services on your behalf."_ and click next.
5. Search for `AmazonSSMReadOnlyAccess`, select it and click next.
6. Lets call it `ApiRole`. Click create Role.

We have already created entries in the Parameter Store. In the future we will need encrypted variables, like the password for our database. For this, will create an encryption key to encrypt and decrypt those values. That encryption key will be attached to our admin user and to the role we just created, so only services that are setup to assume the role can get access to the decrypted values. You can read more about SSM and secure data [here](https://aws.amazon.com/blogs/compute/managing-secrets-for-amazon-ecs-applications-using-parameter-store-and-iam-roles-for-tasks/).

1. Go to the section **Encryption keys**.
2. Select **Create key**.
3. Enter `workshopkey` as alias and a meaningful description like "this is the encryption key for the AWS workshop".
4. Click next step and then next step again.
5. Select both your AWS CLI and console users and click next.
6. Select your EC2 Role and click next.
7. Click Finish.

In the future, if an EC2 instance with our new role wants to access an encrypted parameter, AWS will automatically decrypt it!

## Launch your first EC2 instance

We are ready to launch our first EC2 instance. We will create a standard EC2 instance, add a [startup script](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html) (which will run automatically when the instance boots) and finally create a [security group](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html) that will control the outbound and inbound in our EC2 instances.

1. Go to the **EC2** under **Compute section**, and in the top right corner, you can pick the region we are going to use. In this case, we will be using the same region that we used for the S3 bucket setup earlier, that is, `US East (N. Virginia)`.
2. Click on Launch Instance.
3. Look for Ubuntu Server (make sure it says Free tier eligible) and click Select.
4. Select `t2.micro` and then click on Next: Configure Instance Details.
5. Select our `ApiRole` on **IAM role**.
6. On Advanced Details, select "As text" in User data and then paste the following bash script:
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

    Be careful, if you leave spaces at the beginning of the script it will not work. So NO SPACES!
    If you had used another region, the bucket name in the `wget` line would be different (see [here](https://docs.aws.amazon.com/codedeploy/latest/userguide/resource-kit.html#resource-kit-bucket-names)).

7. Click Next: Add Storage.
8. Leave the default settings and click Next: Add Tags.
9. Click Add Tag.
10. Fill Key with `service` and in Value with `api`.
11. Add another tag with Key `environment` and Value `prod`. These keys will help us identify our EC2 instances running the API later.
12. Click on Next: Configure Security Group.
13. Make sure the _Create a new security group_ option is selected and write a descritive name on the _Security group name:_ field. You cannot rename it later so choose the name wisely.
14. Click Add Rule.
15. In port range put `9000` and in Source `0.0.0.0/0`, and add a meaningful description. This will enable incoming traffic on port 9000 from every IP, so you can "contact" your instance from the outside. If you pay attention, by default we also get a rule allowing inbound traffic on port 22, which we will use for SSH'ing to the instance. Also by default, outbound traffic (that is, traffic originating from your instance) will be allowed to any destination and port, but you could restrict that later by editing the outbound rules for the security group.
16. Click Review and Launch.
17. Click Launch.
18. When asked to select an existing key pair, choose `create a new key pair`, give it as name `aws_workshop` and click download. Store it in a secure place (`~/.ssh` is good, but make sure you `chmod 400` the PEM file so only your user can read it), we will use it to SSH into the instances during the whole workshop.
19. Click Launch Instances.

---
**Extra mil:**

- Try `pin`ging your EC2 instance. Extra points for make it work.
- Loggin with `ssh` to the new instance, username: _ubuntu_ try the `-i` flag to use the .pem file.

---
**Next:** create a [PostgresSQL database on RDS](/workshop/s3-web-ec2-api-rds/03-RDS.md).
