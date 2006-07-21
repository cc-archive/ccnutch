pushd `pwd`
cd $CRAWL_DIR
~/local/tomcat/bin/catalina.sh stop
~/local/tomcat/bin/catalina.sh start
cd `popd`
