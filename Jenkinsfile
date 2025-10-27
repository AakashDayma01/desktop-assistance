pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Program Files\\Python311\\python.exe"
        GIT_CREDENTIALS_ID = 'github-credentials' // Replace with your Jenkins GitHub credentials ID
        BRANCH_NAME = 'main' // Change if your branch is different
    }

    stages {
        stage('Checkout SCM') {
            steps {
                echo "🔽 Cloning repository..."
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                echo "🐍 Checking Python version..."
                bat "\"${env.PYTHON_PATH}\" --version"
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "📦 Skipping dependencies installation (no requirements.txt)"
            }
        }

        stage('Run Main Script') {
            steps {
                echo "▶️ Running desktop_assis.py..."
                bat "\"${env.PYTHON_PATH}\" desctop_assis.py"
            }
        }

        stage('Run Tests') {
            steps {
                echo "🧪 Running test_voice_assistant.py..."
                bat "\"${env.PYTHON_PATH}\" -m unittest test_voice_assistant.py"
            }
        }

        stage('Push to GitHub') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo "🚀 All tests passed! Pushing code to GitHub..."
                script {
                    // Configure Git
                    bat '''
                        git config user.name "Jenkins CI"
                        git config user.email "jenkins@example.com"
                    '''
                    // Add and commit changes
                    bat '''
                        git add .
                        git commit -m "Automated commit from Jenkins [ci skip]" || echo "No changes to commit"
                    '''
                    // Push changes using Jenkins credentials
                    withCredentials([usernamePassword(credentialsId: env.GIT_CREDENTIALS_ID, usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
                        bat '''
                            git remote set-url origin https://%GIT_USER%:%GIT_PASS%@github.com/AakashDayma01/desktop-assistance.git
                            git push origin %BRANCH_NAME%
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ Build and Git push completed successfully!"
        }
        failure {
            echo "❌ Build failed — code will not be pushed to GitHub."
        }
    }
}
