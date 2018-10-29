# Beanstalk

[Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) 는 웹 애플리케이션 배포에 앞서 해야할 일들(보안 그룹, 로드 밸런서 등등)을 걱정할 필요없이 쉽게 배포할수 있도록 해줍니다. 그걸하기위해 우리가 해야할일은 Beanstalk가 해야할일을 지정해주고 기다리는 일뿐입니다.

Beanstalk는 또한 다른 AWS 써비스는 제공하지 않는 몇몇의 나이스한 툴을 제공하는데요.  그들은: 

- 앱 환경(개발, 운영, 테스팅 등등) 매니징.
- 각환경을 핸들할수있는 중앙 대시보드.
- 많은 감시 측정 항목.
- 자세한 현재 상황표시.
- 쉽고 빠른 환경 셋업.

이 글을 쓰고있는 현재, Beanstalk는 Java, PHP, .NET, Node.js, Python, Ruby 로 개발된 앱을 써포트하며, 아마존 리눅스에 도는 여러분 자신들의 콘테이너도 빌드할수있습니다.


이번 섹션에는 현 로드밸런서와 오토 스케일링을 대체할 프로덕션 환경 [외장 RDS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.RDS.html)를  Beanstalk를 사용해서 셋업합니다.

중요한것은 환경을 정확하게 지우기 위해서는, Beanstalk로 생성된 컴포넌트를 임의적으로 바꾸는일을 하지 않아야 합니다.  그래서 우리는 깨끗하게 시작하기 위해 몇가지를 지우고 시작해야 합니다.

---
**다음** [현재 셋업 제거하기](/workshop/beanstalk/01-clean-up.md)
