# Create a Load Balancer

1. Go to EC2 under Compute section
2. On left menu select Load Balancers under LOAD BALANCING
3. Click Create Load Balancer
4. Select Application Load Balancer
5. As name put: aws-workshop-load-balancer
6. Select at least 2 Availability zones
7. click Next: Configure Security Settings
8. click Next: Configure Security Groups
9. pick up : Create a **new** security group and as name put: load-balancer-security-group and a description
10. click Next: Configure Routing
11. as name put: aws-workshop-target-group
12. as Port: 9000
13. as path: /api/tags
14. click Next: Register Targets
15. click Next: Review
16. click: Create
17. click: Close

---
Next: [Create Auto Scaling Group](/workshop/elb-auto-scaling-group/02-auto-scaling-group.md)
