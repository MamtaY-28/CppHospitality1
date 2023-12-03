import boto3
# Initialize the DynamoDB client
dynamodb =  boto3.client(
                'dynamodb',
               aws_access_key_id="ASIATUYJP7SUCX7WMTUO",
          aws_secret_access_key="uZHg5d9lC1yw/P2kzYHBkVDCv2peCn5GSYh+/WST",
          aws_session_token="IQoJb3JpZ2luX2VjEMj//////////wEaCXVzLWVhc3QtMSJHMEUCIEqy7MSWYd0G951+VFO7UShjsqMbj7T+ZCdd67Lp4YxyAiEAppiRoAm/hS+E9msZ/hzKzSB3q9PMHAXU73Z/bEyDcG4q+wMIMRADGgwyNTA3Mzg2Mzc5OTIiDI7KFWczWg5XsI5meSrYA/7Rmtjy9I5Mw4wO7UZ2pAKLtZOvilKqlauN1FvKPAmZwcet3eRP0d/d4umq8MU/aiW5rkdwOYavAcyKH+N06kUekkLen2BKHvk/Sg/XUM1aO9OjbA86JqG5wKTLX8iM37OpHgMCRSlk2CfyrboHE9ZSgo1AkmiBei+hd4p63oKoaRhPy50zVNo+cTeSrrH9yZISv1dHUmCrmjksMsrK8AWNU12hQBnSLyDWbbp7dDPWqqKX05qle0aVNxErg3N3CUd38Yc8wp+5oJ7ODyRQnapYpYcUm2xOaUP4gbWk3w9kG2lVD7V2CEmImW+J8aHp5MGniZ4W7ZTlE4fqOygkD2I5WUsW1R6FCMeYSPh7zpFr+o8H+/P41KqdzFU3eQDfggLw6o2kCGHQ8X6mk9DQ5dP67IkeNbTTHZTIeYluRTsYyKZhyuppA71jx7xmFDctx0C/TkIEVX09BHLlN37xQGKfO8v4tAdV+DMqjgJNjnP0x/2z5Md7uOQ6KWuMumU9RF3QCDS7aX0WMGEDxnxSzwsz+nBW/6eafh6r5jSYu0WHNfQFO5jcayeuFCimMnQVmEha92BhvyI9vzM+TgLBbFtXgLWijc5p61uH8krdfTXwYeb26OIAcXYw7qitqwY6pgEnePJsNzH9THu9spKKr29SOFjnuIRNQL8i7+SYFqOrGw7m1ELwznAaE1PA7ye/YaIXVCo4ELje/HRTVFLra+NhXi9hmp98VVOryrO6xhSmvoQYY+edcy8VSeqoxiYEE9qnTT0mLK2o78TifISdYquBMGnJVISknlFrvfTJXoOO76h7Y5/Z0dFOpnJ8OlxvsTe0a6XlOpfa29LJOhhJW7zYERIQ1yJB",
           region_name="eu-west-1"   
            )


# Initialize CloudWatch
cloudWatch =  boto3.client(
                'logs',
                    aws_access_key_id="ASIATUYJP7SUCX7WMTUO",
          aws_secret_access_key="uZHg5d9lC1yw/P2kzYHBkVDCv2peCn5GSYh+/WST",
          aws_session_token="IQoJb3JpZ2luX2VjEMj//////////wEaCXVzLWVhc3QtMSJHMEUCIEqy7MSWYd0G951+VFO7UShjsqMbj7T+ZCdd67Lp4YxyAiEAppiRoAm/hS+E9msZ/hzKzSB3q9PMHAXU73Z/bEyDcG4q+wMIMRADGgwyNTA3Mzg2Mzc5OTIiDI7KFWczWg5XsI5meSrYA/7Rmtjy9I5Mw4wO7UZ2pAKLtZOvilKqlauN1FvKPAmZwcet3eRP0d/d4umq8MU/aiW5rkdwOYavAcyKH+N06kUekkLen2BKHvk/Sg/XUM1aO9OjbA86JqG5wKTLX8iM37OpHgMCRSlk2CfyrboHE9ZSgo1AkmiBei+hd4p63oKoaRhPy50zVNo+cTeSrrH9yZISv1dHUmCrmjksMsrK8AWNU12hQBnSLyDWbbp7dDPWqqKX05qle0aVNxErg3N3CUd38Yc8wp+5oJ7ODyRQnapYpYcUm2xOaUP4gbWk3w9kG2lVD7V2CEmImW+J8aHp5MGniZ4W7ZTlE4fqOygkD2I5WUsW1R6FCMeYSPh7zpFr+o8H+/P41KqdzFU3eQDfggLw6o2kCGHQ8X6mk9DQ5dP67IkeNbTTHZTIeYluRTsYyKZhyuppA71jx7xmFDctx0C/TkIEVX09BHLlN37xQGKfO8v4tAdV+DMqjgJNjnP0x/2z5Md7uOQ6KWuMumU9RF3QCDS7aX0WMGEDxnxSzwsz+nBW/6eafh6r5jSYu0WHNfQFO5jcayeuFCimMnQVmEha92BhvyI9vzM+TgLBbFtXgLWijc5p61uH8krdfTXwYeb26OIAcXYw7qitqwY6pgEnePJsNzH9THu9spKKr29SOFjnuIRNQL8i7+SYFqOrGw7m1ELwznAaE1PA7ye/YaIXVCo4ELje/HRTVFLra+NhXi9hmp98VVOryrO6xhSmvoQYY+edcy8VSeqoxiYEE9qnTT0mLK2o78TifISdYquBMGnJVISknlFrvfTJXoOO76h7Y5/Z0dFOpnJ8OlxvsTe0a6XlOpfa29LJOhhJW7zYERIQ1yJB",
           region_name="eu-west-1"   
            )
