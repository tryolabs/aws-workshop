# Finishing up

We are almost done. We have to add some more parameters and we are ready to deploy the whole project.

## Create API_URL on Parameter Store
1. Go to **EC2** under **Compute** section.
2. Select your instance.
3. Copy the **Public DNS** under **Description**.
4. Go to the **Parameter Store** under Systems Manager.
5. Click **Create Parameter**.
6. Enter  `/prod/frontend/API_URL` as name and `http://<public dns you copied>:9000` as value.
7. Click **Create Parameter** and close.

This will be used by CodeBuild, so the frontend knows where the API is. You can check how [here](/buildspec.frontend.yml).

## Run CodeBuild project
1. Go to **CodeBuild** under the **Developer Tools** section.
2. Select the project created before.
3. Click **Start Build**.
4. Wait.
5. Check if all the phases run successfully.
6. Done.

Now, if you go to the public URL provided by S3 (under **S3**, your bucket, **Properties**, **Static website hosting**) you will find the endpoint. If everything went as planned, you should see the complete website.

Remember that the page isn't fully functional. But if you cannot hit the API using Postman, you should try re-deploying with the _latest_ commit ID and re building the project.

---
**Next:** add an extra [EC2 instance with ELB and auto-scaling](/workshop/elb-auto-scaling-group/introduction.md).
