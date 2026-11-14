
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
                bat '"C:\\Users\\sys11\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\sys11\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest test_app.py -v'
            }
        }

        stage('Run Application') {
            steps {
                echo 'Python application is ready!'
                bat '"C:\\Users\\sys11\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" app.py'
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
