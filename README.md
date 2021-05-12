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
5. [Huzaifa TODO notes](#todo)

## Introduction
r/place clone is an application which allows a user to place a point of the color of their choice on a canvas. Each user can only place one point every 5 minutes. It was inspired by the original [Place](https://en.wikipedia.org/wiki/Place_(Reddit)) application which was a collaborative project and social experiment created on a subreddit called [r/place](https://www.reddit.com/r/place/). Registered users were only allowed to place a point AKA color a pixel every 5-20 minutes. The project lasted 72 hours. In the early hours it was just a mess of points, however slowly users started to collaborate and created a spectacular work of art. Here is the final product: 
![image](https://user-images.githubusercontent.com/66569506/117082665-d7690c80-ad10-11eb-8f56-350c8060a79b.png)
You can watch a timelapse of Place [here](https://www.youtube.com/watch?v=XnRCZK3KjUY). We created simple version of place with a 1000x1000 canvas. Users can place points or color pixels every 5 minutes. Points are stored in DynamoDB. The DynamoDB table is checked every 5 seconds for new points. Users are auto updated every 30 seconds or can manually reload the page for quicker updates. The application was deployed on EC2 instances running in an auto-scaling group. An elastic load balancer was used to distribute users across instances. Originally Route53 was used as the DNS service and a domian name was publicly available for users. The boto3 AWS SDK for Python was used to query the DynamoDB points table and also used to insert new points. You may take a look at the various Python scripts for more details.


## Guide
Full AWS setup guide coming soon...


## Contributors
•[Muhammad Moaz](https://github.com/moazmuha) <br>
•[Muhammad Huzaifa](https://github.com/waifa) <br>

## Notes
If there are any problems and/or you want to contribute to this project please open an issue.

## ToDo
Todo: <br>
•Add timer<br>
•set up on AWS(EC2, ELB, ASG)<br>
•write out steps for readme
