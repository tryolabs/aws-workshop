# Finishing up
# 마무리

Now, we have two instances on EC2, an ELB to distribute the traffic across them, and an Auto Scaling Group to have redundancy and scale in an automatic way if throughput needs to increase.

In [the first section](/workshop/s3-web-ec2-api-rds/05-finishing-up.md), the `API_URL` parameter was set to the DNS name of our only instance. Now, we need to tell the web that the request must be done through the load balancer, so we need to modify `API_URL`.
We also need to modify the CodeDeploy project so the tool knows that now we have an Auto Scaling Group and that it needs to run the deploy each time a new instance is launched.
Finally, we need to re-run CodeBuild so the new bundle on S3 points to the DNS of the load balancer instead of the instance' DNS.

## Modify `API_URL`
1. Go to **EC2** under **Computer** section.
2. On left menu select **Load Balancer** under **LOAD BALANCING**.
3. Copy the DNS name of your load balancer that appears under **Description**.
4. On left menu, select **Parameter Store**.
5. Click on `/prod/frontend/API_URL` and on **Actions** select **Edit Parameter**.
6. As Value put: `http://` + the DNS that you copied 3 steps ago.
7. Click **Save Parameter**.

## Modify the CodeDeploy project
1. Go to **CodeDeploy** under **Developer Tools**.
2. Click your application's name.
3. Select your deployment group and on **Actions** select **Edit**.
4. On **Environment configuration** select your Auto Scaling Group on **Auto Scaling groups** tab.
5. Go to **Amazon EC2 instances** tab, and delete all existing Tag groups that we setup earlier.
6. Check **Enable load balancing**.
7. On **Load balancer** check **Application Load Balancer**.
8. Select your target group in the dropdown.
9. Click **Save**.
10. Select your deployment group and on **Actions** click **Deploy new version**.
11. On **Repository** type select: `My application is stored in GitHub`.
12. Repository Name: `tryolabs/aws-workshop`.
13. Get the last commit id and past it in the **Commit ID** field.
14. Then click **Deploy**.

## Re-run CodeBuild
1. Go to **CodeBuild** under **Developer Tools**.
2. Click **Start build**.
3. Click **Start build**.

## Update RDS security group
To give access to the instances created by the auto scaling to the data base we need to update our Postgres instance security group.

1. Go to **RDS** under **Database**
2. Click **Instances** on the left
3. Select your instance and with the radio button on the left and click **Instance actions** and select **Modify**
4. Scroll to **Security group** under **Network & Security** section
5. Click on the security groups drop down and select `api-security-group`. This is the group we created with the Launch Configuration for our Auto Scaling Group in the [previous section](/workshop/elb-auto-scaling-group/02-auto-scaling-group.md#create-launch-configuration-group).

Now, terminate all your running instances and wait for the Auto Scaling group to start the new ones, this might take some minutes. You can follow the current state of the ASG by going to **EC2**, **Auto Scaling Groups**, select your group and check the **Activity History** and **Instances** tabs. Once the new instances were in place and `running` you should be able to get the full site working on the URL of the load balancer.

---
**Extra mile:** once you have the site running:

- Can you tell which instance is getting the requests?
- Try changing the _Desired_ and _Min_ parameters of the ASG and see what happens.
- Force the launch of new instances by triggering a condition that would make the scale up policy activate (that is, without changing the _Desired_ value).
  > Tip: running `yes > /dev/null &` will max out one of the CPU cores.

- Try running [ab](http://httpd.apache.org/docs/2.2/programs/ab.html) (installed by default on macOS) to stress test the API. Do you see any reaction in the AWS console?

---
**Next:** [VPC configuration and Bastion instance](/workshop/vpc-subnets-bastion/introduction.md).