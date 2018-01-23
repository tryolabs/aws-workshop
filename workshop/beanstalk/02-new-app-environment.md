# Create new app

> **Important:** these steps refer to the last UI available for Elastic Beanstalk. If the Elastic Beanstalk site asks you to _opt in_ to a new UI choose to use it.

Now we are going to start using Beanstalk to manage our production environment. First we need to create a new application.

1. Go to **Elastic Beanstalk** under **Compute**.
2. Click **Create New Application** on the top right.
3. Set the **Application Name** to `Conduit`
4. Click **Create**

Now we have a new application without any environment so we are going to add a new one. To provision our new environment we need to give to Beanstalk a snapshot of our app in a zip file ([here](/workshop/backend/beanstalk_deploy.zip) is the one we are going to use), this is how the deploys work in Beanstalk. When we upload a new snapshot Beanstalk extract it, install all the dependencies declared in `requirements.txt` and execute the actions declared in a special folder called [.ebextensions](/workshop/backend/.ebextensions). Check the content of that folder for more details.

1. Click **Actions**, **Create environment**
2. Now we have to choose an _"environment tier"_, we have: [Web server environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-worker.html) for web apps that handle HTTP requests and [Worker environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-worker.html) for apps that handle input from an AWS serial queue, typically for long running tasks. We are going to select **Web server environment** and click **Select**
3. Change **Environment name** to `Conduit-prod`
4. In **Domain** put `conduit-prod` and click **Check availability**.
5. Click on **Choose a platform** and select **Python** under **Preconfigured**
6. Select **Upload your code** in **Application code** and click **Upload**.
7. Now you could choose a location on your local machine or a bucket on S3, we are going to use [this zip](/workshop/backend/beanstalk_deploy.zip) so download it, click on **Choose file** and select the zip.
8. On **Version label** put a mining full description like _"First version"_
9. We could terminate the process now and we will have a working environment with an ELB and ASG properly set up. But we need to configure other details to like use our VPC and the RDS instance. So instead we are going to click **Configure more options**.
10. Choose **Custom configuration** under **Configuration presets**. Look how the options change for every preset.

This is an important step, here we can control almost all the aspects regarding how our instances are going to be provisioned and how to configure their environment and behavior (ELB and ASG). Do you remember how much details we need to take into account to setup these parameters by hand? This is one of the stronger points in use Beanstalk.

Take a moment to investigate this screen, don't make any change but look around. This dashboard is going to be available to make changes to the environment when we finish.

1. Now go to the **Security** card and click **Modify**
2. Click on **Choose a key pair** on the **Virtual machine permissions** and select the key pairs you created during the workshop.
3. Click **Save**. If you pay attention you will notice that we are leaving the **IAM instance role** in the default value instead of using the **_ApiRol_** we create before to provisioning our instances. That's because we need an extra set of permissions already put together in a default role created by Beanstalk for this purpose.

Now we are going to setup our environment to use the VPC we have in place.

1. Go to **Network** card and click **Modify**
2. Scroll to the top and click the dropdown next to the **VPC** field and select your VPC.
3. In the **Load balancer settings** section make sure the **Visibility** dropdown has the **Public** option selected.
4. Under **Load balancer subnets**, select the checkbox on the left for the public subnets (those are with the CIDR 10.0.1.0/24 and 10.0.3.0/24).
5. In **Instance settings** go to **Instance subnets** grid and select the privates subnets (the ones with CIDR 10.0.2.0/24 and 10.0.4.0/24).
6. In **Instance security groups** select the group with name **default**.
7. Click **Save**
8. Click **Create environment**

Now the setup of the environment is running. When it finishes we are going to have a full working load balancer with an auto scaling group that start instances with our app in the VPC we setup earlier.

When the setup finish you will land on the environment dashboard. At the top is the URL associated with the load balancer, next to the **All Applications** > **Conduit** > **Conduit-prod**. Try clicking that URL and append the `/api`. You should get an error now because we still need to push some buttons but the API is there.

If for some reason the deploy fails take a look at [this troubleshooting](/workshop/beanstalk/troubleshooting.md). If you fill comfortable with the command line there is a CLI tool to interact with Elastic Beanstalk that is much more comfortable to use than the AWS console for maintenance tasks. Check [here](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html) for more.

---
**Extra mil:**

- Once the setup finish take a look at how Beanstalk did the setup for the ELB and ASG. Is it different than the one we do? how?
- You should have your bastion instance running (if not take a look on [how to run one](/workshop/vpc-subnets-bastion/07-bastion.md)) so why not try to log to the new instance? Tip: the username for Amazon Linux is `ec2-user`

---
**Next:** [finish integration](/workshop/beanstalk/03-finish-integration.md)