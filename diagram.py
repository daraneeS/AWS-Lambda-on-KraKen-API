import diagrams
from diagrams import Cluster, Diagram

from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import Eventbridge
from diagrams.aws.management import Cloudwatch
from diagrams.aws.management import CloudwatchEventTimeBased

with Diagram("Work Flows", show=True):
    with Cluster("AWS"):
        Eventbridge("EventBridge") >> Lambda("Lambda") >> S3("S3")
        
        