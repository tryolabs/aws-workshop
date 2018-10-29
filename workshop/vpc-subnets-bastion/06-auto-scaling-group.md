# Auto Scaling Group

모든 인스턴스가 Private Subnet에서만 시작되도록 새로운 Launch Configuration and Auto Scaling Group을 만들 것입니다.

## 새로운 시작 구성(Launch Configuration) 생성하기
1. AWS Management Console 에서 Compute 의 EC2 를 Click 하세요.
2. 왼쪽 메뉴 아래에 Auto Scaling Groups 를 Click 하세요.
3. 기존의 Auto Scaling group 은 삭제하세요.
4. 왼쪽 메뉴에서 Launch Configuration 을 Click 하세요.
5. 기존의 Launch Configuration 은 삭제하세요.

새로운 인스턴스 구성 및 자동 확장 그룹을 만들어 모든 인스턴스가 Private Subnet 에서만 시작되도록합니다. 이제 한 가지를 제외하고 방금 삭제 한 인스턴스와 거의 동일한 새 Launch Configuration 을 만들어야합니다: Security Group 을 만드는 대신 VPC에 대한 Default Security Group 을 선택해야합니다.

AWS 계정에 이미 Default Security Group 이 포함 된 Default VPC가 있기 때문에이를 쉽게 찾을 수있는 방법이 없으며 Launch Configuration Wizard 의 단계에서는 VPC의 Default Group과 Default VPC의 Default Group 을 구별 할 수있는 방법이 없습니다 (🤔). Security Group 을 찾으려면 다음과 같이하십시오.

1. AWS Management Console 에서 **Networking & Content Delivery** 의 **VPC** 를 Click 하세요.
2. 왼쪽 메뉴에서 **Security** 에서 **Security Groups** 을 선택하세요.
3. `default` 라는 Name을 찾고 VPC `vpc-ugly-id | awsworkshopvpc` 을 선택하거나 원하시는 것을 하세요.
4. **Group ID** 값을 Copy 하세요.

Security Group Id 가 있다면, Launch Configuration creation wizard 를 시작하세요. _Click Next: Configure Security Group. _step, 새로운 security group 을 생성하는 대신  **Select an existing security group** 을 선택하고 _default_ 라는 Name 의 ID 를 찾습니다. 필요한 경우 [previous instructions](/workshop/elb-auto-scaling-group/02-auto-scaling-group.md) 확인할 수 있습니다.

## Create Auto Scaling Group
1. AWS Management Console 에서 Compute 에서 EC2 를 선택하세요.
2. 왼쪽 메뉴에서 Auto Scaling Groups 에서 AUTO SCALING 을 선택하세요.
3. Click: Create Auto Scaling group.
4. Select: `aws-workshop-auto-scaling-group` 이후 click Next Step.
5. Launch configuration 과 동일한 Group Name 을 입력하세요.
6. Group size: 2.
7. Network: `awsworkshopvpc` 을 입력하거나 원하시는 것을 입력하세요.
8. Subnet: `10.0.2.0-ap-northeast-1a` and `10.0.4.0-ap-northeast-1b` 를 선택하세요.
9. Advanced Details 를 click 하고 : Receive traffic from one or more load balancers 를 선택하세요.
10. Target Groups 을 click 하고 select: `aws-workshop-target-group-vpc` 를 선택하거나 원하시는 것을 선택하세요.
11. Next: Configure scaling policies 를 Click 하세요.
12. Select: **Use scaling policies to adjust the capacity of this group**.
13. Between 2 and 4.
14. Target value: 80.
15. Instances need: 180.
16. Next: Configure Notifications Click 하세요.
17. Next: Configure Tags Click 하세요.
18. Review 를 Click 하세요.
19. Create Auto Scaling group Click 하세요.
20. Close Click 하세요.

---
**도전 과제:**

- 왜 ASG는 두 서브넷에서만 사용할 수 있으며 모든 서브넷에서 사용할 수 있습니까?
- 어쨌든이 서브넷 구성이 필요한 이유는 무엇입니까? (Public 2 와 Private 2).

---
**다음** [create a Bastion](/workshop/vpc-subnets-bastion/07-bastion.md) Private instances 에서 SSH 로 연결할 수 있습니다.
