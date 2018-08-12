# VPC 와 Bastion 인스턴스

이 섹션의 목적은 우리의 Security 와 Redundancy 를 개선시키는 것에 있습니다. 이를 위해 [custom VPC](https://aws.amazon.com/documentation/vpc/)를 만듭니다.

VPC가 생기면 중복성을 이유로 서로 다른 가용 영역에서 2 개의 Private Subnet (AutoScaling Group 이 웹 서버 인스턴스를 시작할 위치)을 만듭니다. Load Balacner 에 필요한 동일한 가용 영역에 2 개의 Public Subnet 을 설치합니다. VPC 와 subnets 에 대해 많은 것은 [here](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) 읽을 수 있습니다.

Public Subnet의 경우 [Internet Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html)를 설정하고 새로운 [Route Table](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html) 을 생성, 그래서 이 Subnet 의 모든 인스턴스는 인터넷에서 액세스 할 수 있습니다.

애플리케이션의 인스턴스는 **Private** Subnets 에 존재하는 것이라면 Public Subnets 을 통하여 인터넷 트래픽을 라우트 할 [NAT 인스턴스](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html)가 필요할 것입니다. 패키지를 다운로드하고 시스템을 업데이트 할 수 있도록 인터넷에 액세스하려면 인스턴스가 필요합니다.

새로운 Launch Configuration을 만들고 Auto Scaling Group을 수정하여 올바른 Subnet의 VPC에 배치해야 합니다. 또한 RDS (PostgreSQL 데이터베이스)를 VPC 로 이동하여 인스턴스가 도달 할 수 있습니다.

바깥 세상에서 SSH를 통해 인스턴스에 액세스하려면 [Bastion 인스턴스](https://aws.amazon.com/blogs/security/how-to-record-ssh-sessions-established-through-a-bastion-host/)를 추가하십시오.  Bastion은 인스턴스에 직접 액세스 할 수 있으므로 첫번쨰로 Bastion에 액세스하여 접속 할 수 있습니다.

마지막으로 CodeDeploy 프로젝트에 일부 변경을 하여 VPC에 배포합니다.

그래서 이제 시작하겠습니다.

---
**다음:** [Create a VPC](/workshop/vpc-subnets-bastion/01-create-vpc.md).
