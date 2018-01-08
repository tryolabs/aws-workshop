# Load Balancer

At this point, we need to create a Load Balancer to be able to route request from the web to our instances.

## Create a new Load Balancer
1. Go to EC2 under Computer section.
2. Click on Load Balancers.
3. Click Create Load Balancer.
4. Click Create on Application Load Balancer.
5. As Name put: `aws-workshop-load-balancer-vpc`.
6. On Availability Zones, on VPC select `awsworkshopvpc`.
7. Click on `us-east-1a`.
8. Click on `10.0.1.0-us-east-1a`.
9. Repeat steps 7 and 8 for `us-east-1b` and `10.0.3.0-us-east-1b`.
10. Click Next: Configure Security Settings.
11. Click Next: Configure Security Groups.
12. Select Create a **new** security group and then click Next: Configure Routing.
13. As name put: `aws-workshop-target-group-vpc`.
14. As Port: `9000`.
15. As path: `/api/tags`.
16. Click Next: Register Targets.
17. Click Next: Review.
18. Click: Create.
19. Click: Close.
20. Select the new load balancer.
21. Go to Description on bottom and find Security.
22. Click Edit Security Groups.
23. Select default (so that both security groups are selected).
24. Click Save.
25. Delete old Load Balancer.

## Modify API_URL
Repeat the steps outlined in [this section](/workshop/elb-auto-scaling-group/03-finishing-up.md).

---
**Next:** [move RDS into your VPC](/workshop/vpc-subnets-bastion/05-RDS.md).