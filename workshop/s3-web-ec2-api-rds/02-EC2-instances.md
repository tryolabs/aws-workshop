# EC2 instances

[AWS EC2](https://aws.amazon.com/ec2/) 애플리케이션의 API는 여러 곳에서 이용됩니다. 다음 섹션에서는 [CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) 를 사용하여 API를 만들고 배포할 것입니다.

먼저 EC2 인스턴스가 SSM에 액세스 할 수 있도록 role을 만듭니다:

1. **Security, Identity & Compliance** 아래에 있는 **IAM** 으로 이동하십시오.
2. Role 섹션으로 이동하고, Create Role을 클릭하십시오.
3. **AWS Service** 선택한 후 **EC2** 를 선택하십시오.
4. **Select your use case** 에서, _"Allows EC2 instances to call AWS services on your behalf."_ 라는 메시지를 선택하고 next를 클릭하십시오.
5. `AmazonSSMReadOnlyAccess`를 검색하고 , 그것을 선택 후 next를 클릭하십시오.
6. 그것을 `ApiRole` 이라 부를 수 있습니다. create Role를 클릭하십시오.

우리는 이미 Parameter Store에 항목을 만들었습니다. 앞으로는 데이터베이스 password와 같은 암호화 된 변수가 필요할 것입니다. 이를 위해 암호화 된 키를 만들어 해당 값을 암호화하고 해독합니다.해당 암호화 키는 관리자와 방금 만든 역할에 첨부되므로 역할을 맡을 수 있도록 설정된 서비스만 암호 해독 된 값에 액세스 할 수 있습니다. SSM 및 보안 데이터에 대한 자세한 내용을 볼 수 있습니다. [here](https://aws.amazon.com/blogs/compute/managing-secrets-for-amazon-ecs-applications-using-parameter-store-and-iam-roles-for-tasks/).

1. **Encryption keys** 섹션으로 이동하십시오.
2. **Create key** 를 선택하십시오.
3. `workshopkey`를 별칭으로 입력하고 "this is the encryption key for the AWS workshop"와 같은 의미있는 설명을 입력하십시오.
4. next step을 클릭하고 next step을 다시 클릭하십시오.
5. AWS CLI 및 콘솔 사용자를 모두 선택하고 next 를 클릭하십시오.
6. 너의 EC2 Role을 선택하고 and next를 클릭하십시오.
7. Finish를 클릭하십시오.

앞으로는 새로운 역할을 가진 EC2 인스턴스가 암호화된 매개 변수에 액세스 하려고하면 AWS가 자동으로 암호를 해독합니다.

## 첫 번째 EC2 인스턴스 실행

우리는 첫 번째 EC2 인스턴스를 시작할 준비가되었습니다. 우리는 스탠다드한 EC2 인스턴스를 만들것이고, [startup script](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html) (인스턴스가 부팅 될 때 자동으로 실행 되는) 를 추가해야하고, 마지막으로 EC2 인스턴스에서 아웃 바운드 및 인바운드를 제어하는[security group](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html) 을 만들 것입니다.

1. **Compute section** 아래의 **EC2** 로 이동하고, 오른쪽 상단에서 우리가 사용할 region을 선택할 수 있습니다. 이 경우 이전에 S3 버킷 설정에 사용했던 것과 동일한 영역 인 `US East (N. Virginia)`를 사용하게됩니다.
2. Launch Instance를 클릭하십시오.
3. Ubuntu Server를 본다음 (free tier를 사용할 수 있는지 확인하십시오), 그것을 선택후 클릭하십시오.
4. `t2.micro`를 선택하고 Next : Configure Instance Details를 클릭하십시오.
5. **IAM role** 에서 우리의 `ApiRole` 을 선택하십시오.
6. 고급 세부 사항에서 사용자 데이터에서 "As text"를 선택하고 다음 bash 스크립트를 붙여 넣으십시오:
    ```
    #!/bin/bash
    export LC_ALL=C.UTF-8
    apt update
    apt -y install ruby
    cd /home/ubuntu
    wget https://aws-codedeploy-us-east-1.s3.amazonaws.com/latest/install
    chmod +x ./install
    ./install auto
    ```

    스크립트 시작 부분에 공백을 남겨두면 작동하지 않습니다. 그래서 각 행의 앞부분에는 공백을 남기지 지마십시오!
    만약 다른 region을 사용했다면 `wget` 행의 버킷 이름이 다를 수 있습니다([여기](https://docs.aws.amazon.com/codedeploy/latest/userguide/resource-kit.html#resource)를 참조해 주세요). -kit-bucket-names))

7. 다음을 클릭하십시오: Add Storage
8. 기본 설정을 그대로두고 다음을 클릭하십시오: Add Tags
9. Add Tag를 클릭하십시오.
10. Fill 키에`service`를 넣고 Value에는`api`를 넣습니다.
11. Key `environment` 와 Value `prod` 를 가진 또 다른 태그를 추가하십시오. 이 키는 나중에 API를 실행하는 EC2 인스턴스를 식별하는 데 도움이됩니다.
12. 다음을 클릭하십시오: Configure Security Group.
13. _Create a new security group_ 옵션이 선택되었는지 확인하고, on the _Security group name:_ 필드에 설명이 포함 된 이름을 작성하십시오. 나중에 이름을 바꿀 수 없으므로 이름을 현명하게 선택하십시오.
14. Add Rule를 클릭하십시오.
15. port range 는 `9000` 을 셋팅하고, 소스에는 `0.0.0.0/0`를 셋팅하고, 의미있는 설명 추가하십시오. 이렇게하면 모든 IP의 포트 9000에서 들어오는 트래픽을 사용할 수 있으므로 외부에서 인스턴스에 "연결할"수 있습니다. 만약 너가 집중해서 본다면, 기본적으로 우리는 포트 22에서 인바운드 트래픽을 허용하는 규칙을 얻습니다. 이 규칙은 인스턴스에 대한 SSH를 사용할 수 있습니다. 또한 기본적으로 아웃 바운드 트래픽 (즉, 인스턴스에서 시작된 트래픽)은 모든 대상 및 포트에 허용되지만 나중에 보안 그룹에 대한 아웃 바운드 규칙을 편집하여 제한 할 수 있습니다.
16. Review and Launch를 클릭하십시오.
17. Launch를 클릭하십시오.
18. 기존 키 쌍을 선택하라는 메시지가 나타나면 `create a new key pair` 을 선택하고 이름을 `aws_workshop` 으로 지정하고 download를 클릭하십시오. 그것을 안전한 장소에 저장하십시오. (`~/.ssh`는 좋습니다.하지만 `chmod 400` 은 PEM 파일이므로 사용자만 읽을 수 있습니다.) 우리는 그것을 전체 워크샵 동안 SSH에 사용합니다.
19. Launch Instances를 클릭하십시오.

---
**Extra mile:**

- EC2 인스턴스를 핑 (ping) 해보십시오. 엑스트라 포인트를 받으면 작동합니다!
- SSH를 통해 새 인스턴스에 연결하십시오. 사용자 이름은 _ubuntu_이며`.pem` 파일을 사용하기 위해`-i` 플래그를 사용하십시오.

---
**다음:** [PostgresSQL database on RDS](/workshop/s3-web-ec2-api-rds/03-RDS.md) 만들기.
