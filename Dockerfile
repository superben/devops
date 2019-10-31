FROM tomcat
MAINTAINER Raymond
WORKDIR /usr/app
Run cd /
COPY target/demo1-0.0.1-SNAPSHOT.jar ./demo1-0.0.1-SNAPSHOT.jar
EXPOSE 80
ENTRYPOINT ["java", "-jar", "demo1-0.0.1-SNAPSHOT.jar"]