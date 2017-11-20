
# Add an extra EC2 instance with ELB and auto-scaling

In this section we want to add an extra EC2 instance to be able to manage a bigger amount of trafic and improve our performance.

To do that we are going to add also a [ELB](https://aws.amazon.com/elasticloadbalancing/) that is going to be the one in charge of distribute the traffic accross our instances.

Also we will add an [auto-scaling group](https://aws.amazon.com/documentation/autoscaling/) with 2 availability zones. 
This way we ensure that if we have 2 instances one on each availability zone and an Availability Zone goes down and our instance terminated, AWS will automatically start a new instance in the other availability zone so we don't decrease our performance.
Also we will create some rules to add more instances if our 2 instances are overloaded (example: using 80% of cpu for the last 5 minutes), you can add whatever rule you want.

---
Next: [Create a Load Balancer](/workshop/elb-auto-scaling-group/01-load-balancer.md)
