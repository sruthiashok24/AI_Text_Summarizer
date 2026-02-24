pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        IMAGE_NAME = 'sruthiashok24/ai-text-summarizer'
        EC2_HOST = 'your-ec2-public-ip'
        EC2_USER = 'ubuntu'
    }

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/sruthiashok24/AI_Text_Summarizer.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo 'Pushing image to DockerHub...'
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push ${IMAGE_NAME}:latest'
            }
        }

        stage('Deploy to EC2') {
            steps {
                echo 'Deploying to EC2...'
                sshagent(['ec2-ssh-key']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_HOST} '
                        docker pull ${IMAGE_NAME}:latest &&
                        docker stop summarizer || true &&
                        docker rm summarizer || true &&
                        docker run -d --name summarizer -p 5000:5000 -e GEMINI_API_KEY=${GEMINI_API_KEY} ${IMAGE_NAME}:latest
                        '
                    """
                }
            }
        }
    }
}