pipeline {
    agent any

    environment {
        WORKSPACE_DIR = "C:\\Temp\\jenkins_sync"                     // 🧩 Folder synced by watcher.py
        GIT_REPO_URL = 'https://github.com/AakashDayma01/desktop-assistance.git'
        GIT_BRANCH = 'main'
        GIT_CREDENTIALS_ID = 'github-credentials'                    // Must exist in Jenkins credentials
        PYTHON = "C:\\Program Files\\Python311\\python.exe"
    }

    stages {

        stage('Use Local Synced Code') {
            steps {
                dir("${env.WORKSPACE_DIR}") {
                    echo "💻 Using code from synced local folder: ${env.WORKSPACE_DIR}"
                    bat 'dir'  // ✅ Show files to confirm sync works
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir("${env.WORKSPACE_DIR}") {
                    echo "🧪 Running tests on synced local code..."
                    script {
                        def result = bat(
                            script: "\"${env.PYTHON}\" -m unittest discover -s .",
                            returnStatus: true
                        )
                        if (result != 0) {
                            error("❌ Tests failed! Stopping pipeline.")
                        } else {
                            echo "✅ All tests passed successfully!"
                        }
                    }
                }
            }
        }

        stage('Commit & Push to GitHub') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                dir("${env.WORKSPACE_DIR}") {
                    echo "🚀 Committing and pushing updated code to GitHub..."
                    script {
                        bat '''
                            git config --global user.name "Jenkins CI"
                            git config --global user.email "jenkins@example.com"
                            git init
                            git remote remove origin || echo No remote
                            git remote add origin https://github.com/AakashDayma01/desktop-assistance.git
                            git add .
                            git diff --cached --quiet || git commit -m "✅ Auto commit by Jenkins after successful tests"
                        '''

                        withCredentials([usernamePassword(credentialsId: "${GIT_CREDENTIALS_ID}", usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
                            bat """
                                git remote set-url origin https://%GIT_USER%:%GIT_PASS%@github.com/AakashDayma01/desktop-assistance.git
                                echo "📦 Pulling latest ${GIT_BRANCH} before pushing..."
                                git pull --rebase origin ${GIT_BRANCH} || echo "⚠️ Pull failed, continuing..."
                                echo "📤 Pushing updates to GitHub..."
                                git push origin HEAD:${GIT_BRANCH}
                            """
                        }
                    }
                }
            }
        }
    }

    post {
        success {
            echo "🎉 Build succeeded — local synced code tested and pushed to GitHub!"
        }
        failure {
            echo "🚨 Build failed — code not pushed to GitHub."
        }
        always {
            echo "📝 Build complete. Review console output for details."
        }
    }
}
