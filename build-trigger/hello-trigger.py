 
import jenkins 

def lambda_handler(event, context):
  server = jenkins.Jenkins('http://52.53.188.33:8080', username='andrewthompson', password='admin')
  user = server.get_whoami()
  target_build = server.build_job('post-action-trigger-build-job')
 
  return  user 
