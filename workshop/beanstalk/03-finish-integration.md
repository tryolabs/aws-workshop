# 연동 끝맺기

지금 우리의 인스턴스가 다른 구성원과 협업하기위해서는 세부사항을 조율해야 합니다. 그들은 S3 프론트엔드와 RDS 데이타베이스 입니다. 여기서 우리는 다른 URL에있는 API를 부를수 있다고 프론트단에 말해줘야 합니다.

우선 우리는 API를 위한 새로운 URL을 필요로 합니다. 
1. **Compute** 아래 **Elastic Beanstalk** 로 가십시오.
2. **Conduit** 애플리케이션 아래 **Conduit-prod** 카드에 클릭하십시오.
3. 맨위, **All Applications** 끝쪽에 **Environment ID** 와 **URL** 가 있습니다.  URL을 복사하십시오.

이제 우리는 API URL를 프론트단 Parameter Store에 붙이기를 합니다.
1. **Compute** 아래 **EC2**로 가십시오.
2. **SYSTEMS MANAGER SHARED RESOURCES** 아래 **Parameter Store**를 클릭하십시오.
3. **/prod/frontend/API_URL** 를 선택하십시오.
4. **Actions** => **Edit Parameter** 클릭하십시오.
5. 인풋 박스에 API URL 붙여넣기를 하십시오.  URL이 `elasticbeanstalk.com`로 끝날수 있도록 `/`를 제거하십시오.  `/`를 제거하지 않으면 API요청은 실패할것입니다.

이번 바꿈이 효과를 발휘하기위해서는, CodeBuild를 런해야하는데, 왜냐하면 바뀐값은 [플론트단 배포](buildspec.frontend.yml)시간에 읽기 때문입니다.
1. **Developer Tools** 아래 **Code Build**로 가십시오.
2. 당신의 프로젝을 클릭하십시오.
3. **Build History** 섹션에서, 가장 최근 빌드에 첵 하십시오.
4. **Retry** 클릭하십시오.

빌드이름에 클릭하면 진행과정을 볼수있습니다만, 얼마 걸리지 않을것입니다.  빌드가 완성되면, 프론트단은 새로운 프로덕션 환경을 콜하게 될것입니다. 하지만, 우리는 API를 콜할수있는 허가를 주기전까지 그 콜은 성공하지 않을것입니다.  이것은 전에 **ApiRole**에 했던것과 같습니다만, 여기서 우리는 Beanstalk이 생성한 롤을 사용하기 때문에, 읽기허가를 Parameter Store에 주어야 합니다.

1. **Security, Identity & Compliance** 아래 **IAM**로 가십시오.
2. 왼쪽편 **Roles** 클릭하십시오.
3. **aws-elasticbeanstalk-ec2-role** 클릭하십시오. 이 Beanstalk가 EC2 인스턴스를 사용하기위해 만든 롤입니다.
4. **Permissions** 탭에 **Attach policy** 클릭하십시오.
5. 서치바에 클릭한다음 `AmazonSSMReadOnlyAccess`를 찾아서 첵박스에 클릭하십시오.
6. **Attach policy** 클릭하십시오.

이제 우리 인스턴스가 Parameter Store를 접속할수있으나, 아직도 비밀번호가 걸려있는값들은 읽을수 없습니다.  해결책으로 우리 암호화 키에 **aws-elasticbeanstalk-ec2-role**롤을 주고 모두가 접속할수있도록 합니다. 

1. **Security, Identity & Compliance** 아래 **IAM**, **Encryption keys** 가십시오.
2. **Key Users** 섹션까지 스크롤을 내린다음 **This Account** 부섹션 아래 **Add** 클릭하십시오.
3. **aws-elasticbeanstalk-service-role** 롤을 선택하십시오
4. **Attach** 클릭하십시오.

좋습니다. 이제 우리 인스턴스는 Parameter Store 안에 있는 모든 파라미터를 접속할수 있습니다. 여기서 Parameter Store에 값을 읽기위해 서버를 다시 시작해야합니다.

1. **Compute** 아래 **Elastic Beanstalk**로 가십시오.
2. **Conduit** 애플리케이션 아래 **Conduit-prod** 카드를 클릭하십시오.
3. 오른쪽편에 **Action** 클릭하십시오
4. **Restart App Server(s)** 클릭하십시오.

서버가 다시시작되면, API가 작동을 할것입니다.  프로덕션 환경 URL 뒤에 `/api`를 붙이면, API 를 기술한 Django Rest-Framework 페이지를 볼수있습니다.  그리고 맞는 환경에 있는지 확인하기위해 몇몇의 프론엔드링크를 테스트 해보십시오.

---
**도전 과제:**

- 왜 RDS는 아무런 조치를 안했는데 작동하나요?
- 환경을 위해 **Configuration** 선택지에 **Scaling**를 보십시오. **Time-based Scaling** 액션을 클릭하십시오. 그리고 그것이 구성에 어떤변화를 주는지 보십시오.
- 데이타베이스는 확신할수 없나요? 한 인스턴스에 로그인 해서, `postgresql` 를 설치한다음 해보십시오. 팁: Amazon Linux는 [yum](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-software.html)을 사용합니다.
---
**다음:** [결론](/workshop/beanstalk/04-conclusion.md)
