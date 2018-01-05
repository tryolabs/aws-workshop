# RDS

Now, we should move our RDS to the private subnets of our VPC. This way, we ensure that RDS is only accessible from these private subnets, and never from the outside world.

## Move RDS to your VPC
1. Open the [Amazon RDS console](https://console.aws.amazon.com/rds) and choose Subnet Groups on the left navigation pane.
2. Choose **Create DB Subnet Group**.
3. Enter the subnet name: `vpcsubnetgroup`.
4. As VPC ID: your VPC.
5. Then choose Availability Zone `us-east-1a` and Subnet Id `10.0.2.0-us-east-1a` and click Add.
6. Then choose Availability Zone `us-east-1b` and Subnet Id `10.0.4.0-us-east-1a` and click Add.
7. Click **Create**.
8. Go to Instances, select your RDS instance and on Instance Actions select Modify.
9. As Subnet Group select your `vpcsubnetgroup`.
10. Security Group: `default`.
11. Check Apply Immediately.
12. Click Continue.
13. Click Modify DB Instance.

---
**Next:** [Auto Scaling Group](/workshop/vpc-subnets-bastion/06-auto-scaling-group.md).
