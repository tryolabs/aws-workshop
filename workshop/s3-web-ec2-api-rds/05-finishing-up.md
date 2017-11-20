# Finishing up

We are almost done. We have to add some more parameters and we are ready to deploy the hole project.

## Create API_URL on Parameter Store
1. Go to EC2 under Compute section
2. Select your instance
3. Copy the Public DNS under Description
4. On the left menu select Parameter Store
5. Click get started now
6. Enter  `/prod/frontend/API_URL` as name and `http://<public dns you copied>:9000`
7. Click create parameter and close

This will be used by CodeBuild, so the frontend knows where the API is


## Run CodeBuild project
1. Go to CodeBuild under the Developer Tools section
2. Select the project created before and click Start Build
3. Click Start Build
4. Wait
5. Check if all the phases run successfully
6. Done

Now, if you go to the public URL provided by S3 (under S3, your bucket, properties, static website hosting) you will find the endpoint. If everything went as planned, you should see the complete website.

---
Next: [Add an extra EC2 instance with ELB and auto-scaling](/workshop/elb-auto-scaling-group/introduction.md)
