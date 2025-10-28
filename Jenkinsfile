pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    environment {
        WORKSPACE_DIR = "C:\\Temp\\jenkins_sync"
        GIT_REPO_URL = 'https://github.com/AakashDayma01/desktop-assistance.git'
        GIT_BRANCH = 'main'
        GIT_CREDENTIALS_ID = 'github-credentials'
        PYTHON = "C:\\Program Files\\Python311\\python.exe"
    }

    stages {

        stage('Use Local Synced Code') {
            steps {
                dir("${env.WORKSPACE_DIR}") {
                    echo "💻 Using code from synced local folder: ${env.WORKSPACE_DIR}"
                    bat 'dir'
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
                            error("❌ Tests failed! Build stopped.")
                        } else {
                            echo "✅ All tests passed successfully!"
                        }
                    }
                }
            }
        }

        stage('Commit & Push to GitHub') {
            steps {
                dir("${env.WORKSPACE_DIR}") {
                    echo "🚀 Committing and pushing updated code to GitHub..."
                    script {
                        // ✅ Allow Jenkins SYSTEM user to access this repo folder
                        bat 'git config --global --add safe.directory C:/Temp/jenkins_sync'

                        // ✅ Initialize repository safely
                        bat '''
                            git init
                            git config user.name "Jenkins CI"
                            git config user.email "jenkins@example.com"
                            git remote remove origin || echo No remote
                            git remote add origin https://github.com/AakashDayma01/desktop-assistance.git
                            git add .
                            git commit -m "✅ Auto commit by Jenkins after successful tests" || echo "Nothing to commit"
                        '''

                        // ✅ Push changes using stored credentials
                        withCredentials([usernamePassword(credentialsId: "${GIT_CREDENTIALS_ID}", usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
                            bat """
                                git remote set-url origin https://%GIT_USER%:%GIT_PASS%@github.com/AakashDayma01/desktop-assistance.git
                                git pull --rebase origin ${GIT_BRANCH} || echo "⚠️ Pull failed, continuing..."
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
    }
}
