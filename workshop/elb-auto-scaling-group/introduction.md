
# Add an extra EC2 instance with ELB and auto-scaling


## Create auto-scaling group
1. Go to EC2 under Compute section
2. On left menu select Auto Scaling Groups under AUTO SCALING
3. Click Create Auto Scaling group
4. Click Create launch configuration
5. Look for Ubuntu Server (make sure it say Free tier eligible) and click Select.
6. Select t2.micro and then click on Next: Configure Details.
7. As name put: aws-workshop-auto-scaling-group
8. As IAM Role select: ApiRole
9. On Advance Settings, there you have to select As text in User data and paste this bash script:
    #!/bin/bash
    export LC_ALL=C.UTF-8
    apt update
    apt -y install ruby
    cd /home/ubuntu
    wget https://aws-codedeploy-us-east-1.s3.amazonaws.com/latest/install
    chmod +x ./install
    ./install auto
10. Be carefull that there are NO SPACES before every line in the script.
11. Click Next: Add Storage
12. Click Next: Configure Security Group
13. Click : Select an existing security group and pick up the same one you have on the old EC2 instance then click Review.
14. Click Create launch configuration
15. select the key pair your where using and then click Create launch configuration.
16. On Group name put the same as in Launch configuration
17. Group size: 2