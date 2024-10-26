pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-u root' // Run as root user to install packages
        }
    }

    environment {
        PYTHON_VENV = 'SHEHARA_venv'  // Virtual environment directory for Python
    }

    stages {
        // Checkout code from GitHub
        stage('Checkout') {
            steps {
                cleanWs() // Clean workspace before build
                git url: 'https://github.com/WMSShehara/Selenium-CI-CD-Login-Automation.git', branch: 'main'
            }
        }

      // Install Node.js
    // stage('Install Node.js') {
    //     steps {
    //         script {
    //             def setupScript = sh(script: 'curl -sL https://deb.nodesource.com/setup_14.x -o nodesource_setup.sh', returnStdout: true)
    //             echo "Setup script output: ${setupScript}"
    //             def runSetup = sh(script: 'bash nodesource_setup.sh', returnStdout: true)
    //             echo "Run setup output: ${runSetup}"
    //             def installNode = sh(script: 'apt-get install -y nodejs', returnStdout: true)
    //             echo "Node.js install output: ${installNode}"
    //         }
    //     }
    // }



    //     // Install Node.js dependencies (for Next.js)
    //     stage('Install Node.js Dependencies') {
    //         steps {
    //             dir('my-app') {
    //                 sh 'npm install'
    //             }    
    //         }
    //     }

    //     // Build the Next.js project
    //     stage('Build') {
    //         steps {
    //             dir('my-app') {
    //                 sh 'npm run build'
    //             }
    //         }
    //     }

        // Set up Python environment and install dependencies
        // stage('Setup Python Environment') {
        //     steps {
        //         // Install required packages
        //         sh '''
        //             apt update
        //             apt install -y wget gnupg2
        //             wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
        //             echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
        //             apt update
        //             apt install -y google-chrome-stable python3-venv
        //         '''

        //         // Create the virtual environment
        //         sh 'python3 -m venv $PYTHON_VENV'
                
        //         // Activate the virtual environment and install dependencies
        //         sh '''
        //             . $PYTHON_VENV/bin/activate
        //             pip install -r requirements.txt
        //         '''
        //     }
        // }

        // Install ChromeDriver
         stage('Install ChromeDriver') {
            steps {
                sh 'whoami'
                sh 'wget -q -O /tmp/chromedriver_linux64.zip https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.99/linux64/chromedriver-linux64.zip'
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

        // Build the project
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

        // Run Python Selenium tests
        stage('Run Selenium Tests') {
            steps {
                dir('selenium_testing') {
                    // Print Python version for verification
                    sh '. $PYTHON_VENV/bin/activate && python3 --version'

                    // Run Selenium tests within the virtual environment
                    sh '. $PYTHON_VENV/bin/activate && python3 -m unittest discover -s . -p "*.py"'
                }
            }
        }

        // Deploy (optional)
        stage('Deploy') {
            steps {
                sh 'echo "Deploying the application..."'
                // Add actual deploy steps if needed, like `sh './deploy.sh'`
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
