# Add an extra EC2 instance with ELB and auto-scaling
# ELB 와 auto-scaling을 통한 여분의 EC2 추가
In this section we want to add an extra EC2 instance to be able to manage a bigger amount of trafic and improve our performance.
이 번 장에서는 더 많은 양의 트래픽 관리가 가능하고 성능 향상을 위해 여분의 EC2 인스턴스를 추가에 대해 알아보겠다.

To do that we are going to add also a [ELB](https://aws.amazon.com/elasticloadbalancing/) that is going to be the one in charge of distribute the traffic accross our instances.
또한 우리는 인스턴스의 성능을 넘은 트랙픽의 배분 관리를 하는 [ELB](https://aws.amazon.com/elasticloadbalancing/)도 추가할 것이다.

Also we will add an [auto-scaling group](https://aws.amazon.com/documentation/autoscaling/) with 2 availability zones.
또한 우리는 2개의 availability zone에 [auto-scaling group](https://aws.amazon.com/documentation/autoscaling/)을 추가할 것이다.

This way we ensure that if we have 2 instances one on each availability zone, and an [Availability Zone](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions-availability-zones) goes down and our instance terminated, AWS will automatically start a new instance in the other availability zone so we don't decrease our performance.
이것은 우리가 각각의 availability zone에 한개씩 2개의 인스턴스가 있다면, 한 [Availability Zone](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions-availability-zones) 다운되거나 인스턴스가 종료되어도,
AWS는 성능이 떨어지는 것을 막기위해 자동적으로 다른 availability zone의 새로운 인스턴스를 시작할 것이다.

Also we will create some rules to add more instances if our 2 instances are overloaded (example: using 80% of cpu for the last 5 minutes), you can add whatever rule you want.
또한 2개의 인스턴스가 과부화되면 더 많은 인스턴스 추가를 위해 새로운 규칙을 만들 것이다. (ex: 마지막 5분 동안 cpu 사용량 80%), 우리는 원하는 어떤 규칙도 추가할 수 있다.

---
**Next:** [Create a Load Balancer](/workshop/elb-auto-scaling-group/01-load-balancer.md)
