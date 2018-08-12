# Load Balancer 생성하기

Elastic Load Balancing은 Amazon EC2 인스턴스 와 컨테이너, IP 주소와 같은 여러 대상을 통해 들어오는 트래픽을 자동으로 배분한다.

production환경의 응용프로그램을 실핼할때, 우리는 하나가 실행이 불가능하여도 응용프로그램이 작동할 수 있도록 일반적으로 여러 인스턴스를 사용할 것이다. Load Balancer는 트래픽을 받아 응용프로그램의 인스턴스에 전송할 것이다. 
더 자세한 사항은 [여기](https://aws.amazon.com/elasticloadbalancing/)를 참고해 주세요.

1. **컴퓨팅** 섹션의 **EC2** 로 이동한다.
2. 왼쪽 메뉴에서 **로드 밸런싱** 섹션의 **로드밸런서** 선택한다.     
3. **로드 밸런서 생성** 클릭한다.
4. **Application Load Balancer** 선택한다
5. 이름: `aws-workshop-load-balancer` 입력한다.
6. 적어도 2개의 가용 영역 선택한다.
7. **다음: 보안 설정 구성** 클릭한다.
8. **다음: 보안 그룹 구성** 클릭한다.
9. **새 보안 그룹 생성** 선택 후 이름에 `load-balancer-security-group` 입력하고 설명 추가한다.
10. **다음:라우팅 구성** 클릭한다.
11. 이름: `aws-workshop-target-group` 입력한다.
12. 포트: `9000` 입력한다.
13. 경로: `/api/tags` 입력한다.
14. **다음: 대상 등록** 클릭한다.
15. **다음: 검토** 클릭한다.
16. **생성** 클릭한다.
17. **닫기** 클릭한다.

---
**다음:** [Auto Scaling Group 생성하기](/workshop/elb-auto-scaling-group/02-auto-scaling-group.md).
