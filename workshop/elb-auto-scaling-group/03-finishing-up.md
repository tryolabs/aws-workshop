# Finishing up

Now, we have two instances on EC2, an ELB to distribute the traffic across them, and an Auto Scaling Group to have redundancy and scale in an automatic way if throughput needs to increase.

On [section 1](/workshop/s3-web-ec2-api-rds/05-finishing-up.md), the `API_URL` parameter was set to the DNS name of our only instance. Now, we need to tell the web that the request must be done through the load balancer, so we need to modify `API_URL`.
We also need to modify the CodeDeploy project so the tool knows that now we have an Auto Scaling Group and that it needs to run the deploy on each of the instances in the group.
Finally, we need to re-run CodeBuild so the new bundle on S3 points to the DNS of the load balancer instead of the instance' DNS.

## Modify `API_URL`
1. Go to EC2 under Computer section.
2. On left menu select Load Balancer under LOAD BALANCING.
3. Copy the DNS name of your load balancer that appears under Description.
4. On left menu, select Parameter Store.
5. Click on `/prod/frontend/API_URL` and on Actions select Edit Parameter.
6. As Value put: `http://` + the DNS that you copied 3 steps ago.
7. Click Save Parameter.

## Modify the CodeDeploy project
1. Go to CodeDeploy under Developer Tools.
2. Click your application's name.
3. Select your deployment group and on Actions select Edit.
4. On Environment configuration select your Auto Scaling Group on Auto Scaling groups tab.
5. Go to Amazon EC2 instances tab, and delete all existing Tag groups that we setup earlier.
6. Check Enable load balancing.
7. On Load balancer, check Application Load Balancer or Network Load Balancer.
8. Select your target group in the dropdown.
9. Click Save.
10. Select your deployment group and on Actions click Deploy new version.
11. On Repository type select: My application is stored in GitHub.
12. Repository Name: `tryolabs/aws-workshop`.
13. Select last commit id.
14. Then click Deploy.

## Re-run CodeBuild
1. Go to CodeBuild under Developer Tools.
2. Click Start build, twice.

---
**Next:** [VPC configuration and Bastion instance](/workshop/vpc-subnets-bastion/introduction.md).