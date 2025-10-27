pipeline {
    agent any

    environment {
        PYTHON = "C:\\Program Files\\Python311\\python.exe"
    }

    stages {

        stage('Prepare Workspace') {
            steps {
                echo "🧹 Cleaning workspace and preparing environment..."
                deleteDir()
                checkout scm
            }
        }

        stage('Detect Local Changes') {
            steps {
                echo "🔍 Checking for uncommitted local changes..."
                bat '''
                git status
                git diff --stat
                '''
            }
        }

        stage('Run Local Tests') {
            steps {
                echo "🧪 Running unit tests on updated local code..."
                script {
                    def result = bat(
                        script: "\"${env.PYTHON}\" -m unittest discover -s .",
                        returnStatus: true
                    )

                    if (result != 0) {
                        error("❌ Unit tests failed! Aborting pipeline.")
                    } else {
                        echo "✅ All tests passed successfully!"
                    }
                }
            }
        }

        stage('Commit & Push to GitHub (if tests pass)') {
            steps {
                echo "🚀 Tests passed — committing and pushing updated code to GitHub..."
                script {
                    // Configure Git identity for Jenkins
                    bat '''
                    git config --global user.name "Jenkins CI"
                    git config --global user.email "jenkins@example.com"
                    '''

                    // Ignore unwanted files like .pyc or __pycache__
                    bat '''
                    echo "__pycache__/" >> .gitignore
                    echo "*.pyc" >> .gitignore
                    git add .gitignore
                    '''

                    // Add and commit if there are changes
                    bat '''
                    git add .
                    git diff --cached --quiet || git commit -m "✅ Auto commit by Jenkins after successful tests"
                    '''

                    // Authenticate and push
                    withCredentials([usernamePassword(credentialsId: 'github-credentials', passwordVariable: 'GIT_PASS', usernameVariable: 'GIT_USER')]) {
                        bat '''
                        echo "🔄 Fetching latest changes from GitHub..."
                        git remote set-url origin https://%GIT_USER%:%GIT_PASS%@github.com/AakashDayma01/desktop-assistance.git
                        git fetch origin main

                        echo "📦 Rebasing local commits on top of latest main..."
                        git rebase origin/main || (echo "⚠️ Rebase failed, aborting..." && git rebase --abort && exit /b 1)

                        echo "📤 Pushing code to GitHub..."
                        git push origin HEAD:main
                        '''
                    }
                }
            }
        }
    }

    post {
        failure {
            echo "❌ Build failed — changes were NOT pushed to GitHub."
        }
        success {
            echo "🎉 Build succeeded — all tests passed and code pushed successfully!"
        }
        always {
            echo "📝 Build complete. Review console output for details."
        }
    }
}
