pipeline {

    agent any

    environment {

        AWS_REGION = 'ap-south-1'
        AWS_ACCOUNT_ID = '997752498626'
        ECR_REPOSITORY = 'devops-cicd'
        IMAGE_NAME = 'devops-app'
        ECR_REGISTRY = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"
        ECR_IMAGE = "${ECR_REGISTRY}/${ECR_REPOSITORY}:latest"

    }

    stages {

        stage('Get Source') {

            steps {

                checkout scm

            }

        }

        stage('Application Check') {

            steps {

                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements.txt
                    ./venv/bin/python -m py_compile app.py
                '''

            }

        }

        stage('Create Docker Image') {

            steps {

                sh 'docker build -t ${IMAGE_NAME}:latest .'

            }

        }

        stage('Connect to ECR') {

            steps {

                sh '''
                    aws ecr get-login-password --region ${AWS_REGION} |
                    docker login --username AWS --password-stdin ${ECR_REGISTRY}
                '''

            }

        }

        stage('Prepare ECR Image') {

            steps {

                sh 'docker tag ${IMAGE_NAME}:latest ${ECR_IMAGE}'

            }

        }

        stage('Upload Image') {

            steps {

                sh 'docker push ${ECR_IMAGE}'

            }

        }

    }

    post {

        success {

            echo 'DevOps pipeline completed successfully.'

        }

        failure {

            echo 'Pipeline execution failed. Check the stage logs.'

        }

    }

}