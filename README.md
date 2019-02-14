# Naga_Challenge
SED Coding Challenge (Infrastructure and Python)

CODING Challenge:
credit_card_validation.py - It validates N credit cards from ABCD Bank has the following characteristics:
► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.

For Infrastrucre code has 3 parts. 
cf_temp_ansible.yml file to trigger the intiation of instance creation for webserver with load balancer and autoscaling group behind it in a default VPC setting.
apache.yml to install apache on the launched instance and copy the index.html file which has our basic hello world code
