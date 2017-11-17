# Finishing up

So now we have two instances of EC2, an ELB to distribute the traffic accross our instances, and a auto-scaling group to have redundancy and scale in an automatic way if performance need to increase.

On [section 1]() we used as API_URL the dns of our only instance, now we need to tell the web that the request must be done thru the load balancer, so we need to modify API_URL.
Also we need to modify the CodeDeploy project so he knows that now we have a auto-scaling group and that need to deploy on each of our instances.
Finally we need to re-run codebuild so the new bundle on s3 has the dns of the load-balancer instead of the instance dns.

## Create ALLOWED_HOSTS and modify API_URL
1. Go to EC2 under Computer section
2. On left menu select Load Balancer under LOAD BALANCING
3. Copy the DNS name of your load balancer appear under Description
4. On left menu select Parameter Store
5. click on /prod/frontend/API_URL and on Actions select Edit Parameter
6. as Value put: http:// + DNS that you copy 3 steps ago
7. click Save Parameter
8. click Create Parameter
9. as name put `/prod/api/ALLOWED_HOSTS`
10. as value put just the DNS you copy 7 steps ago inside a list between “ `[``"``<dns-of-your-load-balancer>``"``]`
11. click Create Parameter


## Modify the CodeDeploy project
1. Go to CodeDeploy under Developer Tools
2. click your application name
3. select your deployment group and on Actions select Edit
4. On Environment configuration select your Auto Scaling Group on Auto Scaling groups tag
5. Go to Amazon EC2 instances tag and delete all tag groups
6. check the Enable load balancing
7. on Load balancer check Application Load Balancer or Network Load Balancer
8. then select your target group on the drop down
9. click Save
10. select your deployment group and on Actions click Deploy new version
11. on Repository type select : My application is stored in github
12. Repository Name: tryolabs/aws-workshop
13. select last commit id
14. then click Deploy


## Re-run CodeBuild
1. Go to CodeBuild under Developer Tools
2. click Start build
3. click Start build

---
Next: [Create your own VPC with private and public subnets and a bastion to access thru SSH to your instances](/workshop/vpc-subnets-bastion/introduction.md)