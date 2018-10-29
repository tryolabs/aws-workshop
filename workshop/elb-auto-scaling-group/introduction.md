# ELB 와 auto-scaling을 통한 여분의 EC2 추가


이 번 장에서는 더 많은 양의 트래픽 관리가 가능하고 성능 향상을 위해 여분의 EC2 인스턴스를 추가에 대해 알아보겠다.

또한 우리는 인스턴스의 성능을 넘은 트랙픽의 배분 관리를 하는 [ELB](https://aws.amazon.com/elasticloadbalancing/)도 추가할 것이다.

또한 우리는 2개의 가용 영역(availability zone)에 [auto-scaling group](https://aws.amazon.com/documentation/autoscaling/)을 추가할 것이다.
이것은 우리가 각각의 가용 영역(availability zone)에 한 개씩 2개의 인스턴스가 있다면, 한 [가용 영역(Availability Zone)](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions-availability-zones)이 다운되거나 인스턴스가 종료되어도, AWS는 성능이 떨어지는 것을 막기위해 자동적으로 다른 가용 영역(availability zone)의 새로운 인스턴스를 시작할 것이다.

또한 2개의 인스턴스가 과부화되는 경우라면 더 많은 인스턴스 추가하는 규칙을 만들어야 할 것이다. (ex: 마지막 5분 동안 cpu 사용량 80%), 우리는 원하는 어떤 규칙도 추가할 수 있다.

---

**다음:** [Load Balancer 생성하기](/workshop/elb-auto-scaling-group/01-load-balancer.md)
