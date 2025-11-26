pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = 'subhashh2005' 
        TAG = 'IMT2023104' 
        APP_NAME = 'calculator-app'
        FULL_IMAGE_NAME = "${DOCKER_HUB_USER}/${APP_NAME}:${TAG}"
        DOCKER_CREDS_ID = 'dockerhub-login'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Subhashhari/calculator-cli'
            }
        }

        stage('Setup Venv & Test') {
            steps {
                script {
                    echo ' Creating Virtual Environment...'
                    bat "python -m venv .venv"
                    
                    echo ' Running Tests in Venv...'
                    bat ".venv\\Scripts\\python.exe test_app.py"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Tests passed locally. Building Docker Image...'
                    bat "docker build -t %FULL_IMAGE_NAME% ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo 'Pushing to Docker Hub...'
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDS_ID, passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                        bat "docker login -u %USER% -p %PASS%"
                        bat "docker push %FULL_IMAGE_NAME%"
                    }
                }
            }
        }
    }
    
   post {
        always {
            script {
                echo 'Cleaning up...'
                try {
                    bat "rmdir /s /q .venv"
                } catch (Exception e) {
                    echo "Could not delete .venv (maybe it is already gone)"
                }

                try {
                    bat "docker rmi %FULL_IMAGE_NAME%"
                } catch (Exception e) {
                    echo "Docker image was not found locally to delete. It might have been handled by BuildKit. Ignoring."
                }
            }
        }
    }
}
