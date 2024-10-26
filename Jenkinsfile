pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-u root'
        }
    }

    environment {
        HOME = "${env.WORKSPACE}"
        PYTHON_VENV = "SHEHARA_venv"
    }

    stages {
        stage('Checkout') {
            steps {
                cleanWs() // Clean workspace before build
                git url: 'https://github.com/WMSShehara/Selenium-CI-CD-Login-Automation.git', branch: 'main'
            }
        }

        stage('Install ChromeDriver') {
            steps {
                sh '''
                    wget -q -O /tmp/chromedriver_linux64.zip https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.99/linux64/chromedriver-linux64.zip
                    unzip -d /tmp /tmp/chromedriver_linux64.zip
                    mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver
                    chmod +x /usr/local/bin/chromedriver
                    echo "ChromeDriver version: $(chromedriver --version)"
                '''
                sh 'apt-get update && apt-get install -y libnss3'
            }
        }

        stage('Build') {
            steps {
                script {
                    sh '''
                        #!/bin/bash
                        export PATH="${WORKSPACE}/.local/bin:$PATH"
                        python3 --version
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pip freeze
                        ls
                    '''
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                dir('selenium_testing') {
                    sh '''
                        . $PYTHON_VENV/bin/activate
                        python3 --version
                        python3 -m unittest discover -s . -p "*.py"
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }

        success {
            echo 'Build succeeded!'
        }

        failure {
            echo 'Build failed!'
        }
    }
}
