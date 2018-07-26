# VPC

We are going to create our VPC with 4 subnets (2 private and 2 public).

## Create a VPC
1. Go to VPC under Networking & Content Delivery.
2. Go to Your VPCs on the left section.
3. Click on Create VPC.
4. As **Name** **tag** put: `awsworkshopvpc`.
5. As **IPv4 CIDR** **block** put: `10.0.0.0/16`.
6. Then click: Yes, Create.

## Create 4 subnets
1. Go to Subnets on the left section.
2. Click Create Subnet.
3. As **Name tag** put: `10.0.1.0-us-east-1a`.
4. **Availability Zone**: `us-east-1a`.
5. As **IPv4 CIDR** **block** put: `10.0.1.0/24`. CIDR block for any subnet will be a subset of the VPC CIDR block.
6. Then click in Yes, Create.
7. Repeat steps 2-6 using as **Name tag**: `10.0.2.0-us-east-1a`, **Availability Zone**: `us-east-1a` and **IPv4 CIDR block**: `10.0.2.0/24`.
8. Repeat steps 2-6 using as **Name tag**: `10.0.3.0-us-east-1b`, **Availability Zone**: `us-east-1b` and **IPv4 CIDR block**: `10.0.3.0/24`.
9. Repeat steps 2-6 using as **Name tag**: `10.0.4.0-us-east-1b`, **Availability Zone**: `us-east-1b` and **IPv4 CIDR block**: `10.0.4.0/24`.

---
**Next:** [create an Internet Gateway and a public Routes table](/workshop/vpc-subnets-bastion/02-internet-gateway.md).

# VPC

우리는 VPC에 4개의 Subnet을 만들려고 합니다.  (2 private and 2 public).

## Create a VPC
1. AWS Management Console에 접속한 후 Region(예:Seoul) 을 Click 하세요. 이후 메뉴에서 Networking & Content Delivery 안의 VPC를 Click 하세요.
2. 왼쪽 메뉴에서 `Your VPCs` 를 Click 하세요.
3. 화면 왼쪽 위에 `Create VPC` 를 Click 하세요.
4. **Name** **tag** 에는 `awsworkshopvpc` 를 입력하시거나 원하시는 것을 입력하세요.
5. **IPv4 CIDR** **block** 에는 `10.0.0.0/16` 를 입력하시거나 원하시는 IP 대역을 입력하세요.
6. 오른쪽 아래에 `Yes, Create` 를 Click 하세요..

## Create 4 subnets
1. 왼쪽 메뉴에서 `Subnets` 를 Click 하세요.
2. 화면 왼쪽 위에 `Create Subnet` 을 Click 하세요.
3. **Name tag** 에는 `10.0.1.0-us-east-1a` 를 입력하시거나 원하시는 것을 입력하세요.
4. **VPC** 에는 생성한 VPC 를 Click 하세요.
5. **Availability Zone** 에는 원하시는 Availability Zone(예:ap-northeast-2a)을 Click 하세요.
6. **IPv4 CIDR** **block** 에는 `10.0.1.0/24` 를 입력하세요. 모든 Subnet 에 대한 CIDR 블록은 VPC CIDR 블록의 하위 집합이 됩니다.
7. `Yes, Create` 을 Click 하세요.
8. 반복, 위의 2번 - 7번을 반복하여 **Name tag**: `10.0.2.0-ap-northeast-2a`, **Availability Zone**: `ap-northeast-1a`, **IPv4 CIDR block**: `10.0.2.0/24`.
9. 반복, 위의 2번 - 7번을 반복하여 **Name tag**: `10.0.3.0-ap-northeast-2b`, **Availability Zone**: `us-east-1b`, **IPv4 CIDR block**: `10.0.3.0/24`.
10. 반복 위의 2번 - 7번 **Name tag**: `10.0.4.0-ap-northeast-2b`, **Availability Zone**: `ap-northeast-2b`, **IPv4 CIDR block**: `10.0.4.0/24`.

---
**다음:** [create an Internet Gateway and a public Routes table](/workshop/vpc-subnets-bastion/02-internet-gateway.md).

