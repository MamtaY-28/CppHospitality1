import json
import time
from DynamoDBsettings import cloudWatch
class cloudWatchLog:
    
    def logFunction(retrunValue):
         # Get the current timestamp
        timestamp = int(time.time() * 1000)
        response=cloudWatch.put_log_events(
        logGroupName='x22245855_log',
        logStreamName='log_Stream_Name',
        logEvents=[
            {
                'timestamp':timestamp,
                'message':json.dumps(retrunValue)
            }
        ]

)