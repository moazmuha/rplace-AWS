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
r/place clone is an application which allows a user to place a point of the color of thier choice on a canvas. Each user can only place one point every 5 minutes. It is inspired by the original [Place](https://en.wikipedia.org/wiki/Place_(Reddit)) application which was a collaborative project and social experiment created on a subreddit called [r/place](https://www.reddit.com/r/place/). Registered users were only allowed to place a point AKA color a pixel every 5-20 minutes. The project lasted 72 hours. In the early hours it was just a mess of points, however slowly users started to collaborate and created a spectacular work of art. Here is the final product: 
![image](https://user-images.githubusercontent.com/66569506/117082665-d7690c80-ad10-11eb-8f56-350c8060a79b.png)
You can watch a timelapse Place [here](https://www.youtube.com/watch?v=XnRCZK3KjUY).


## Guide 


## Contributors
•[Muhammad Moaz](https://github.com/moazmuha) <br>
•[Muhammad Huzaifa](https://github.com/waifa) <br>

## Notes
If there are any problems and/or you want to contribute to this project please open an issue.

## ToDo
Todo: <br>
•Find out where root directory is for windows, or where aws api checks for credentials and config file <br>
•Add timer<br>
•set up on AWS(EC2, ELB, ASG)<br>
•write out steps for readme
