#!Groovy
pipeline {
    agent any
    environment{
    DOCKERHUB_CREDENTIALS = credentials('docker-push')
    }
    stages {
         stage('1.Git repository') {
            steps {
git credentialsId: 'git-push', url: 'git@github.com:Alkaponees/IKTA-Explorer.git'
            }
        }
        stage('2.Delete all Docker containers') {
            steps {
sh'''#!/bin/sh
chmod +x delete.sh
./delete.sh
'''

            }
        }
        stage('3.Build Docker images') {
            steps {
sh'''#!/bin/sh
docker build -t alkaponees/ikta-explorer:latest .
''' 




            }
        }
         stage('4.Run Docker Container') {
            steps {
sh '''
#!/bin/sh/
docker run -d --restart=always alkaponees/ikta-explorer:latest
'''


            }
        }
        stage('5.Login to Docker') {
            steps {
sh '''
#!/bin/sh/
echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
'''


            }
        }
        stage('6.Push on DockerHub') {
            steps {
sh '''
#!/bin/sh/
docker push alkaponees/ikta-explorer
'''


            }
        }
    
    }
}
