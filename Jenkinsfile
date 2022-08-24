pipeline {

    environment {
        imageName = "daniel-waruo/school-api"
        dockerImage = ''
        containerName = "school-api"
        port = 9000
    }

    agent any

     stages {
        stage('PULLING CHANGES') {
            steps {
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building image'
                script {
                    sh "docker-compose build"
                }
            }
        }

        stage('Docker run') {
            steps {
                script {
                   sh "docker-compose up -d"
                 }
            }
        }
    }
}
