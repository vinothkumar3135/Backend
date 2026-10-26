pipeline {
    agent any

    environment {
        IMAGE = "practice-backend"
        TAG   = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Install & Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest -q
                '''
            }
        }
        stage('Build Image') {
            steps { sh 'docker build -t $IMAGE:$TAG -t $IMAGE:latest .' }
        }
        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f $IMAGE || true
                    docker run -d --name $IMAGE -p 8000:8000 --env-file .env $IMAGE:latest
                '''
            }
        }
        stage('Smoke Test') {
            steps { sh 'sleep 5 && curl -f http://localhost:8000/health' }
        }
    }

    post {
        failure { echo 'Pipeline failed - check the stage logs above.' }
    }
}
