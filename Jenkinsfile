pipeline {
    agent any

    environment {
        PYTHON = "C:\\Program Files\\Python311\\python.exe"
    }

    stages {
        stage('Prepare Workspace') {
            steps {
                echo "🧹 Preparing Jenkins workspace (attached to main branch)..."
                bat '''
                if exist .git (
                    echo "✅ Repo exists — cleaning..."
                    git reset --hard
                    git clean -fd
                    git checkout main || git checkout -b main origin/main
                    git branch --set-upstream-to=origin/main main
                    git pull origin main
                ) else (
                    echo "🆕 Initializing repository..."
                    git init
                    git remote add origin https://github.com/AakashDayma01/desktop-assistance.git
                    git fetch origin main
                    git checkout -b main origin/main
                    git branch --set-upstream-to=origin/main main
                )
                '''
            }
        }

        stage('Detect Local Changes') {
            steps {
                echo "🔍 Checking for local changes..."
                bat 'git status && git diff --stat'
            }
        }

        stage('Run Tests') {
            steps {
                echo "🧪 Running unit tests..."
                script {
                    def result = bat(
                        script: "\"${env.PYTHON}\" -m unittest discover -s .",
                        returnStatus: true
                    )
                    if (result != 0) {
                        error("❌ Tests failed.")
                    } else {
                        echo "✅ All tests passed!"
                    }
                }
            }
        }

        stage('Commit & Push') {
            steps {
                echo "🚀 Committing and pushing..."
                script {
                    bat '''
                    git config --global user.name "Jenkins CI"
                    git config --global user.email "jenkins@example.com"

                    if not exist .gitignore (
                        echo "__pycache__/" > .gitignore
                        echo "*.pyc" >> .gitignore
                    )

                    git add .
                    git diff --cached --quiet || git commit -m "✅ Auto commit by Jenkins after successful tests"
                    '''
                }

                withCredentials([usernamePassword(credentialsId: 'github-credentials', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
                    bat '''
                    git remote set-url origin https://%GIT_USER%:%GIT_PASS%@github.com/AakashDayma01/desktop-assistance.git
                    git checkout main
                    git pull origin main --rebase
                    git push origin main
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "🎉 Build succeeded — code pushed to GitHub main branch!"
        }
        failure {
            echo "❌ Build failed — changes not pushed."
        }
    }
}
