# 마무리

지금, 우리는 2개의 EC2 인스턴스와 트래픽을 분산시키는 ELB 및 자동으로 처리량의 확장과 여분을 구성하는 Auto Scaling 그룹을 갖추었다.

[첫 섹션](/workshop/s3-web-ec2-api-rds/05-finishing-up.md)에서, `API_URL` 파라미터에 특정 인스턴스의 DNS 이름을 설정 하였습니다. 지금, 우리는 웹에 로드 밸런서를 통해 요청이 치리되어야 하므로 `API_URL`를 수정해야만 합니다.
또한 CodeDeploy 프로젝트를 수정해야 한다. 지금 Auto Scaling 그룹 사용하고 새로운 인스턴스가 시작될때마다 배포를 실행하여야 한다고 적용해야한다. 
마지막으로, CodeBuild를 S3의 새로운 배포본이 인스턴스 대신 로드 밸런서의 DNS로 처리될 수 있게 재실행해야 한다.

## `API_URL` 수정하기
1. **컴퓨팅** 섹션의 **EC2** 로 이동한다.
2. 왼쪽 메뉴에서 **로드 밸런싱** 섹션의 **로드밸런서** 선택한다.  
3. **설명** 밑의 로드 밸런서의 DNS 이름을 복사한다.
4. 왼쪽 메뉴 중, **파라미터 스토어** 를 선택한다.
5. `/prod/frontend/API_URL` 를 클릭하고 **작업** 의 **파라미터 편집** 를 선택한다.
6. 값: `http://` + 3번에서 복사한 DNS 값을 입력한다.
7. Click **파라미터 스토어** 클릭한다.
8. **닫기** 클릭한다.

## CodeDeploy 프로젝트 수정하기
1. **개발자 도구** 아래의 **CodeDeploy** 로 가기.
2. 응용프로그램 이름을 클릭한다.
3. 배포 그룹을 선택 후 **작업** 에서 **수정** 을 클릭한다.
4. **환경구성** 에서 **Auto Scaling 그룹** 탭에서 생성한 Auto Scaling 그룹을 선택한다.
5. **Amazon EC2 인스턴스** 탭으로 가서 이전에 설정한 모든 태그 그룹을 삭제한다.
6. Check **로드 밸런싱 활성화** 를 클릭한다.
7. **로드 밸런서** 에서 **어플리케이션 로드 발랜서** 를 체크한다.
8. 드롭다운 리스트의 타켓 그룹을 선택한다.
9. **저장** 을 클릭한다..
10. 배포 그룹을 선택 후 **작업** 에서 **새 개정 배포** 를 클릭한다.
**이부분이 조금 달라진 것 같습니다. 현재 GitHub 계정을 인증해야만 되게 되어있습니다.**
11. On **Repository** type select: `My application is stored in GitHub`.
12. Repository Name: `tryolabs/aws-workshop`.
13. Get the last commit id and past it in the **Commit ID** field.

11. **레파지토리 유형** 유형 선택: `GitHub에 어플리케이션 저장`.
12. GitHub 계정: `본인의 GitHub계정` 입력 후 **GitHub 연결** 클릭 후 연결을 한다.
13. **레파지토리 이름** 필드에 및 **Commit ID** 필드 각각 레파지토리 이름과 마지막 commit id를 입력한다.

14. **배포** 를 클릭한다.

## CodeBuild 재실행하기
1. **개발자 도구** 아래의 **CodeBuild** 로 가기.
2. Click **빌드 시작** 을 클릭한다.
3. Click **빌드 시작** 을 클릭한다.

## RDS 보안 그룹 수정하기
Auto Scaling으로 생성된 인스턴스에게 데이터베이스 접근 권한을 부여하려면 Postgres 인스턴스의 보안 그룹을 업데이트 하여야 한다.

1. **데이터베이스** 아래의 **RDS** 로 가기.
2. 왼쪽 **인스턴스** 를 클릭한다.
3. 인스턴스를 선택 후 **인스턴스 작업** 클릭 후 **수정** 을 선택한다.
4. **네트워크 및 보안** 섹션 아래의 **보안 그룹** 까지 스크롤한다.
5. 보안 그룹 콤보박스를 클릭하여 `api-security-group`를 선택한다. 이 그룹은 Auto Scaling 그룹을 위해 시작 구성에서 생성한 것이다. [이전 섹션](/workshop/elb-auto-scaling-group/02-auto-scaling-group.md#create-launch-configuration-group).


이제, 모든 실행중인 인스턴스를 종료하고 Auto Scaling 그룹이 새로운 인스턴스를 시작하기를 기다립니다. 이 작업은 몇 분 정도 걸릴 수 있습니다.
**EC2**, **Auto Scaling 그룹** 이동하여 그룹을 선택하고 **활동 기록** 과 **인스턴스** 탭을 확인하여 Auto Scaling 그룹의 상태를 확인 할 수 있습니다.
새로운 인스턴스가 설치되고 `running` 상태과 되면 로드 밸런서의 URL로 모든 사이트를 사용할 수 있습니다.

---
**추가 사항:** 일단 사이트를 실행하면:

- 요청받고 있는 인스턴스를 알 수 있나요?
- Auto Scaling 그룹에서 _Desired_ 와 _Min_ 파라미터를 변경하고 무슨 일이 일어나는지 확인해 보자.
- 확장 인스턴스 정책을 활성화하는 조건을 트리거하여 새 인스턴스의 시작을 강제 실행하십시오. (즉, _Desired_ 값을 변경하지 않고)
  > Tip: `yes > /dev/null &` 을 실행하면 CPU코어 중 하나가 최대값이 됩니다.
- API 스트레스 테스트를 위해 [ab](http://httpd.apache.org/docs/2.2/programs/ab.html) 를 실행하십시오. (기본적으로 macOS에 설치됨)
AWS 콘솔에 반응이 있습니까?
---
**다음:** [VPC configuration and Bastion instance](/workshop/vpc-subnets-bastion/introduction.md).
