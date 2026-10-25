
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m pip --version'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t fuugaa/cloud-cicd-lab:latest .'
            }
        }

        stage('Docker Hub Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_TOKEN'
                )]) {
                    sh '''
                        echo "$DOCKER_TOKEN" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push fuugaa/cloud-cicd-lab:latest
                        docker logout
                    '''
                }
            }
        }
    }
}
