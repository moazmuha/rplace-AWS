# r/place clone on AWS
•A simple version of the popular r/Place<br>
•r/Place web application written in HTML and JavaScript<br>
•Application ran on docker containers which ran on EC2 instances in an auto-scaling group behind an elastic loadbalancer<br>
•Used boto3 (AWS SDK for Python) to store points and get points from DynamoDB<br>


## Contents
1. [Introduction](#introduction)
2. [Guide](#guide)
3. [Contributors](#contributors)
4. [Notes](#notes)

## Introduction
r/place clone is an application which allows a user to place a point of the color of their choice on a canvas. Each user can only place one point every 5 minutes. It was inspired by the original [Place](https://en.wikipedia.org/wiki/Place_(Reddit)) application which was a collaborative project and social experiment created on a subreddit called [r/place](https://www.reddit.com/r/place/). Registered users were only allowed to place a point AKA color a pixel every 5-20 minutes. The project lasted 72 hours. In the early hours it was just a mess of points, however slowly users started to collaborate and created a spectacular work of art. Here is the final product: 
![image](https://user-images.githubusercontent.com/66569506/117082665-d7690c80-ad10-11eb-8f56-350c8060a79b.png)
You can watch a timelapse of Place [here](https://www.youtube.com/watch?v=XnRCZK3KjUY). We created simple version of place with a 1000x1000 canvas. Users can place points or color pixels every 5 minutes. Points are stored in DynamoDB. The DynamoDB table is checked every 5 seconds for new points. Users are auto updated every 30 seconds or can manually reload the page for quicker updates. The application was deployed on EC2 instances running in an auto-scaling group. An elastic load balancer was used to distribute users across instances. Originally Route53 was used as the DNS service and a domian name was publicly available for users. The boto3 AWS SDK for Python was used to query the DynamoDB points table and also used to insert new points. You may take a look at the various Python scripts for more details.


## Guide
### Setting up r/place on a single AWS instance
1. Clone this repo
2. Create an IAM user with permissions to read/write from DynamoDB(or simply give Administrator Access)
3. Place the credentials from the IAM user into the credentials file
4. Run the createPointsTable.py script to create the table in DynamoDB
5. Create a security group which allows all inbound traffic on ports 8080 and 8081 and traffic from your IP on port 22
6. Create a Ubunutu instance via the EC2 console, attaching the security group from the previous step to the instance
7. SSH into the instance
8. Run each line from the docker.sh file in the instance
9. Your rplace applicatino should be running at this point. Test it by reaching out to http://{InstancePublicIP}:8080/ via your browser

### Setting up r/place as a scalable application behind a load balancer
1. Using the single instance created in "Setting up r/place on a single AWS instance", create an AMI(click on the instance and under Actions -> Image and templates -> Create image) 
2. Use the image to launch a number of instances(choose my AMIs when launching new instances and select AMI from step 1)
3. When launching the instances, on the "configure instance" page, under andvanced details, paste the last two lines from the docker.sh file into the User Data text box. This will start the docker container on the instance on initialization.
4. Go to Target Groups in the EC2 console. Create two new target groups, one with port configuration set to 8080, and one with port configuration set to 8081. Add the instances created in step 3 in the register targets page.
5.  Create a HTTP/HTTPS load balancer, set the listener ports to 8080 and 8081 and forward them to corresponding target groups. Set the security group to the same one as for the instances. Launch the load balancers and once the isntances are registered, test the load balancer by using the DNS name.
6. Create an Auto Scaling Group, create a new launch template where the AMI is the image created in step 1 and the user data is the last two lines of docker.sh as done previously. 
7. Under the "configure advanced details" page when creating the auto scaling group, select attach an existing load balancer and choose the previous two target groups created in step 4. Optionally select new capacities for group size and set scaling policies and create the auto scaling group.
8. Congratulations, you have now created a scalable and redundant load balancing AWS application.


## Contributors
•[Muhammad Moaz](https://github.com/moazmuha) <br>
•[Muhammad Huzaifa](https://github.com/waifa) <br>

## Notes
If there are any problems and/or you want to contribute to this project please open an issue.
