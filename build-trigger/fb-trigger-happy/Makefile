
virtual:
  @echo "-->> setup and activate virutalenv"
  if test ! -d  "$(VIRTUAL_ENV)" ; then \
    pip install virtualenv; \
    virtualenv $(VIRTUAL_ENV); \
  fi 
  @echo ""


build_pacakge_location: 
  mkdir -p ./trigger-package/lib
  cp -a ./$(PROJECT)/ . ./trigger-packages

copy_python: 
  if test -d $(VIRTUAL_ENV)/lib; then \
    cp -a $(VIRTUAL_ENV)/lib/python2.7/site-packages/trigger-package
  fi
  if test -d $(VIRTUAL_ENV)/lib64; then \
    cp -a $(VIRTUAL_ENV)/lib64/python2.7/site-packages . ./trigger-pacakges; \
  fi 



zip: 

  cd ./trigger-packages/lib && zip -r ../$(PROJECT).zip



