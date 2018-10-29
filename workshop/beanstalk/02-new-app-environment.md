# 새로운 앱 만들기

> **중요한점:** 다음 스텝들은 최근 Elastic Beanstalk 사용자 인터페이스를 지칭하고 있습니다.  만약 Elastic Beanstalk 싸이트가 새로운 사용자 인터페이를 사용할것을 요청하면, 그렇게 하십시오.

이제 Beanstalk를 사용하여 운영환경을 매니징을 시작합니다.  우선 새로운 애플리케이션을 다음과 같이 만듭니다.

1. **Compute** 아래 **Elastic Beanstalk** 로 갑니다.
2. 오른쪽 상단 **Create New Application**에 클릭합니다.
3. **Application Name**을 `Conduit`로 합니다.
4. **Create**에 클릭합니다.

위에서 만든 새로운 애플리케이션에 환경을 더합니다. 새로운 환경을 규정하기위에서, Beanstalk에 새로만든 애플리케이션 스냅샵을 압축파일로 제공합니다([사용할앱 다운로드](/beanstalk_deploy.zip URL goes here)), 이렇게 Beanstalk에서 배포가 작동합니다. Beanstalk가 업로드된 새로운 애플리케이션 스냅샵을 압축파일을 풀기위해, `requirements.txt`에 있는 모든 의존파일을 설치및  [.ebextensions](/workshop/backend/.ebextensions)폴더에있는 액션들을 실행합니다. 자세한 내용은 앞서말한 폴더를 참조하십시오. 

1. **Actions** => **Create environment** 클릭하십시오.
2. _"environment tier"_를 선택하십시오. 긴시간 처리를 위해, HTTP요청 [웹서버 환경](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-worker.html) 와 AWS serial queue 처리를 위해 [작업 환경](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-worker.html)가 있습니다. 
**Web server environment**를 선택한다음 **Select** 클릭하십시오.
3. **Environment name**를 `Conduit-prod`로 바꾸십시오.
4. **Domain**에 `conduit-prod` 라고 쓰고 **Check availability**에 클릭하십시오.
5. **Choose a platform**에 클릭한 다음 **Preconfigured** 아래 **Python**를 선택하십시오.
6. **Application code**에 **Upload your code**를 선택한다음 **Upload**에 클릭하십시오.
7. 여기서 로컬 또는 S3 버킷을 선택할수 있습니다. 이번 예제에서는 [예제 다운로드](/workshop/backend/beanstalk_deploy.zip)를 사용하니, **Choose file** 클릭한다음 압축파일을 선택합니다.
8. **Version label**에 _"First version"_ 같이 알아볼수있는 이름을 쓰십시오.
9. 여기서 프로세스를 터미네이트 하고 ELB and ASG 환경을 셋업할수있지만, VPC 와 RDS를 지정하기위해 **Configure more options**를 클릭합니다.
10. **Configuration presets**밑에 **Custom configuration**를 선택하십시오. 각 preset마다 어떻게 선택사항이 바뀌는지 보십시오. 

이번은 중요한 스텝입니다. 여기서 우리는 우리의 인스턴스, 환경, 그리고 ELB 와 ASG 어떻게 규정되고 구성되는걸 조정할수 있습니다.  인스턴스, 환경, 그리고 ELB 와 ASG등에 얼만큼 신경을 써야하는 기억하십니까?  이점이 바로 Beanstalk를 사용해야하는 이유입니다.

다음 스크린은 바꾸지말고, 보기만 하십시오. 여기 대시보드를 바꿀수있는 기회는 끝에가면 있습니다.

1. **Security** 카드로 가서  **Modify**에 클릭하십시오.
2. **Virtual machine permissions**에 **Choose a key pair**를 클릭한다음, 이번 워크샵중에 만든 키페어를 선택하십시오.
3. **Save**를 클릭하십시오. 여기서 주의를 기울인다면, **IAM instance role**를 떠나서 인스턴스 규정할때 만든 **_ApiRol_** 를 사용한다는 것을 알것입니다.  그이유는 Beanstalk가 이미 우리에게 필요한 엑스트라롤을 설정했기 때문입니다.

여기서는 VPC를 우리환경에 설정합니다.

1. **Network** 카드로 가서 **Modify**를 클릭하십시오.
2. 화면 위쪽으로 올린다음 **VPC**옆 드랍다운에 본인의 VPC를 선택하십시오.
3. **Load balancer settings** 섹션에서 **Visibility** 드랍다운에 **Public**를 선택하십시오.
4. **Load balancer subnets** 아래에 첵박스 왼쪽편 공동 섭넷(CIDR 10.0.1.0/24 and 10.0.3.0/24)를 선택하십시오.
5. **Instance settings** => **Instance subnets**, 개인 섭넷(CIDR 10.0.2.0/24 and 10.0.4.0/24)을 선택하십시오.
6. **Instance security groups**에서 그룹 이름으로 **default**를 선택하십시오.
7. **Save** 클릭하십시오.
8. **Create environment** 클릭하십시오.

환경설정이 끝나면, 앞서 우리가 설정한 VPC안에서 로드밸런서와 오토 스케일링이 작동할것입니다.

설정이 끝나면, 환경 대시보드 맨 위쪽에 **All Applications** > **Conduit** > **Conduit-prod**이 로드 밸런서 URL 입니다.  URL를 클릭한다음 `/api`를 주소창끝에 붙이십시오. 여기서 에러가 나는 이유는 몇개의 버튼을 API를 이용해서 배포해야합니다.

만약에 어떠한 이유로 배포가 실패했을경우, 다음 링크를 보십시오[문제해결](/workshop/beanstalk/troubleshooting.md). CLI가 AWS console보다 익숙한 사용자를위해, Elastic Beanstalk를 상호작용할수 있는 CLI가 있습니다. 자세한 사항은 [이쪽](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html)을 보십시오.

---
**도전 과제:**

- 셋업이 끝나면, Beanstalk이 ELB 와 ASG를 셋업했는지 보십시오.  우리가 직접한것과 다릅니까?  어떻게 다릅니까?
- bastion이 런하는 인스턴스를 갖고 있을테니, 그 인스턴스에 로그인 해보십시오.  만약에 런하지 않는다면, 다음을 보십시오 [런하는 방법](/workshop/vpc-subnets-bastion/07-bastion.md)) 팁: Amazon Linux 사용자명은 `ec2-user` 입니다.

---
**다음:** [연동 끝맺기](/workshop/beanstalk/03-finish-integration.md)
