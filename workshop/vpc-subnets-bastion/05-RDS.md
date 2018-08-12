# RDS

이제 RDS를 VPC의 개인 서브넷으로 이동해야합니다. 이렇게하면 RDS가 외부 전용이 아닌 개인 서브넷에서만 액세스 할 수 있습니다.

## RDS를 여러분의 VPC로 이동시키기
1. AWS Management Console 에서 [Amazon RDS console](https://console.aws.amazon.com/rds) 을 열고 왼쪽 메뉴에서 Subnet Groups 을 선택하세요.
2. **Create DB Subnet Group** 을 선택하세요.
3. Enter the subnet name: `vpcsubnetgroup` 을 입력하거나 원하시는 것을 입력하세요.
4. VPC ID: your VPC 를 선택하세요.
5. 이후 Availability Zone `ap-northeast-1a` 와 Subnet Id `10.0.2.0-ap-northeast-1a` 을 선택하고 Click 하여 추가하세요.
6. 이후 Availability Zone `ap-northeast-1b` 와 Subnet Id `10.0.4.0-ap-northeast-1a` 를 선택하고 Click 하여 추가하세요.
7. **Create** Click 하세요.
8. 왼쪽 메뉴에서 Instances 로 이동하고, RDS instance 와 Instance Actions Modify 를 선택하세요.
9. Subnet Group 에서 `vpcsubnetgroup` 을 선택하세요.
10. Security Group: `default`.
11. Modify DB Instance 를 Click 하세요.
12. Immediately 를 확인하여 Apply 를 하세요.
13. Continue Click 하세요.

---
**다음:** [Auto Scaling Group](/workshop/vpc-subnets-bastion/06-auto-scaling-group.md).
