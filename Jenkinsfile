pipeline {
    agent any

    environment {
        PYTHON = "C:\\Program Files\\Python311\\python.exe"
    }

    stages {

        stage('Prepare Workspace') {
            steps {
                echo "🧹 Preparing Jenkins workspace (keeping synced code from watcher.py)..."
                // ❌ Removed deleteDir()
                // ❌ Removed checkout scm (we keep watcher-synced local files)
                bat "git init"
                bat "git remote remove origin || echo 'No remote to remove'"
                bat "git remote add origin https://github.com/AakashDayma01/desktop-assistance.git"
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
                echo "🧪 Running tests on updated local code..."
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
                    bat '''
                    git config --global user.name "Jenkins CI"
                    git config --global user.email "jenkins@example.com"
                    '''

                    // Ignore cache files
                    bat '''
                    echo "__pycache__/" >> .gitignore
                    echo "*.pyc" >> .gitignore
                    git add .gitignore
                    '''

                    // Add and commit only if there are changes
                    bat '''
                    git add .
                    git diff --cached --quiet || git commit -m "✅ Auto commit by Jenkins after successful tests"
                    '''

                    // Authenticate and push
                    withCredentials([usernamePassword(credentialsId: 'github-credentials', passwordVariable: 'GIT_PASS', usernameVariable: 'GIT_USER')]) {
                        bat '''
                        git remote set-url origin https://%GIT_USER%:%GIT_PASS%@github.com/AakashDayma01/desktop-assistance.git
                        echo "📦 Pulling latest main before pushing..."
                        git pull --rebase origin main || echo "⚠️ Pull failed, continuing with local changes..."
                        echo "📤 Pushing local code to GitHub..."
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
            echo "🎉 Build succeeded — local updates tested and pushed to GitHub successfully!"
        }
        always {
            echo "📝 Build complete. Review console output for details."
        }
    }
}
