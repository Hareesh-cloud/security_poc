import json
import yaml
import subprocess
# bucket creation
cmd1= "gcloud logging buckets create my_logs_bucket2 --location global --description 'my_logs_bucket2'"
proc = subprocess.Popen(cmd1, stdout=subprocess.PIPE, shell=True)