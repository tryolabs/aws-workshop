# CodeDeploy

First we need to create a default role for CodeDeploy.

## Create CodeDeploy Role
1. Go to **IAM** under **Security, Identity & Compliance**.
2. Go to **Role** section and click **Create Role**.
3. Select **CodeDeploy** and click **Next: Permissions**.
4. Select **Next: Review**.
5. Type a name and description and click **Create Role**.

Now we are ready to start using it.

##  Configure Code Deploy
1. Go to **CodeDeploy** under **Developer Tools**.
2. Click **Create application**.
3. Enter an **Application name** and **Deployment group name**.
4. Select **In-place deployment** on **Deployment Type** section.
5. Select **Amazon EC2 instances** tab on **Environment configuration**.
6. On the first tag group select `environment` as Key and as Value `prod`, on the second line select `service` as Key and as Value `api`. This means that CodeDeploy will deploy our application to all the EC2 instances with those tags.
7. On **Deployment configuration** select **OneAtATime**.
8. On **Service role** select the role created to grant CodeDeploy access to the instances.
9. Click Create application.

Now our CodeDeploy application is ready. Let’s try our first deployment.

1. Under **Deployment groups** section tick your group and in **Actions** select **Deploy new revision**.
2. On **Repository type** select **"My application is stored in GitHub"**.
3. In **Connect to GitHub** section type your GitHub account and select **Connect to GitHub**.
4. Allow AWS to access your GitHub account, if needed.
5. Enter your repository name in the form _account/repository_.
6. In **Commit ID** type the commit hash that you want to deploy.
7. Select **Overwrite the content** below.
8. Click Deploy.

During the deploy try **View instances** and then **View events** to follow the progress and see what's happening.

---
**Extra mile:** once the deploy is finish:

- Try hitting the API with something like Postman
- What effect the deploy has? Where end up all the Python code? is the API connected with the RDS already? `ssh` has all that answers, and more.

---
**Next:** we are going to [finish our first deploy](/workshop/s3-web-ec2-api-rds/05-finishing-up.md), only some extra parameters are missing!
