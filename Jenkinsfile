pipeline {
    agent any

    options {
        disableConcurrentBuilds()
        timeout(time: 30, unit: 'MINUTES')
    }

    environment {
        EC2_HOST = '65.0.32.30'
        EC2_USER = 'ubuntu'
    }

    stages {
        stage('Detect branch') {
            steps {
                script {
                    def branch = (env.GIT_BRANCH ?: '').replaceFirst(/^origin\//, '')
                    if (!branch || branch == 'HEAD') {
                        error('Could not detect branch. Check the Branch Specifier in the job config.')
                    }
                    env.DEPLOY_BRANCH = branch
                    echo "Deploying branch: ${env.DEPLOY_BRANCH}"
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                withCredentials([file(credentialsId: 'Infoez-Backend-Env', variable: 'ENV_FILE')]) {
                    sshagent(['Infoez-Pem-Key']) {
                        sh '''
ssh -o StrictHostKeyChecking=no $EC2_USER@$EC2_HOST "rm -f /tmp/infoez-backend.env"
scp -o StrictHostKeyChecking=no "$ENV_FILE" $EC2_USER@$EC2_HOST:/tmp/infoez-backend.env
ssh -A -o StrictHostKeyChecking=no $EC2_USER@$EC2_HOST "bash -s -- '$DEPLOY_BRANCH'" <<'REMOTE'
set -euo pipefail
BRANCH="$1"
APP_DIR=/home/ubuntu/Backend

rm -rf "$APP_DIR"
git clone -q -b "$BRANCH" git@github.com:Infoez-kiaq/Backend.git "$APP_DIR"
cp /tmp/infoez-backend.env "$APP_DIR/.env"
chmod 600 "$APP_DIR/.env"
rm -f /tmp/infoez-backend.env

cd "$APP_DIR"
docker build -t inf-backend .
docker rm -f infoez >/dev/null 2>&1 || true
docker run -d --restart unless-stopped -p 8000:8000 --env-file .env --network my-app-network --name infoez inf-backend
REMOTE
'''
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Finished: ${currentBuild.currentResult}"
        }
    }
}
