# 마무리

우리는 거의 끝났습니다. 더 많은 parameter 를 추가해야하며 전체 프로젝트를 배포 할 준비가 되었습니다.

## Parameter Store 에서 API_URL 만들기 
1. **Compute** 섹션 아래에 **EC2**로 이동하십시오.
2. 너의 인스턴스를 선택하십시오.
3. **Description** 아래에 **Public DNS** 를 복사하십시오. 
4. 왼쪽메뉴에 있는 **Parameter Store** 를 선택하십시오.
5. **Create Parameter** 를 클릭하십시오.
6. `/prod/frontend/API_URL` 을 이름으로 입력하고 `http://<public dns you copied>:9000`을 입력하십시오.
7. **Create Parameter** 를 클릭하고 닫으십시오.

이것은 CodeBuild에서 사용되므로 프론트 엔드는 API의 위치를 ​​알고 있습니다. [here] (/ buildspec.frontend.yml)에서 체크할 수 있습니다..

## CodeBuild 프로젝트 실행
1. **Developer Tools** 섹션 아래 있는 **CodeBuild** 로 이동하십시오.
2. 이전에 생성 한 프로젝트를 선택하고 **Start Build** 를 클릭하십시오.
3. **Start Build** 를 클릭하십시오.
4. 잠시만 기다리십시오.
5. 모든 단계가 성공적으로 실행되는지 확인하십시오.
6. 끝.

이제 S3에서 제공하는 공개 URL (under **S3**, your bucket, **Properties**, **Static website hosting**)으로 이동하면 엔드 포인트를 찾을 수 있습니다. 모든 것이 계획대로 진행되면 전체 웹 사이트를 볼 수 있습니다.

---
**다음:** [EC2 instance with ELB and auto-scaling](/workshop/elb-auto-scaling-group/introduction.md)를 추가하십시오.
