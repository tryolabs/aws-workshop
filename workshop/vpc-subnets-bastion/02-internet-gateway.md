# Internet Gateway

We already have our VPC with 4 subnets, but none of those can access the Internet (they are effectively private). To turn 2 of them into public, we need to setup an [Internet Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html) for our VPC and create a Route Table to route all external traffic through the gateway.
Finally, we need to associate 2 of our subnets to this route table and assign them a public IP, so they turn into public subnets.

## Create a Internet Gateway
1. Go to Internet Gateways on the left section.
2. Click Create Internet Gateway.
3. As Name tag put: `awsworkshopIGW`.
4. Click: Yes, Create.
5. Click Attach to VPC.
6. Click: Yes, Attach.

## Create Route tables
1. Go to Route Tables on the left section.
2. Click Create Route Table.
3. As Name tag: `awsWorkshopPublicRT`.
4. Click Yes, Create.
5. On the bottom section select the Routes tab.
6. Click on Edit button.
7. Click on Add another Route.
8. As **Destination** put `0.0.0.0/0`.
9. As **Target** select your Internet Gateway.
10. Click Save.
11. Now select Subnet Associations tab.
12. Click on Edit.
13. Select `10.0.1.0-us-east-1a` and `10.0.3.0-us-east-1b`.
14. Click Save.

## Assign public IP to our public subnet
1. Go to Subnets on the left section.
2. Select the `10.0.1.0-us-east-1a`.
3. Click on Subnet Actions.
4. Select Modify auto-assign IP settings.
5. Check: Enable auto-assign public IPv4 address.
6. Click Save.
7. Click Close.
8. Repeat steps 2-7 with `10.0.3.0-us-east-1b`.

---
**Next:** [create a NAT Instance](/workshop/vpc-subnets-bastion/03-nat-instance.md).

# Internet Gateway

우리는 이미 4개의 Subnet과 함께 VPC를 가지고 있지만, 그중 아무도 인터넷에 접속할 수 없습니다. (그들은 private 효과가 있다.). Public으로 2개를 전환하려면, 우리는 VPC용 [Internet Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html) 를 Setup하고 Gateway를 통하여 모든 외부 트래픽을 라우팅하는 Routing Table 을 create 해야 합니다. 마지막으로, 우리는 2개의 Subnet을 라우팅 테이블에 associate 하고 public IP 를 할당하면, public subnet이 됩니다.

## Internet Gateway 만들기
1. 왼쪽 메뉴에서 **Internet Gateways** 를 Click 하세요.
2. **Create Internet Gateway** 를 Click 하세요.
3. **Name** **tag** 에는 `awsworkshopIGW` 를 입력하거나 원하시는 것을 입력하세요.
4. Yes, Create 를 Click 하세요.
5. Attach to VPC 를 Click 하세요.
6. Yes, Attach 를 Click 하세요.

## Route tables 만들기
1. 왼쪽 메뉴에서 **Route Tables** 을 Click 하세요.
<<<<<<< HEAD
2. Create Route Table 을 Click 하세요.
3. **Name tag** 에는 `awsWorkshopPublicRT` 을 입력하거나 원하시는 것을 입력하세요.
4. **Yes, Create** 를 Click 하세요.
5. On the bottom section select the Routes tab.
6. Click on Edit button.
7. Click on Add another Route.
8. As **Destination** put `0.0.0.0/0`.
9. As **Target** select your Internet Gateway.
10. Click Save.
11. Now select Subnet Associations tab.
12. Click on Edit.
13. Select `10.0.1.0-us-east-1a` and `10.0.3.0-us-east-1b`.
14. Click Save.
=======
2. **Create Route Table** 을 Click 하세요.
3. **Name tag**: `awsWorkshopPublicRT` 을 입력하거나 원하시는 것을 입력하세요.
4. **Yes, Create** 을 Click 하세요.
5. 화면 아래에 **Routes tab** 을 선택하세요.
6. **Edit button** 을 Click 하세요.
7. 추가할 **Route** 을 입력하세요.
8. **Destination** 에서 `0.0.0.0/0` 을 입력하거나 원하시는 것을 입력하세요.
9. **Target** 에는 **Internet Gateway** 을 선택하세요.
10. 설정이 완료되었으면 **Save** 를 CLick 하세요.
11. **Associations tab** 에는 Subnet을 선택하세요.
12. **Edit** 를 Click 하세요.
13. `10.0.1.0-ap-northeast-1a` 와 `10.0.3.0-ap-northeast-1b` 을 선택하세요.
14. **Save** 을 Click 하세요.
>>>>>>> 3b5a7c9246173129e929ca5e43e094b903d0d65a

## Assign public IP to our public subnet
1. 왼쪽 메뉴에서 **Subnets** 을 Click 하세요.
2. `10.0.1.0-ap-northeast-1a` 을 선택하세요.
3. **Subnet Actions** 를 Click 하세요.
4. **auto-assign IP** 를 수정하여 설정하세요.
5. **Enable auto-assign public IPv4 address** 를 Click 하세요.
6. **Save** Click 하세요.
7. **Close** Click 하세요.
8. 반복, 위의 2번 - 7번을 반복하여 `10.0.3.0-ap-northeast-1b`.

---
**다음:** [create a NAT Instance](/workshop/vpc-subnets-bastion/03-nat-instance.md).