# VPC and *bastion* instance

The aim of this section is to improve a bit our security and redundancy. For this we are going to create a [custom VPC](https://aws.amazon.com/documentation/vpc/).

Once we have our VPC, we will create 2 private subnets (where our Auto Scaling Group will launch the web server instances) in different Availability Zones (for redundancy reasons). We will also setup 2 public subnets in the same availability zones, which are needed by the load balancer. You can read more about VPC and subnets [here](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html).

For our public subnets, we will need to setup an [Internet Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html) and create a new [Route Table](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html), so any instance in the subnet can access the Internet.

Since our application's instances will live in the **private** subnets, we also will need a [NAT Instance](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html) that will route their Internet traffic through the public subnets. We need our instances to access the Internet so that we can download packages, update our system, etc.

We need to create a new Launch Configuration and modify our Auto Scaling Group so from now on it deploys to our VPC in the right subnets. Also, our RDS (PostgreSQL database) needs to be moved to our VPC so our instances can reach it.

To access our instances through SSH from the outside world, we will add a [bastion instance](https://aws.amazon.com/blogs/security/how-to-record-ssh-sessions-established-through-a-bastion-host/). Since the bastion has direct access to the instances, we can access them by accessing the bastion first.

Finally, some changes need to be made to our CodeDeploy project so it deploys to our VPC, as expected.

So, let's get started.

---
**Next:** [create a VPC](/workshop/vpc-subnets-bastion/01-create-vpc.md).


# VPC 와 Bastion 인스턴스

이 섹션의 목적은 우리의 Security 와 Redundancy 를 개선시키는 것에 있습니다. 이를 위해 [custom VPC](https://aws.amazon.com/documentation/vpc/)를 만듭니다.

Public Subnet의 경우 [Internet Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html)를 설정하고 새로운 [Route Table](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html) 을 생성, 그래서 이 Subnet 의 모든 인스턴스는 인터넷에서 액세스 할 수 있습니다.

애플리케이션의 인스턴스는 **private** Subnets 에 존재하는 것이라면 Public Subnets 을 통하여 인터넷 트래픽을 라우트 할 [NAT 인스턴스](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html)가 필요할 것입니다. 패키지를 다운로드하고 시스템을 업데이트 할 수 있도록 인터넷에 액세스하려면 인스턴스가 필요합니다.

새로운 Launch Configuration을 만들고 Auto Scaling Group을 수정하여 올바른 Subnet의 VPC에 배치해야합니다. 또한 우리의 RDS (PostgreSQL 데이터베이스)를 VPC로 움직여서  인스턴스가 도달 할 수 있습니다.

바깥 세상에서 SSH를 통해 인스턴스에 액세스하려면 [Bastion 인스턴스](https://aws.amazon.com/blogs/security/how-to-record-ssh-sessions-established-through-a-bastion-host/)를 추가하십시오.  Bastion은 인스턴스에 직접 액세스 할 수 있으므로 첫번쨰로 Bastion에 액세스하여접속  할 수 있습니다.

마지막으로 CodeDeploy 프로젝트에 일부 변경을 가해 VPC에 배포합니다.

그래서 이제 시작하겠습니다.

---
**다음:** [create a VPC](/workshop/vpc-subnets-bastion/01-create-vpc.md).
