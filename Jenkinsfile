pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-u root'
        }
    }

    environment {
        HOME = "${env.WORKSPACE}"
    }

    stages {

        stage('Install ChromeDriver') {
            steps {
                sh 'wget -q -O /tmp/chromedriver_linux64.zip https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.69/linux64/chromedriver-linux64.zip'
                sh 'unzip -d /tmp /tmp/chromedriver_linux64.zip'
                sh 'ls -l /tmp'
                sh 'ls -l /tmp/chromedriver-linux64'
                sh 'mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver'                
                sh 'echo "ChromeDriver location: $(which chromedriver)"'
                sh 'chmod +x /usr/local/bin/chromedriver'
                sh 'apt-get update'
                sh 'apt-get install -y libnss3'
                sh 'chromedriver --version'
                sh 'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
                sh 'apt-get update'
                sh 'apt-get install -y ./google-chrome-stable_current_amd64.deb'
                sh 'google-chrome --version'
            }
        }
        
        stage('Setup Python Virtual Environment') {
            steps {
                sh '''
                     #!/bin/bash
                    export PATH="${WORKSPACE}/.local/bin:$PATH"
                    python3 --version
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip freeze
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                dir('selenium_testing') {
                    sh '''
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
