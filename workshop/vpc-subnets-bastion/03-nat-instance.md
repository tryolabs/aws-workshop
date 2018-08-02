# NAT Instance

Until now we have 2 public subnets and 2 private subnets. In the private ones, we will deploy the webserver instances that will be accessible via a Load Balancer.

Even if these instances don't need to be reachable from outside of the VPC, they need to have Internet access to download and update packages. For this reason, we need a NAT through which we can route all external outbound traffic.

AWS offers two options for NAT: [NAT Instance](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html) and [NAT Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html).
The Gateway offering is newer and easier to setup than the NAT Instance, and also automatically scales. However, for this tutorial, will go for the NAT Instance purely because it's cheaper (we don't want to be billed too much!).

## Create Nat Instance
1. Go to EC2 under Computer section.
2. Click on Instances on the left menu.
3. Click Launch Instance.
4. Select Community AMIs.
5. Type NAT and then hit Enter.
6. Select the first option that appears:
  1. Root device type: `ebs`
  2. Virtualization type: `hvm`
  3. ENA Enabled: `No`.
7. Select `t2.micro` and click Next: Configure Instance Details.
8. On Network, select your VPC.
9. As subnet, select `10.0.1.0-us-east-1a`
10. Click Next: Add Storage.
11. Click Next: Add Tag.
12. As Key put `Name` and as Value `MyNat`.
13. Click Next: Configure Security Group.
14. Select: Create a new security group.
15. As **Security group name** put `natsecuritygroup`.
16. Add 3 rules: SSH, HTTP, HTTPS.
17. Click: Review and Launch.
18. Click: Next.
19. Click: Launch.
20. Select your key pair and click Launch Instances.
21. Click View Instances.
22. Select your NAT instance.
23. Go to Actions - Networking and click on **Change Source/Dest. Check**.
24. Click Yes, Disable.
25. Go to Actions again - Networking and click **Change Security Groups** and add the default one for the VPC.

## Create a route for private subnets through the NAT instance
1. Go to VPC under Networking & Content Delivery.
2. Go to Route Tables on the left section.
3. Select the Main subnet of `awsworkshopvpc`.
4. On the bottom section go to the Routes tab.
5. Click Edit.
6. Click Add another Route.
7. As Destination put: `0.0.0.0/0`.
8. As Target select your NAT Instance.
9. Click Save.

---
**Next:** [create new Load Balancer](/workshop/vpc-subnets-bastion/04-load-balancer.md).

# NAT Instance

지금까지 2개의 Public Subnet과 2개의 Private Subnet 이 있습니다. Private 에서는 Load Balancer 를 통해 액세스 할 수 있는 웹 서비 인스턴스를 배포합니다.

이러한 인스턴스가 VPC 외부에서 연결할 필요가 없더라도 패키지를 다운로드하고 업데이트하려면 인터넷에 액세스 할 수 있어야합니다. 이러한 이유로 외부의 모든 아웃 바운드 트래픽을 라우팅 할 수있는 NAT가 필요합니다.

AWS 는 NAT: [NAT Instance](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html) 와 [NAT Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html) 2가지 option을 제공합니다. Gateway 오퍼링은 NAT 인스턴스보다 새롭고 설치가 쉽고 자동으로 확장됩니다. 그러나이 자습서에서는 NAT 인스턴스를 저렴하게 사용할 수 있습니다 (너무 많이 청구되기를 원하지 않습니다!).

## Create Nat Instance
1. AWS Management Console 의 Computer 에서 EC2로 이동하세요.
2. 왼쪽 메뉴에서 Instances Click 하세요.
3. Launch Instance Click 하세요.
4. Community AMIs 를 선택하세요.
5. NAT 를 입력하고 그 다음 Enter 를 누르세요.
6. 나타나는 첫 번째 옵션을 선택하십시오:
  1. Root device type: `ebs`
  2. Virtualization type: `hvm`
  3. ENA Enabled: `No`.
7. `t2.micro` 를 선택 그리고 Next 를 click : Configure Instance Details.
8. Network 에서, VPC를 선택하세요.
9. subnet 에서, `10.0.1.0-ap-northeast-1a` 를 선택하세요.
10. Next: Add Storage 를 Click 하세요.
11. Next: Add Tag Click 하세요.
12. Key 에서 `Name` 과 Value `MyNat` 을 입력하세요.
13. Next: Configure Security Group Click 하세요.
14. Select: 새로운 security group 을 만듭니다.
15. **Security group name** 을 `natsecuritygroup` 를 입력하거나 원하시는 것을 입력하세요.
16. 3개의 rules: SSH, HTTP, HTTPS 을 추가하세요.
17. Review and Launch 를 Click 하세요.
18. Next 를 Click 하세요.
19. Launch 를 Click 하세요.
20. key pair 를 선택하고 Launch Instances 를 Click 하세요.
21. View Instances Click 하세요.
22. NAT instance 선택하세요.
23. Actions - Networking 으로 이동하고 **Change Source/Dest. Check** 을 click 하세요.
24. Yes, Disable Click 하세요.
25. 다시 Actions - Networking 으로 이동하고 **Change Security Groups** click 하고 VPC에 기본으로 추가하세요.

## Create a route for private subnets through the NAT instance
1. Networking & Content Delivery 안에 있는 VPC로 이동.
2. 왼쪽 메뉴에서 Route Tables 로 이동하세요.
3. Main subnet 인 `awsworkshopvpc` 을 선택하세요.
4. 화면 하단의 Routes tab 으로 이동하세요.
5. Edit 를 Click 하세요.
6. another Route 를 추가하고 Click 하세요.
7. Destination `0.0.0.0/0` 을 입력하세요.
8. NAT Instance 를 Target 으로 선택하세요.
9. Save Click 하세요.

---
**다음:** [create new Load Balancer](/workshop/vpc-subnets-bastion/04-load-balancer.md).
<<<<<<< HEAD

=======
>>>>>>> f6c4bc7d450c38053fa9458250752732b0776588
