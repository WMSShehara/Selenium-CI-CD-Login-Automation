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
                    apt-get update
                    echo "Installing ChromeDriver"
                    apt-get install -y wget unzip
                    echo "Downloading ChromeDriver"
                    wget https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip
                    echo "Unzipping ChromeDriver"
                    unzip chromedriver_linux64.zip
                    chmod +x chromedriver
                    echo "Moving ChromeDriver to /usr/local/bin"
                    mv chromedriver /usr/local/bin/
                '''
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv $PYTHON_VENV
                    . $PYTHON_VENV/bin/activate
                    pip install --upgrade pip
                '''
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
