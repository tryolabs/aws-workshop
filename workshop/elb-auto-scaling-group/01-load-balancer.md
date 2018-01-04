# Create a Load Balancer

Elastic Load Balancing automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, and IP addresses. When you are running applications in production, you typically will use multiple instances so if one fails, your application can still work. The Load Balancer will get the traffic, and will forward it to the instances that serve your app. You can more about this [here](https://aws.amazon.com/elasticloadbalancing/).

1. Go to EC2 under Compute section.
2. On left menu select Load Balancers under LOAD BALANCING.
3. Click Create Load Balancer.
4. Select Application Load Balancer.
5. As name put: aws-workshop-load-balancer.
6. Select at least 2 Availability zones.
7. Click Next: Configure Security Settings.
8. Click Next: Configure Security Groups.
9. Select "Create a new security group" and as name put `load-balancer-security-group` and add a description.
10. Click Next: Configure Routing.
11. As name put: `aws-workshop-target-group`.
12. As Port: `9000`.
13. As path: `/api/tags`.
14. Click Next: Register Targets.
15. Click Next: Review.
16. Click: Create.
17. Click: Close.

---
**Next:** [create an Auto Scaling Group](/workshop/elb-auto-scaling-group/02-auto-scaling-group.md).
