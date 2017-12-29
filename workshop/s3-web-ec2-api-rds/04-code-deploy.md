# CodeDeploy

First we need to create a default role for CodeDeploy.

## Create CodeDeploy Role
1. Go to IAM under Security, Identity & Compliance.
2. Go to Role section and click Create Role.
3. Select CodeDeploy and click Next: Permissions.
4. Select Next: Review.
5. Type a name and description and click Create Role.

Now we are ready to start using it.

##  Configure Code Deploy
1. Go to CodeDeploy under Developer Tools.
2. Click Get Started Now.
3. Select Custom deployment and then Skip Walkthrough.
4. Enter an Application name and Deployment group name.
5. Select In-place deployment on Deployment Type section.
6. Select Amazon EC2 instances tab on Environment configuration.
7. On the first tag group select `environment` as Key and as Value `prod`, on the second line select `service` as Key and as Value `api`. This means that CodeDeploy will deploy our application to all the EC2 instances with those tags.
8. On Deployment configuration select `OneAtATime`.
9. On Service role select the role created to grant CodeDeploy access to the instances.
10. Click Create application.

Now our CodeDeploy application is ready. Let’s try our first deployment.

1. Under Deployment groups section tick your group and in Actions select Deploy new revision.
2. On Repository type select "My application is stored in GitHub".
3. In Connect to GitHub section type your GitHub account and select Connect to GitHub.
4. Allow AWS to access your GitHub account.
5. Enter your repository name (if you are under an organization, type ORGANIZATION/REPOSITORY).
6. In Commit ID type the commit hash that you want to deploy.
7. Select Overwrite the content.
8. Click Deploy.

---
**Next:** we are going to [finish our first deploy](/workshop/s3-web-ec2-api-rds/05-finishing-up.md), only some extra parameters are missing!
