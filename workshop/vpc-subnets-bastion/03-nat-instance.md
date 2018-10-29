# NAT Instance

지금까지 2개의 Public Subnet과 2개의 Private Subnet 을 만들었습니다. Private 에서는 Load Balancer 를 통해 액세스 할 수 있는 웹 서비 인스턴스를 배포합니다.

이러한 인스턴스가 VPC 외부에서 연결할 필요가 없더라도 패키지를 다운로드하고 업데이트하려면 인터넷에 액세스 할 수 있어야합니다. 이러한 이유로 외부의 모든 아웃 바운드 트래픽을 라우팅 할 수있는 NAT가 필요합니다.

AWS 는 NAT: [NAT Instance](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html) 와 [NAT Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html) 2가지 option을 제공합니다. Gateway 오퍼링은 NAT 인스턴스보다 새롭고 설치가 쉽고 자동으로 확장됩니다. 그러나이 자습서에서는 NAT 인스턴스를 저렴하게 사용할 수 있습니다 (너무 많이 청구되기를 원하지 않습니다!).

## Create Nat Instance
1. AWS Management Console 에서 Computer 의 EC2 Dashboard 로 이동하세요.
2. 왼쪽 메뉴에서 Instances 를 Click 하세요.
3. Launch Instance Click 하세요.
4. Community AMIs 를 선택하세요.
5. NAT 를 입력하고 그 다음 Enter 를 누르세요.
6. 나타나는 첫 번째 옵션을 선택하십시오:
  1. Root device type: `ebs`
  2. Virtualization type: `hvm`
  3. ENA Enabled: `No`.
7. `t2.micro` 를 선택하고 Next 를 click : Configure Instance Details.
8. Network 에서, VPC를 선택하세요.
9. subnet 에서, `10.0.1.0-ap-northeast-1a` 를 선택하세요.
10. Next: Add Storage 를 Click 하세요.
11. Next: Add Tag Click 하세요.
12. Key 에서 `Name` 과 Value `MyNat` 을 입력하거나 원하시는 것을 입력하세요.
13. Next: **Configure Security Group** Click 하세요.
14. Select: 새로운 **security group** 을 만듭니다.
15. **Security group name** 을 `natsecuritygroup` 를 입력하거나 원하시는 것을 입력하세요.
16. 기본이 되는 3개의 rules: SSH, HTTP, HTTPS 을 추가하세요.
17. **Review and Launch** 를 Click 하세요.
18. Next 를 Click 하세요.
19. Launch 를 Click 하세요.
20. key pair 를 선택하고 Launch Instances 를 Click 하세요.
21. **View Instances** 를 Click 하세요.
22. NAT instance 선택하세요.
23. Actions - Networking 으로 이동하고 **Change Source/Dest. Check** 을 click 하세요.
24. Yes, **Disable** Click 하세요.
25. 다시 Actions - Networking 으로 이동하고 **Change Security Groups** 을 click 하고 VPC에 기본으로 추가하세요.

## Create a route for private subnets through the NAT instance
1. AWS Management Console에서 Networking & Content Delivery 의 VPC로 이동하세요.
2. 왼쪽 메뉴에서 **Route Tables** 로 이동하세요.
3. Main subnet 인 `awsworkshopvpc` 을 선택하세요.
4. 화면 하단의 **Routes tab** 으로 이동하세요.
5. **Edit** 를 Click 하세요.
6. **another Route** 를 추가하고 Click 하세요.
7. Destination `0.0.0.0/0` 을 입력하세요.
8. NAT Instance 를 Target 으로 선택하세요.
9. **Save** 를 Click 하세요.

---
**다음:** [Create new Load Balancer](/workshop/vpc-subnets-bastion/04-load-balancer.md).
