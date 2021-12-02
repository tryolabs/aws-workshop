# RDS

## Create a PostgreSQL instance in RDS
1. Go to **RDS** under **Database** section.
2. Click on **Create Database**.
3. Select the engine by:
    1. Clicking on PostgreSQL logo.
    2. Choosing a _Version_ with version major 12 (i.e.: PostgreSQL 12.8-R1).
        
        At the time of writing, PostgreSQL 13 is not included in the free tier but 12 is.
4. Under **Templates** section tick the _"Free Tier"_ checkbox.
5. Enter a name on _DB Instance identifier_ (we will need it later, so don’t forget it).
6. Enter a username and password and click Next (again, we will need these later). Save these in your password manager.
7. Under the **Connectivity** section:
    1. Verify that **Public Access** is set to No.
    2. On **VPC security groups** choose _Select existing VPC security groups_.
    3. Select the security group you created when [launching the EC2 instance](/workshop/s3-web-ec2-api-rds/02-EC2-instances.md#launch-your-first-ec2-instance). If you followed the naming recommendation, this name should be `<your-name>-workshop-ec2-security-group`.
8. Pick an _Initial database name_ under **Additional Configuration** (again, we will need the database name later).
9. Click create Database.

Now our instance is created. We configured its access, allowing every instance under the security group that was created in the previous section to connect.

## Add DB parameters on Parameters Store

As before, we will need some variables stored in the parameter store, including the database name, username, password and endpoint. These variables are referenced in [this file](/backend/conduit/settings/ec2.py), so Django can access the database.

1. Go to **RDS** under **Database** section.
2. Click on Instances.
3. Wait for the instance to get created. 
4. Once done, click the name.
    1. Copy the **Endpoint**. This will be the value for `DATABASE_HOST`.
4. Go to AWS console **Systems Manager** under **Management & Governance**.
5. On the left menu select **Parameter Store**.
6. Click Create Parameter.
7. Enter  `/prod/api/DATABASE_NAME` as the name and a meaningful description like "Name of the PostgreSQL database".
8. Enter the DB name you selected before on the value attribute.
9. Click create parameter and close.
10. Now we will need to do the same thing for the username and host
  1. For the username enter `/prod/api/DATABASE_USER` as the name and your database username and as the value
  2. For the host enter `/prod/api/DATABASE_HOST` as the name and the hostname you copied earlier as the value
11. For `/prod/api/DATABASE_PASSWORD` do the same steps but select as **Type: Secure String** and as KMS Key ID the key `workshopkey`.

Now we have our database parameters set, and the password encrypted. Only our EC2 instances will be able to decrypt it.

---
**Extra mile:**

- Can you `ping` the Postgres instance?
- Try to connect to the DB through your running EC2 instance.

---

**Next:** create a [CodeDeploy project to deploy your API](/workshop/s3-web-ec2-api-rds/04-code-deploy.md).
