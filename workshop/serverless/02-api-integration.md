## API Integration

Now we want to use our API endpoint we have been using before to have a single API endpoint to all of our API calls. For doing that we will connect our load balancer to fordward all requests to the path `/*/search/*`

Firstly we need to create a new `Target Group` with our lambda registered as the targets.

1. Go to **EC2** under **Computing** section.
2. Click on **Target Groups**.
3. Click on **Create Target Group**.
4. Put a name and choose `Lambda function` as Target Type.
5. Select your lambda and click **Create**

Now we will modify our load balancer to add a fordwarding rule for the new target group.

1. Go to **EC2** under **Computing** section.
2. Click on **Load Balancers** on the left.
3. Select your load balancer, go to the `Listeners` tab and click on `View/edit rules`.
4. Add a new rule with condition `IF` path is `/*/search/*` `THEN` Forward to your Target Grup you created before.
5. Click on **Update**

--- 

This is the end of this part of the workshop. You could continue reading more about serverless architecture in the AWS ecosystem [here](https://aws.amazon.com/serverless/). 

