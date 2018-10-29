# Internet Gateway

우리는 이미 VPC에 4개의 Subnet 을 함께 가지고 있지만, 그 중 아무것도 인터넷에 접속할 수 없습니다. (그것들은 Private 상태입니다). Public으로 2개를 전환하려면, 우리는 VPC용 [Internet Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html) 를 Setup하고 Gateway를 통하여 모든 외부 트래픽을 라우팅하는 Routing Table 을 create 해야 합니다. 마지막으로, 우리는 2개의 Subnet을 라우팅 테이블에 associate 하고 public IP 를 할당하면, public subnet이 됩니다.

## Internet Gateway 만들기
1. VPC Dashboard 의 왼쪽 메뉴에서 **Internet Gateways** 를 Click 하세요.
2. **Create Internet Gateway** 를 Click 하세요.
3. **Name tag** 에는 `awsworkshopIGW` 를 입력하거나 원하시는 것을 입력하세요.
4. **Create** 를 Click 하세요.
5. 메뉴 상단에 **Action** 을 Click 하고 **Attach to VPC** 를 Click 하세요.
6. **Attach** 를 생성한 VPC를 선택하여 Click 하세요.

## Route tables 만들기
1. VPC Dashboard 의 왼쪽 메뉴에서 **Route Tables** 을 Click 하세요.
2. **Create Route Table** 을 Click 하세요.
3. **Name tag**: `awsWorkshopPublicRT` 을 입력하거나 원하시는 것을 입력하세요.
4. **Yes, Create** 을 Click 하세요.
5. 화면 아래에 **Routes** tab 을 Click 하세요.
6. **Edit** button 을 Click 하세요.
7. 추가할 `Route` 을 입력하세요.
8. **Destination** 에서 `0.0.0.0/0` 을 입력하거나 원하시는 것을 입력하세요.
9. **Target** 에는 생성한 **Internet Gateway** 을 선택하여 Click 하세요.
10. 설정이 완료되었으면 **Save** 를 CLick 하세요.
11. **Subnet Associations** tab 에는 Subnet을 선택하세요.
12. **Edit** 를 Click 하세요.
13. `10.0.1.0-ap-northeast-1a` 와 `10.0.3.0-ap-northeast-1b` 을 선택하세요.
14. **Save** 을 Click 하세요.

## Assign public IP to our public subnet
1. 왼쪽 메뉴에서 **Subnets** 을 Click 하세요.
2. `10.0.1.0-ap-northeast-1a` 을 선택하세요.
3. **Actions** 를 Click 하세요.
4. **Modify auto-assign IP** 를 수정하여 설정하세요.
5. **Enable auto-assign public IPv4 address** 를 Click 하세요.
6. **Save** Click 하세요.
7. **Close** Click 하세요.
8. 반복, 위의 2번 - 7번을 반복하여 `10.0.3.0-ap-northeast-1b` 을 선택하세요.

---
**다음:** [Create a NAT Instance](/workshop/vpc-subnets-bastion/03-nat-instance.md).
