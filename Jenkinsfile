
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
                bat 'python --version'
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m py_compile app.py'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t cloud-cicd-lab:latest .'
            }
        }
    }
}
