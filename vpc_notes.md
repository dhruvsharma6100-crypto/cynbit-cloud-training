VPC Basics

What is a VPC?
A Virtual Private Cloud (VPC) is a logically isolated network in AWS where you can launch and manage AWS resources such as EC2 instances.

Components of a VPC

1. Subnet
A subnet is a smaller network inside a VPC.

-> Public Subnet: Can access the internet.
-> Private Subnet: Cannot directly access the internet.

2. Internet Gateway (IGW)
An Internet Gateway allows resources in a public subnet to communicate with the internet.

3. Route Table
A Route Table contains rules that determine where network traffic is directed.

Example Route:
-> Destination: 0.0.0.0/0
-> Target: Internet Gateway

Simple VPC Structure

Internet --> Internet Gateway --> VPC 10.0.0.0/16 --> Public Subnet 10.0.1.0/24 --> EC2 

Summary
-> VPC provides network isolation in AWS.
-> Subnets divide the VPC into smaller networks.
-> Internet Gateway enables internet access.
-> Route Tables control traffic flow.
-> Public subnets can host internet-facing resources like web servers.