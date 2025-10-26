pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Program Files\\Python311\\python.exe"
        GIT_CREDENTIALS = "github-credentials"  // Jenkins credentials ID for GitHub
        GIT_REPO = "https://github.com/AakashDayma01/desktop-assistance.git"
        BRANCH = "main"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                echo "🔽 Cloning repository..."
                checkout([$class: 'GitSCM', branches: [[name: "${BRANCH}"]],
                          userRemoteConfigs: [[url: "${GIT_REPO}", credentialsId: "${GIT_CREDENTIALS}"]]])
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
                echo "📦 Skipping dependencies installation (no requirements.txt found)"
            }
        }

        stage('Run Main Script') {
            steps {
                echo "▶️ Running desctop_assis.py..."
                bat "\"${env.PYTHON_PATH}\" desctop_assis.py"
            }
        }

        stage('Run Tests') {
            steps {
                echo "🧪 Running unit tests..."
                bat "\"${env.PYTHON_PATH}\" -m unittest test_voice_assistant.py"
            }
        }

        stage('Push to GitHub') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                echo "🚀 All checks passed — pushing code to GitHub safely..."

                // Use Jenkins credentials securely
                withCredentials([usernamePassword(credentialsId: "${GIT_CREDENTIALS}", usernameVariable: 'GIT_USER', passwordVariable: 'GIT_TOKEN')]) {
                    bat """
                        git config user.name "%GIT_USER%"
                        git config user.email "jenkins@local"
                        git remote set-url origin https://%GIT_USER%:%GIT_TOKEN%@github.com/AakashDayma01/desktop-assistance.git
                        git add .
                        git commit -m "Auto commit from Jenkins after successful build" || echo "No changes to commit"
                        git push origin ${BRANCH}
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Build, tests, and push completed successfully!"
        }
        failure {
            echo "❌ Build or tests failed — code was not pushed to GitHub."
        }
    }
}
