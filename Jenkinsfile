pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        GROQ_API_KEY = credentials('groq-api-key')
        IMAGE_NAME = 'sruthi23z272/ai-text-summarizer'
        EC2_HOST = '13.201.28.34'
        EC2_USER = 'ec2-user'
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
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo 'Logging into DockerHub...'
                sh """
                    echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin
                """
                echo 'Pushing image to DockerHub...'
                sh "docker push ${IMAGE_NAME}:latest"
            }
        }

        stage('Deploy to EC2') {
            steps {
                echo 'Deploying to EC2...'
                sshagent(['ec2-ssh-key']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_HOST} "
                        docker pull ${IMAGE_NAME}:latest &&
                        docker stop summarizer || true &&
                        docker rm summarizer || true &&
                        docker run -d --name summarizer -p 5000:5000 -e GROQ_API_KEY='${GROQ_API_KEY}' ${IMAGE_NAME}:latest
                        "
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully! Application deployed to EC2.'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}