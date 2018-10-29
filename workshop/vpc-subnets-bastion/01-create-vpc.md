# VPC

지금부터 새로운 VPC를 4개의 서브넷(프라이빗2개, 퍼블릭2개)과 함깨 생성하도록 하겠습니다.

## VPC생성
1. AWS Management Console에 접속한 후 Region(예:Seoul) 을 Click 하세요. 이후 메뉴에서 Networking & Content Delivery 안의 VPC를 Click 하세요.
2. 왼쪽 메뉴에서 **Your VPCs** 를 Click 하세요.
3. 화면 왼쪽 위에 **Create VPC** 를 Click 하세요.
4. **Name tag** 에는 `awsworkshopvpc` 를 입력하시거나 원하시는 것을 입력하세요.
5. **IPv4 CIDR block** 에는 `10.0.0.0/16` 를 입력하시거나 원하시는 IP 대역을 입력하세요.
6. 오른쪽 아래에 **Yes, Create** 를 Click 하세요..

## 4개의 서브넷을 생성
1. 왼쪽 메뉴에서 **Subnets** 를 Click 하세요.
2. 화면 왼쪽 위에 **Create Subnet** 을 Click 하세요.
3. **Name tag** 에는 `10.0.1.0-ap-northeast-1a` 를 입력하시거나 원하시는 것을 입력하세요.
4. **VPC** 에는 생성한 VPC 를 Click 하세요.
5. **Availability Zone** 에는 원하시는 Availability Zone(예:ap-northeast-2a)을 Click 하세요.
6. **IPv4 CIDR block** 에는 `10.0.1.0/24` 를 입력하세요. 모든 Subnet 에 대한 CIDR 블록은 VPC CIDR 블록의 하위 집합이 됩니다.
7. **Create** 을 Click 하세요.
8. 반복, 위의 2번 - 7번을 반복하여 **Name tag**: `10.0.2.0-ap-northeast-2a`, **Availability Zone**: `ap-northeast-1a`, **IPv4 CIDR block**: `10.0.2.0/24`.
9. 반복, 위의 2번 - 7번을 반복하여 **Name tag**: `10.0.3.0-ap-northeast-2b`, **Availability Zone**: `ap-noreast-1b`, **IPv4 CIDR block**: `10.0.3.0/24`.
10. 반복, 위의 2번 - 7번을 반복하여 **Name tag**: `10.0.4.0-ap-northeast-2b`, **Availability Zone**: `ap-northeast-2b`, **IPv4 CIDR block**: `10.0.4.0/24`.

---
**다음:** [Create an Internet Gateway and a public Routes table](/workshop/vpc-subnets-bastion/02-internet-gateway.md).


