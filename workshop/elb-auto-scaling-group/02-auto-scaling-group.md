# Auto Scaling Group 생성

Production 응용프로그램은 일시에 증가하는 사용자를 결딜 준비가 되어있어야 한다. 예를 들어, 인기있는 블로그가 배포하면 단시간에 예상했던 것보다 많은 사용자의 요청을 받게 될 것이다. 그러면 우리의 응용프로그램은 모든 트래픽 요청을 감당할 수 없어 중단 될 것이다.

Amazon은 증가하는 로드를 감당할 수 있는 더욱 강력한 응용프로그램을 만드는 방법으로 [Auto Scaling Groups](https://docs.aws.amazon.com/autoscaling/latest/userguide/AutoScalingGroup.html)를 제공한다.

Auto Scaling Group를 만들려면, 우선 시작될 인스턴스의 속성을 기술한 기본적인 템플릿인 [시작 구성](http://docs.aws.amazon.com/autoscaling/latest/userguide/LaunchConfiguration.html)을 만들어야 한다.

## 시작 구성 생성
1. **컴퓨팅** 섹션의 **EC2** 로 이동한다.
2. 왼쪽 메뉴에서 **AUTO SCALING** 섹션의 **시작 구성** 선택한다.
3. **시작 구성 생성** 클릭한다.
4. Ubuntu Server (프리 티어로 사용할 수 있는지 확인하십시요) 를 찾고 선택 클릭한다.
5. `t2.micro` 를 선택하고 **다음: 세부 정보 구성** 클릭한다.
6. 이름: `aws-workshop-auto-scaling-group` 입력한다.
7. **IAM 역활** 에서 선택: `ApiRole`.
8. **고급 세부 정보** 에서, **사용자 데이터** 의 **텍스트** 선택하고 아래 스크립트를 붙여넣는다.
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
    스크립트의 모들 줄 앞에 공백이 없도록 주의한다.
9. **다음: 스토리지 추가** 클릭한다.
10. **다음: 보안 그룹 구성** 클릭한다.
11. **새 보안 그룹 생성** 클릭한다.
12. 보안 그룹 이름: `api-security-group`.
13. 클릭: **규칙 추가**.
14. 유형: **All TCP**.
15. 원본: `load-balancer-security-group` 입력하거나 제한된 것을 선택한다.
16. **검토** 클릭한다.
17. **시작 구성 생성** 클릭하고 추후 인스턴스의 `ssh`에 사용할 키 쌍을 선택한다.

지금 우리는 **시작 구성**을 구성하였고 **Auto Scaling 그룹** 을 생성할 수 있다.

## Auto Scaling 그룹 생성하기
1. **컴퓨팅** 섹션의 **EC2** 로 이동한다.
2. 왼쪽 메뉴에서 **AUTO SCALING** 섹션의 **Auto Scaling 그룹** 선택한다.
3. 클릭: **Auto Scaling 그룹 생성**.
4. 선택: `aws-workshop-auto-scaling-group` 하고 **다음 단계** 선택한다.
5. **그룹 이름** 에 시작 구성과 같은 이름 입력한다.
6. **그룹 크기:** 2. 우리는 어쨌든 약간의 여분을 가지고 시작할 것이다.
7. **서브넷** 에서 모든 사용 가능한 옵션 추가한다.
8. **고급 세부 정보** 에서 클릭: **하나 이상의 로드 밸런서에서 트래픽 수신**.
9. **대상 그룹** 에서 선택 및 클릭: `aws-workshop-target-group`.
10. **다음: 조정 정책 구성** 클릭한다.
11. 선택: **조정 정책을 사용하여 이 그룹의 용량 조정**. 우리는 학습을 위해 toy 조정 정책을 구성할 것입니다. 실제의 시스템에서는 최적의 조정 정책을 구성하기 위해 일부 벤치마킹을 실행하고 응용프로그램의 병목현상을 파악해야 합니다.
12. 조정 범위를 2에서 4개의 인스턴스로 설정한다.
13. 지표유형: `평균 CPU 사용률` 선택 (imagine your app was compute intensive). 대상 값은 80.
14. **인스턴스 필요 시간:** 180 초 동안 워밍업 시간(초). 더 자세한 사항은 [이곳](https://docs.aws.amazon.com/autoscaling/latest/userguide/as-scaling-simple-step.html#as-step-scaling-warmup)을 참고해 주세요.
15. **다음: 알림 구성** 클릭한다.
16. **다음: 태그 구성** 클릭한다.
17. **검토** 클릭한다.
18. **Auto Scaling 그룹 생성** 클릭한다.
19. **닫기** 클릭한다.
---
**다음:** 마지막으로 이제 [파라미터를 수정하고 CodeBuild를 재실행하기](/workshop/elb-auto-scaling-group/03-finishing-up.md) 를 수행하도록 하겠습니다.
