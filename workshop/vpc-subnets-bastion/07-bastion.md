# Bastion instance

Bastion  dms Public Subnet 중 하나에 있는 일반 EC2 인스턴스로, SSH를 통해 들어오는 트래픽을 허용합니다. 이 Bastion 인스턴스를 통해 Private Subnet 에 있는 모든 인스턴스로 SSH를 수행 할 수 있습니다 (Bastion 에서 들어오는 트래픽을 수락한다고 가정).

## 베스천 호스트 생성하기
1. AWS Management Console 에서 **Compute section** 의 **EC2** 로 이동하세요.
2. Launch Instance 를 Click 하세요.
3. Ubuntu 서버를 찾아 (무료 티어를 사용할 수 있는지 확인하세요) 선택하여 Click 하세요.
4. `t2.micro` 를 선택하고 이후 Next: Configure Instance Details 를 click 하세요.
5. Network 에서, VPC 를 선택하세요.
6. subnet 에서, 2개의 Public 중 1개를 선택하세요. 예를 들어, `10.0.1.0-ap-northeast-1a`.
8. Next: Add Storage Click 하세요.
9. 기본 Settings 을 하고 Next: Add Tags Click 하세요.
10. Add Tag 를 Click 하세요.
11. `Name` 에 Key 를 입력하고 `bastion` 을 입력하거나 원하시는 것을 입력하세요.
12. Next: Configure Security Group Click 하세요.
13. **Security group name** 에 원하시는 것을 입력하세요.
14. Review and Launch 를 Click 하세요.
15. Launch 를 Click 하세요.
16. Key pair 를 선택하고 Launch Instances 를 Click 하세요.
17. EC2 Dashboard 에서 Instances list 를 보고 Bastion 을 선택하고 Actions/Networking Change Security Groups 을 선택하세요.
18. VPC 에서 default security group 을 확인하세요. 2 개의 Security Group 이 선택되었는지 확인하세요. Default Security Group 과 1개의 Security Group 을 작성되었습니다.

## 베스천 호스트를 통해 프라이빗 인스턴스에 접속하기

이제 SSH를 통해 액세스 할 수 있는 Public Instance 가 있지만 원하는 것은 Private Instance 에 액세스 할 수있는 것입니다.

인스턴스에 액세스하려면 첫 번째 인스턴스를 시작할 때 생성 한 PEM (키 쌍)으로 SSH를 수행해야 합니다.

### SSH agent forwarding을 설정
[가이드](https://developer.github.com/v3/guides/using-ssh-agent-forwarding/)를 참고하세요. 예제는 GitHub에 대한 액세스를 다루고 있지만 개인 인스턴스에 액세스하는 것도 유사합니다.

윈도우즈 사용자의 경우 [Putty에서 agent forwarding을 사용](https://www.lesstif.com/pages/viewpage.action?pageId=14090790)하실수도 있습니다.

Bastion 을 통해 투명하게 진행되는 보호된 인스턴스에 더 쉽게 액세스 할 수 있도록 SSH를 설정할 수 있습니다. [Here](https://www.cyberciti.biz/faq/linux-unix-ssh-proxycommand-passing-through-one-host-gateway-server/) 에 좋은 가이드가 있습니다.


---
**도전과제:** `ssh` 는 Private Subnet 의 인스턴스 중 하나에 연결하고 `tracepath`를 외부 호스트에 전달합니다. Public Subnet 의 인스턴스에 대해서도 동일하게 수행하십시오. 차이점이 뭘까요?

---
**다음:** [finish the deploy](/workshop/vpc-subnets-bastion/08-finishing-up.md).
