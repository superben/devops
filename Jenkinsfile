def nodeLabel = 'master'
node (nodeLabel){
	
	echo "env.BRANCH_NAME"+env.BRANCH_NAME
	if (env.BRANCH_NAME == 'develop' || env.BRANCH_NAME ==~ /^release\/.*/ || env.BRANCH_NAME == "master" || env.BRANCH_NAME == "production") {
	withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin:/opt/apache-maven-3.5.4/bin'])
	{
		dateVersion = sh(script: "date \"+%Y%m%d%H%M%S\"", returnStdout: true).trim()
		try {
		timestamps {
		stage('Checkout Code') { 
			echo "Begin Checkout Code"
			//git credentialsId: '1vTYN2PCZjd2GkRy5zrU', url: 'https://yldevsvm.faw.com/hqcom-grp/dcep-devops-sample.git'
		    checkout scm
		    
		}
		stage('Code scanning'){
			echo "Begin code scanning"
			def scannerHome = tool 'SonarQube Scanner';
			   withSonarQubeEnv('SonarQube') {
			   sh "${scannerHome}/bin/sonar-scanner \
			   -Dsonar.projectKey=faw-demo \
			   -Dsonar.projectName=faw-demo \
			   -Dsonar.sources=. \
                           -Dproject.settings=faw-demo/sonar-project.properties\
			   -Dsonar.host.url=http://yldevcqa.faw.com:8080\
			   -Dsonar.login=duyong_ibm -Dsonar.password=12345678 \
			   -Dsonar.language=java \
			   -Dsonar.java.binaries=. \
			   -Dsonar.sourceEncoding=UTF-8"
			   }
		}
		//quality gate
                sleep 30
        stage('Quality Gate') {
                    timeout(3) {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            echo "未通过Sonarqube的代码质量阈检查,请及时修改！failure: ${qg.status}"
                        }
                    }
            }

		stage('Build') {
			withMaven(jdk: 'JDK  8u181', maven: 'Maven 3.5.4'){
				sh 'mvn -U clean compile'
			}
		}
		stage('Packaging'){
			withMaven(jdk: 'JDK  8u181', maven: 'Maven 3.5.4'){
				sh 'mvn -U package -Dmaven.test.skip=true'
			}
		}
	
		}
		} catch (err) {
            throw err
        }
		 //junit for develop branch
        if (env.BRANCH_NAME == 'develop') {
            try {
                stage('Unit Test') {
                    sh "mvn clean test  -Dspring.cloud.consul.config.enabled=false -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true  -Ddockerfile.skip -U"
                }
            } finally {
                //junit "${jar_name}/target/surefire-reports/*.xml"
               // jacoco changeBuildStatus: true, maximumMethodCoverage: '100'
            }
        }
			stage('Push Image To Harbor'){
			sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASSWORD} ${REGISTRY_URL}"
			def image = docker.build("${REGISTRY_URL}/${APP_NAME}:v${BUILD_ID}")
            image.push()
	        }
		def flg="${dateVersion}-v${BUILD_ID}"
		echo(flg)
		stage('Deploying tsf'){
			sh 'python3 devopstest.py "${GRP_ID}" "tsf_100011309346/${APP_NAME}" "v${BUILD_ID}"'
		}
	}
	}
}
