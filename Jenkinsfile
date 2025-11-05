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
                    docker ps
                    docker build -t "${IMAGE_NAME}" .
                '''
            }
        }

        stage('Run container') {
            steps {
                echo 'Running Python script...'
                sh '''
                    docker run "${IMAGE_NAME}"
                '''
            }
        }
        stage('Basic health-check'){
            steps{
                sh '''
                    echo "Starting health check..."
                    
                    # Wait for app to start
                    sleep 10
                    
                    # Health check with curl
                    if curl -f http://localhost:5000/health; then
                        echo "✅ Health check PASSED"
                    else
                        echo "❌ Health check FAILED"
                        docker logs health-check-container
                        exit 1
                    fi
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
