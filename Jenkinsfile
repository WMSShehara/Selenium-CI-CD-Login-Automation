pipeline {
    agent any

    stages {
        //  Checkout code from GitHub
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

        //  Build the Next.js project
        stage('Build') {
            steps {
                dir('my-app') {
                sh 'npm run build'
                }
            }
        }

    
        // Run Python Selenium tests
        stage('Run Selenium Tests') {
            steps {
                dir('selenium_testing') {
                    sh 'python -m unittest discover -s selenium_testing -p "*.py"'
                }
            }
        }

        // Deploy (optional)
        stage('Deploy') {
            steps {
                sh 'echo "Deploying the application..."'
                
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
