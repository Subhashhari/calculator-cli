pipeline {
    agent any

    environment {
        // UPDATE THESE TWO LINES
        DOCKER_HUB_USER = 'subhashh2005' 
        TAG = 'IMT2023104' 
        
        APP_NAME = 'calculator-app'
        FULL_IMAGE_NAME = "${DOCKER_HUB_USER}/${APP_NAME}:${TAG}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                // UPDATE THIS URL
                git branch: 'main', url: 'https://github.com/Subhashhari/calculator-cli'
            }
        }

        stage('Build & Test') {
            steps {
                script {
                    echo 'Building and Testing...'
                    bat "docker build -t test-calc-image ."
                    bat "docker run --rm test-calc-image python test_app.py"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo 'Pushing...'
                    // This uses the ID "dockerhub-login" you created in Step A
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-login', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                        bat "docker login -u %USER% -p %PASS%"
                        bat "docker tag test-calc-image %FULL_IMAGE_NAME%"
                        bat "docker push %FULL_IMAGE_NAME%"
                    }
                }
            }
        }
    }
    
    post {
        always {
            bat "docker rmi test-calc-image"
        }
    }
}
