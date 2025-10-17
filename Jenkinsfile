pipeline {
    agent any

    environment {
        GIT_CREDENTIALS = 'github-credentials'
        GIT_REPO = 'https://github.com/AakashDayma01/desktop-assistance.git'
        BRANCH = 'main'
        LOG_FILE = 'jenkins_build_log.txt'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "🔽 Cloning repository..."
                git branch: "${BRANCH}", credentialsId: "${GIT_CREDENTIALS}", url: "${GIT_REPO}"
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "📦 Installing Python dependencies..."
                bat '''
                if exist requirements.txt (
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                ) else (
                    echo No requirements.txt found, skipping install.
                )
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "🧪 Running test_voice_assistant.py..."
                script {
                    try {
                        bat 'python test_voice_assistant.py > test_output.txt 2>&1'
                        echo "✅ All tests passed."
                    } catch (err) {
                        echo "❌ Tests failed! Saving logs..."
                        bat """
                        echo Build failed on %date% %time% > ${LOG_FILE}
                        echo ---- TEST OUTPUT ---- >> ${LOG_FILE}
                        type test_output.txt >> ${LOG_FILE}
                        """
                        error("Stopping pipeline due to test failure.")
                    }
                }
            }
        }

        stage('Commit and Push Changes') {
            steps {
                echo "📤 Pushing updates to GitHub..."
                bat '''
                git config user.name "Jenkins CI"
                git config user.email "jenkins@example.com"
                git add .
                git commit -m "✅ Auto update from Jenkins on %date% %time%" || echo No changes to commit
                git pull --rebase origin %BRANCH%
                git push origin %BRANCH%
                '''
            }
        }
    }

    post {
        success {
            echo '🎉 Build succeeded and changes pushed to GitHub!'
        }
        failure {
            echo '⚠️ Build failed. Check log for details.'
            bat 'echo Build failed at %date% %time% >> ${LOG_FILE}'
            archiveArtifacts artifacts: "${LOG_FILE}", onlyIfSuccessful: false
        }
    }
}
