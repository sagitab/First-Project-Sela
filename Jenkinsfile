pipeline {
    agent any
    environment {
        IMAGE_NAME= "firstprojectsela"
        CONTAINER_NAME= "ynetapp"
    }

    stages {
        stage('Checkout') {
            steps {
                // Get code from your GitHub repository ok
                git branch: 'main', url: 'https://github.com/sagitab/First-Project-Sela.git'
            }
        }

        stage('Build image') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    # Remove old DinD container if it exists
                    docker rm -f dind-docker || true

                    # Start DinD
                    docker run -d --privileged --name dind-docker --network host -p 2375:2375 docker:23-dind

                    # Wait for DinD daemon to be ready
                    sleep 5

                    # Point Docker commands to DinD
                    export DOCKER_HOST=tcp://localhost:2375
                    docker ps
                    docker build -t ${IMAGE_NAME} .
                '''
            }
        }

        stage('Run container') {
            steps {
                echo 'Running Python script...'
                sh '''
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run --name ${CONTAINER_NAME} --rm ${IMAGE_NAME}
                '''
            }
        }
        stage('Basic health-check'){
            steps{
                sh '''
                    echo "test"
                '''

            }
        }
        
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo '✅ Build completed successfully.'
        }
        failure {
            echo '❌ Build failed.'
        }
    }
}
