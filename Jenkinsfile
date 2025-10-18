pipeline {
    agent any

    environment {
        // ✅ Use your confirmed Python path
        PYTHON = 'C:\\Program Files\\Python311\\python.exe'
        GIT_CREDENTIALS = 'github-credentials'   // Jenkins GitHub credentials ID
    }

    triggers {
        githubPush()  // Automatically trigger build on GitHub push
    }

    stages {
        stage('Checkout') {
            steps {
                echo '🔽 Cloning repository...'
                git branch: 'main',
                    url: 'https://github.com/AakashDayma01/desktop-assistance.git',
                    credentialsId: "${env.GIT_CREDENTIALS}"
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Installing dependencies...'
                bat """
                "${env.PYTHON}" -m pip install --upgrade pip
                "${env.PYTHON}" -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running tests...'
                bat """
                "${env.PYTHON}" -m unittest discover > result.txt
                """
            }
        }

        stage('Check Test Results') {
            steps {
                script {
                    def result = readFile('result.txt')
                    echo result
                    if (result.contains('FAILED') || result.contains('Error')) {
                        error("❌ Tests failed — build stopped, no push performed.")
                    } else {
                        echo "✅ All tests passed — code safe to push."
                    }
                }
            }
        }

        stage('Commit and Push Changes') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                echo '⬆️ Pushing verified code to GitHub...'
                bat """
                git config user.email "youremail@example.com"
                git config user.name "Aakash Dayma"
                git add .
                git commit -m "Auto-tested commit by Jenkins" || echo No changes to commit
                git push origin main
                """
            }
        }
    }

    post {
        failure {
            echo '⚠️ Build failed — changes not pushed to GitHub.'
        }
        success {
            echo '✅ Build passed — code tested and pushed successfully!'
        }
    }
}
