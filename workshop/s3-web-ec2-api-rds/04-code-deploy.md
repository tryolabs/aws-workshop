# CodeDeploy

[CodeBuild](http://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) 는 모든 종류의 응용 프로그램을 EC2 인스턴스에 자동으로 배포하는 서비스입니다. 이 구성은 정말 간단하고 적응하기 쉽습니다. 배포 프로세스는 [이것](/appspec.yml)과 같은 'appspec.yml` 파일에 설명되어 있습니다. 배포 중에 어떤 일이 발생하는지 알고 싶으면 hook [here](/infrastructure/aws/codedeploy) 의 구현을 확인할 수도 있습니다.

먼저 다른 AWS 서비스 (예 : S3)에 액세스 할 수 있도록 CodeDeploy의 기본 역할을 만들어야 합니다.

## CodeDeploy Role 만들기
1. **Security, Identity & Compliance** 아래 **IAM** 로 이동하십시오.
2. **Role** 섹션으로 이동하고 **Create Role**를 클릭하십시오.
3. **CodeDeploy** 를 선택하고 **Next: Permissions**을 클릭하십시오.
4. **Next: Review** 를 선택하십시오.
5. 이름 및 설명을 입력하고 **Create Role**를 클릭하십시오.

이제 우리는 그것을 사용할 준비가되었습니다.

##  Code Deploy 구성
1. **Developer Tools** 아래에 있는 **CodeDeploy** 로 이동하십시오.
2. **Create application** 를 클릭하십시오.
3. **Application name** 과 **Deployment group name** 를 입력하십시오.
4. **Deployment Type** 섹션에서 **In-place deployment** 를 선택하십시오.
5. **Environment configuration** 탭 에서 **Amazon EC2 instances** 를 선택하십시오.
6. 첫 번째 태그 그룹에서 Key로 `environment` 를 선택하고 값 `prod` 로 두 번째 라인에서 key로`service`를, 값으로 `api` 를 선택합니다. 즉, CodeDeploy는 해당 태그가 있는 모든 EC2 인스턴스에 어플리케이션을 배포합니다.
7. **Deployment configuration** 에서 **OneAtATime** 를 선택하십시오.
8. **Service role** 에서 인스턴스에 대한 CodeDeploy 액세스 권한을 부여하기 위해 만든 역할을 선택합니다.
9. Create application 를 클릭하십시오.

이제 CodeDeploy 애플리케이션이 준비되었습니다. 첫 번째 배포를 시도해 보겠습니다.

1. **Deployment groups** 섹션에서 너의 그룹을 선택하고 **Actions** 에서 **Deploy new revision** 를 선택하십시오.
2. **Repository type** 에서 **"My application is stored in GitHub"** 를 선택하십시오.
3. **Connect to GitHub** 섹션에서 GitHub 계정을 입력하고 **Connect to GitHub** 를 선택하십시오.
4. 필요한 경우 AWS에서 귀하의 GitHub 계정에 액세스하도록 허용하십시오.
5. _account / repository_ 형식으로 저장소 이름을 입력하십시오.
6. **Commit ID** 에 배포하려는 커밋 해시를 입력하십시오..
7. 아래의 **Overwrite the content** 를 선택하십시오.
8. Deploy를 클릭하십시오.

배포하는 동안 **View instances**를 클릭 한 다음 **View events**를 클릭하여 진행 상황을 확인하고 무슨 일이 일어나는지 확인하십시오.

---
**Extra mile:** 배포가 완료되면:

- [Postman](https://www.getpostman.com/) 또는 [httpie](https://httpie.org/) 와 같은 방법으로 API를 실행 해보십시오.
- 배포에 어떤 영향이 있습니까? 모든 파이썬 코드는 어디에서 끝났습니까? API가 이미 RDS와 연결되어 있습니까? `ssh`에서 모든 답변을 얻으십시오.

---
**다음:** 우리는 [Finish-deploy](/workshop/s3-web-ec2-api-rds/05-finishing-up.md) 할 것입니다, 일부 추가 파라미터만 누락되었습니다!
