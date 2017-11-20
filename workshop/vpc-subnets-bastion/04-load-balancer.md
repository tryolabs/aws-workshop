# Load Balancer

At this point we need to create a Load Balancer to be able to route inbound request from web to our instances thru the Load Balancer.
 
## Create a new Load Balancer
1. Go to EC2 under Computer section
2. click on Load Balancers
3. click Create Load Balancer
4. click Create on Application Load Balancer
5. As Name put: aws-workshop-load-balancer-vpc
6. On Availability Zones on VPC select awsworkshopvpc
7. click on us-east-1a
8. click on 10.0.1.0-us-east-1a
9. Repeat steps 7 and 8 for us-east-1b and 10.0.3.0-us-east-1b
10. click Next: Configure Security Settings
11. click Next: Configure Security Groups
12. select Create a **new** security group and then click Next: Configure Routing
13. as name put: aws-workshop-target-group-vpc
14. as Port: 9000
15. as path: /api/tags
16. click Next: Register Targets
17. click Next: Review
18. click: Create
19. click: Close
20. select the new load balancer
21. Go to Description on bottom and find Security
22. Click Edit security groups
23. select default (both security groups must be select)
24. click Save
25. Delete old Load Balancer

## Modify ALLOWED_HOSTS and modify API_URL
1. Repeat the steps of [this section](/workshop/elb-auto-scaling-group/03-finishing-up.md) but modifying ALLOWED_HOSTS instead of creating it again.

---
Next: [Move RDS into your VPC](/workshop/vpc-subnets-bastion/05-RDS.md)