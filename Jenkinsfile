
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking source code'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python app.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest test_app.py -v'
            }
        }
    }

    post {
        success {
            echo 'Python CI/CD Successful!'
        }
        failure {
            echo 'Python CI/CD Failed!'
        }
    }
}
