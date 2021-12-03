# Finish integration

Now that we have our instance running we need to adjust some details to make it work with the other components of our infrastructure. Those are: our frontend in S3 and the database in RDS. Now we have to tell the frontend that the API now is reachable in another URL.

First we need the new URL for the API.

1. Go to **Elastic Beanstalk** under **Compute**.
2. Click the **Conduit-prod** card under the **Conduit** application.
3. At the top, in the end of **All Applications**... breadcrumb you have the **Environment ID** and **URL**. Copy that URL.

Now we need to paste the API URL in the Parameter Store read for the frontend.

1. Go to **EC2** under **Compute**.
2. Click on **Parameter Store** under **SYSTEMS MANAGER SHARED RESOURCES**.
3. Select the parameter **/<your-name>/prod/frontend/API_URL**.
4. Click **Actions**, **Edit Parameter**.
5. In the value field past the URL for the API. You may need to remove the last `/` so the URL ends in `elasticbeanstalk.com`. If you left the last path separator all the API calls will fail.

For this change to take effect we need to run CodeBuild because this value is read when the [frontend is deployed](buildspec.frontend.yml).

1. Go to **Code Build** under **Developer Tools**.
2. Click your project name.
3. In the **Build History** section, select the checkbox at the left for the most recent build.
4. Click **Retry**.

You can click the build name to follow the progress, it shouldn't take too long. When the build completes, the frontend will be hitting our new production environment. However, it won't work because we still need to give permissions to access the Parameter Store to our API web instances. This is the same we did in the past with our **ApiRole**, but as we are using the role created by Beanstalk for provisioning our instances now, we need to grant read access to the Parameter Store to that role.

1. Go to **IAM** under **Security, Identity & Compliance**.
2. Click **Roles** in the left pane.
3. Click **aws-elasticbeanstalk-ec2-role**, that's the role created for Beanstalk to use in the EC2 instances.
4. Click **Attach policy** in the **Permissions** tab.
5. Click the search bar and look for `AmazonSSMReadOnlyAccess` and select the checkbox in the left.
6. Click **Attach policy**.

Great, now our instances can access the Parameter Store, but they still can't read the password protected values. To fix this we need to grant access to anyone with the **aws-elasticbeanstalk-ec2-role** role to our encryption keys.

1. In **IAM** under **Security, Identity & Compliance**, go to **Encryption keys**.
2. Scroll down to **Key Users** section and click **Add** under **This Account** sub section.
3. Select the **aws-elasticbeanstalk-service-role** role.
4. Click **Attach**.

Ok, so our instances have full access to all the parameters in the Parameter Store now. We need to restart the server in our prod environment because the values from the Parameter Store are read when the app starts.

1. Go to **Elastic Beanstalk** under **Compute**.
2. Click the **Conduit-prod** card under the **Conduit** application.
3. Click **Action** on the right.
4. Click **Restart App Server(s)**.

When the restart finishes the API should be working. You can navigate to the prod environment URL, append `/api` to get the default Django Rest-Framework page describing the API. Try also to navigate to the front end and inspect some of the requests to confirm that you are using the right environment.

---
**Extra mil:**

- What about the RDS? Why is it working without touching anything?
- Check the **Scaling** card in the **Configuration** options for the environment. Click the gear and a **Time-based Scaling** action. Check how that change impact the configuration.
- Not sure about the database? Login to one of your instance, install `postgresql` and try it yourself. Tip: Amazon Linux use [yum](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-software.html) package manager.

---
**Next:** [conclusion](/workshop/beanstalk/04-conclusion.md)