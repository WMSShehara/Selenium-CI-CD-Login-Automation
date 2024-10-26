pipeline {
    agent any

    environment {
        PYTHON_VENV = 'venv'  // Virtual environment directory for Python
    }

    stages {
        // Checkout code from GitHub
        stage('Checkout') {
            steps {
                cleanWs() // Clean workspace before build
                git url: 'https://github.com/WMSShehara/Selenium-CI-CD-Login-Automation.git', branch: 'main'
            }
        }

        // Install Node.js dependencies (for Next.js)
        stage('Install Node.js Dependencies') {
            steps {
                dir('my-app') {
                    sh 'npm install'
                }    
            }
        }

        // Build the Next.js project
        stage('Build') {
            steps {
                dir('my-app') {
                    sh 'npm run build'
                }
            }
        }

        // Set up Python environment and install dependencies
        stage('Set Up Python Environment') {
            steps {
                // Install virtual environment if not exists and activate it
                sh 'python3 -m venv $PYTHON_VENV'
                sh '. $PYTHON_VENV/bin/activate'

                // Install dependencies (assuming requirements.txt is present in root)
                sh 'pip install -r requirements.txt'
            }
        }

        // Run Python Selenium tests
        stage('Run Selenium Tests') {
            steps {
                dir('selenium_testing') {
                    // Print Python version for verification
                    sh 'python3 --version'

                    // Run Selenium tests within the virtual environment
                    sh '. ../$PYTHON_VENV/bin/activate && python3 -m unittest discover -s . -p "*.py"'
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
