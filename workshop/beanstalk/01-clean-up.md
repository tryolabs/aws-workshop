# 제거하기
Beanstalk를 지금의 인프라에 연동하기 위해서, 몇가지 써비스를 없애야 합니다.  현재 셑업은 네개의 컴포넌트 Elastic Load Balancer (ELB), Auto Scaling Group (ASG), Virtual Private Cloud (VPC), 그리고 Relational Database Service (RDS) 있습니다.  Beanstalk은 [VPCs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/vpc.html) 를셑업하지 못하며, 테스팅 환경외의 RDS를 [추천하지](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.RDS.html) 않기때문에, VPC 와 RDS를 뺀 나머지 써비스 ELB and ASG를 지웁니다.

ELB 없애기:
1. AWS 콘솔에서, **Compute** 아래 **EC2** 로 가십시오
2. **LOAD BALANCING** 아래 **Load Balancers** 를 클릭하십시오
3. `aws-workshop-load-balancer` 라고 명명된 로드밸런서를 선택하십시오
4. **Actions** 클릭하십시오
5. **Delete** 선택하십시오
6. **Yes, Delete** 클릭하십시오

이제는 위와 똑같은 실행을 **Target Groups**, **Launch Configurations** 그리고 **Auto Scaling Groups** 하십시오.

ELB와 ASG를 완전히 없앤다음, 사용하던 EC2를 터미네이트 해야합니다.
1. **Compute** => **EC2** 로 가십시오
2. **Instances** 에 클릭하십시오
3. 왼쪽편 첵박스에 Bastion이 아니고 NAT인스턴스인 모든 인스턴스를 선택하십시오
4. **Actions** 클릭하십시오
5. **Instance State** 클릭하십시오
6. Terminate 클릭하십시오
7. **Yes, Terminate** 클릭하십시오

다음은 프로덕션 환경에 애플리케이션을 셋업합니다.

---
**추가 작업:** 모든 인스턴스를 종료 한 다음, 필요없는 보안 그룹은 모두 없앱니다. 이렇게 고장난 셋업을 방치해도 될까요?

---
**다음:** [새로운 앱 만들기](/workshop/beanstalk/02-new-app-environment.md)
