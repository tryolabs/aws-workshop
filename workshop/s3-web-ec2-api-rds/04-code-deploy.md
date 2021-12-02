# CodeDeploy

[CodeDeploy](http://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) is a service to automate the deployment of any kind of applications to EC2 instances. The configuration is really simple and easy to adapt. The deployment process is described in an `appspec.yml` file like [this one](/appspec.yml). If you want to know what happens during the deploy, you can also check the implementation of the hooks [here](/infrastructure/aws/codedeploy).

First, we need to create a default role for CodeDeploy so it can have access to other AWS services (like S3).

## Create CodeDeploy Role
1. Go to **IAM** under **Security, Identity & Compliance**.
2. Go to **Role** section and click **Create Role**.
3. Select **AWS Service** up top.
4. Select **CodeDeploy** from the **Chose a use case** list.
5. Select **CodeDeploy** from the **Select your use case** section that just appeared.
6. Click **Next: Permissions**.
7. Select **Next: Tags**.
8. Select **Next: Review**.
9. Type a name and description. A good name is `<YourName>CodeDeploy`.
10. Click **Create Role**.

Now we are ready to start using it.

##  Configure Code Deploy
First, let's create an application.
1. Go to **CodeDeploy** under **Developer Tools**.
2. Go to **Applications** and click **Create application**.
   1. Enter an **Application name**. A good name is `<your-name>-workshop`.
   2. On **Compute platform** select **EC2/On-premises**.
3. Click **Create Application**.

An application can have many kinds of deployments (think _production_, _development_ and _staging_). To configure each one, we will create _deployment groups_. Once inside the application:
1. Click on **Create Deployment group**.
2. Enter a Deployment Group name. In this case we won't distinguish between _prod_ or _dev_, so just name it `<your-name>-workshop-deployment-group`.
3. On **Service role** select the role created to grant CodeDeploy access to the instances (probably `<YourName>CodeDeploy`).
4. Select **In-place** on **Deployment Type** section.
5. In **Environment Configuration**:
   1. Check **Amazon EC2 instances**.
   2. Add a tag with `environment` as Key and as Value `prod`.
   3. Add a tag with `service` as Key and as Value `api`.

    This will ensure CodeDeploy deploys the API only to the EC2 instances that are tagged with these exact tags. This is where you would chose the instances used for _prod_ or _dev_.
6. On **Deployment settings** select **CodeDeployDefault.OneAtATime** in Deployment Configurations.
7. Under **Load Balancer** uncheck **Enable load balancing**
8. Click **Create deployment group**

You can get the deployment group's ID (for access to logs) by running
```
aws deploy get-deployment-group \
    --application-name <your-name>-workshop \
    --deployment-group-name <your-name>-workshop-deployment-group \
```
in your computer's console and looking for the key `deploymentGroupId` in the output.

You might need to add a `--profile` flag if you set up `aws` for this workshop with a profile other than `default`.

## Deploy
Now our CodeDeploy application is ready. Let’s try our first deployment.

1. On the deployment group details of the group we just made, click **Create Deployment**
2. On **Repository type** select **"My application is stored in GitHub"**.
3. In **Connect to GitHub** section type your GitHub account and select **Connect to GitHub**.
4. Allow AWS to access your GitHub account, if needed.
5. Enter your repository name in the form _account/repository_.
6. In **Commit ID** type the commit hash that you want to deploy. This will be from the latest commit of your branch (with the fixes to the parameter paths done).
7. Select **Overwrite the content** below.
8. Click **Create Deployment**.

This should leave you inside the deployment page. During the deploy try clicking **View events** next each instance in the **Deployment lifecycle events** table to follow the progress and see what's happening.

Up top you'll see a string like `d-<CHARACTERS>`. That's the deploy ID that you need to access logs in the instance.

## Re deploying
You might need to re deploy the project. Just in case, this is how it's done:

1. Go to **CodeDeploy**.
2. Go to **Applications**.
3. Click your application.
4. Click your deploment group.
5. You can either create a new deployment from scratch or re use an old one.
   1. If creating one from scratch, follow the steps in the previous section.
   2. If re using a deployment, select it and click _Create Deploment_ **after** either:
      - Clicking **Retry deployment** to retry that exact deployment.
      - Clicking **Copy deployment** to get a configuration screen with most details from the selected deployment carried over and changing the Commit ID and click **One at a time** (and change any other settings you need to).

---
**Extra mile:** once the deploy finishes:

- Try hitting the API with something like [Postman](https://www.getpostman.com/) or [httpie](https://httpie.org/).
- What effect did the deploy have? Where did all the Python code end up? Is the API connected with the RDS already? `ssh` in to get all those answers, and more.

---
**Next:** we are going to [finish our first deploy](/workshop/s3-web-ec2-api-rds/05-finishing-up.md), only some extra parameters are missing!
