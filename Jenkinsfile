pipeline {
   
    }

     environment {
        HOME = "${env.WORKSPACE}"
    }

    stages {
        // Checkout code from GitHub
        stage('Checkout') {
            agent any
            steps {
                cleanWs() // Clean workspace before build
                git url: 'https://github.com/WMSShehara/Selenium-CI-CD-Login-Automation.git', branch: 'main'
            }
        }

        // Install ChromeDriver
       stage('Install ChromeDriver') {
        agent {
                docker {
                    image 'python:3.9'
                    args '-u root'
                }
        steps {
            sh 'wget -q -O /tmp/chromedriver_linux64.zip https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.99/linux64/chromedriver-linux64.zip'
            echo 'Unzipping chromedriver_linux64.zip...'
            sh 'unzip -d /tmp /tmp/chromedriver_linux64.zip'
            echo 'Moving chromedriver to /usr/local/bin...'
            sh 'mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver'
            echo 'Setting permissions for chromedriver...'
            sh 'chmod +x /usr/local/bin/chromedriver'
            echo 'ChromeDriver version:'
        }
    }
        // Build the project
        stage('Build') {
            agent {
                docker {
                    image 'python:3.9'
                    args '-u root'
                }
            }
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

        // Run Python Selenium tests
        stage('Run Selenium Tests') {
            agent {
                docker {
                    image 'python:3.9'
                    args '-u root'
                }
            }
            steps {
                dir('selenium_testing') {
                    // Print Python version for verification
                    sh '. $PYTHON_VENV/bin/activate && python3 --version'

                    // Run Selenium tests within the virtual environment
                    sh '. $PYTHON_VENV/bin/activate && python3 -m unittest discover -s . -p "*.py"'
                }
            }
        }

    }

    // Post-build actions 
    post {
        always {
            // Clean up workspace after build
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
