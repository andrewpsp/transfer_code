 
import jenkins 


  server = jenkins.Jenkins('http://52.53.188.33:8080', username='andrewthompson', password='admin')
  user = serer.get_whoami()
  target_build = server.build_job('post-action-trigger-build-job')
 
  print ("current user is at:" user) 
