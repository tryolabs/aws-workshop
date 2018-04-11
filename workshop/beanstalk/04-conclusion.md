# Conclusion

If everything went as expected you have now a running production-ready environment accessible from the same frontend as before. Take some time to explore what Beanstalk offer from the environment dashboard. There are plenty of interesting metrics and health status reports.

The more valuable feature of Beanstalk is the ability to setup and terminate environments for the same application independently. This makes a big difference when you are working on a real project where the changes have to be tested before move to production, new people come to the project and other leave, you need to demo things without the risk of some other team member break the app because it's on active development, etc. In that kind of situations is where Elastic Beanstalk shine.

---
**Extra mil:**

- Thinking about the later our current app architecture (frontend in S3 and API in EC2) is not the ideal combination for taking the most out of multi-environment scenarios. There are many options on how to do this and there are all good and bad depending on the case. Try to think about this and come up with your idea of how can you make the environment management more simple and implement it.

What is the big pain point?

- We mentioned [earlier](/workshop/beanstalk/introduction.md) that letting Beanstalk manage your RDS instances is **not** recommended for production environments. This is because in order to handle your environment configuration Beanstalk needs to handle the life time of your instances like if they were stateless entities. A database is the opposite of that.

Try creating a new environment with an internal RDS called **Conduit-staging**.