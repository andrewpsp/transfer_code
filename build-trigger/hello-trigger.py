 
import jenkins 


  server = jenkins.Jenkins('url', username='andrewthompson', password='password')
  user = server.get_whoami()
  target_build = server.build_job($(next))
 
  print ("current user is at:" user) 
