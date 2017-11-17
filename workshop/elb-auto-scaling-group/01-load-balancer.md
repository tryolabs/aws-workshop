# Create a Load Balancer

1. Go to EC2 under Compute section
2. On left menu select Load Balancers under LOAD BALANCING
3. Click Create Load Balancer
4. Select Application Load Balancer
5. As name put: aws-workshop-load-balancer
6. click Next: Configure Security Settings
7. click Next: Configure Security Groups
8. pick up : Create a **new** security group and click Next: Configure Routing
9. as name put: aws-workshop-target-group
10. as Port: 9000
11. as path: /api/tags
12. click Next: Register Targets
13. click Next: Review
14. click: Create
15. click: Close

---
Next: [Create Auto Scaling Group](/workshop/elb-auto-scaling-group/02-auto-scaling-group.md)
