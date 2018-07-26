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
1. Go to **CodeDeploy** under **Developer Tools**.
1. **개발자 도구** 아래의 **CodeDeploy** 로 가기.
2. Click your application's name.
2. 응용프로그램 이름을 클릭한다.
3. Select your deployment group and on **Actions** select **Edit**.
3. 배포 그룹을 선택 후 **작업** 에서 **수정** 을 클릭한다.
4. On **Environment configuration** select your Auto Scaling Group on **Auto Scaling groups** tab.
4. **환경구성** 에서 **Auto Scaling 그룹** 탭에서 생성한 Auto Scaling 그룹을 선택한다.
5. Go to **Amazon EC2 instances** tab, and delete all existing Tag groups that we setup earlier.
5. **Amazon EC2 인스턴스** 탭으로 가서 이전에 설정한 모든 태그 그룹을 삭제한다.
6. Check **Enable load balancing**.
6. Check **로드 밸런싱 활성화** 를 클릭한다.
7. On **Load balancer** check **Application Load Balancer**.
7. **로드 밸런서** 에서 **어플리케이션 로드 발랜서** 를 체크한다.
8. Select your target group in the dropdown.
8. 드롭다운 리스트의 타켓 그룹을 선택한다.
9. Click **Save**.
9. **저장** 을 클릭한다..
10. Select your deployment group and on **Actions** click **Deploy new version**.
10. 배포 그룹을 선택 후 **작업** 에서 **새 개정 배포** 를 클릭한다.
**이부분이 조금 달라진 것 같습니다. 현재 GitHub 계정을 인증해야만 되게 되어있습니다.**
11. On **Repository** type select: `My application is stored in GitHub`.
11. **레파지토리 유형** 유형 선택: `GitHub에 어플리케이션 저장`.
12. Repository Name: `tryolabs/aws-workshop`.
12. Repository Name: `tryolabs/aws-workshop`.
13. Get the last commit id and past it in the **Commit ID** field.
14. Then click **Deploy**.
14. **배포** 를 클릭한다.

## Re-run CodeBuild
## CodeBuild 재실행하기
1. Go to **CodeBuild** under **Developer Tools**.
1. **개발자 도구** 아래의 **CodeBuild** 로 가기.
2. Click **Start build**.
2. Click **빌드 시작** 을 클릭한다.
3. Click **Start build**.
3. Click **빌드 시작** 을 클릭한다.

## Update RDS security group
## RDS 보안 그룹 수정하기
To give access to the instances created by the auto scaling to the data base we need to update our Postgres instance security group.

1. Go to **RDS** under **Database**
2. Click **Instances** on the left
3. Select your instance and with the radio button on the left and click **Instance actions** and select **Modify**
4. Scroll to **Security group** under **Network & Security** section
5. Click on the security groups drop down and select `api-security-group`. This is the group we created with the Launch Configuration for our Auto Scaling Group in the [previous section](/workshop/elb-auto-scaling-group/02-auto-scaling-group.md#create-launch-configuration-group).

Now, terminate all your running instances and wait for the Auto Scaling group to start the new ones, this might take some minutes. You can follow the current state of the ASG by going to **EC2**, **Auto Scaling Groups**, select your group and check the **Activity History** and **Instances** tabs. Once the new instances were in place and `running` you should be able to get the full site working on the URL of the load balancer.

---
**Extra mile:** once you have the site running:

- Can you tell which instance is getting the requests?
- Try changing the _Desired_ and _Min_ parameters of the ASG and see what happens.
- Force the launch of new instances by triggering a condition that would make the scale up policy activate (that is, without changing the _Desired_ value).
  > Tip: running `yes > /dev/null &` will max out one of the CPU cores.

- Try running [ab](http://httpd.apache.org/docs/2.2/programs/ab.html) (installed by default on macOS) to stress test the API. Do you see any reaction in the AWS console?

---
**Next:** [VPC configuration and Bastion instance](/workshop/vpc-subnets-bastion/introduction.md).
**다음:** [VPC configuration and Bastion instance](/workshop/vpc-subnets-bastion/introduction.md).