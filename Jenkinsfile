// Trigger pipeline on GitHub push
properties([
    pipelineTriggers([
        githubPush()
    ])
])

pipeline {
    agent any

    environment {
        LOG_FILE = 'jenkins_build_log.txt'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                echo "📦 Installing Python dependencies..."
                bat '''
                python -m pip install --upgrade pip
                if exist requirements.txt (
                    pip install -r requirements.txt
                )
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "🧪 Running unit tests..."
                script {
                    try {
                        // Run all test files matching test_*.py and save output to a file
                        bat 'python -m unittest discover -s . -p "test_*.py" > test_output.txt 2>&1'

                        // Print test output to Jenkins console for easier debugging
                        bat 'type test_output.txt'

                        echo "✅ All tests passed."
                    } catch (err) {
                        echo "❌ Tests failed! Saving logs..."
                        // Save failure info and test output to log file
                        bat """
                        echo Build failed on %date% %time% > %LOG_FILE%
                        echo ---- TEST OUTPUT ---- >> %LOG_FILE%
                        type test_output.txt >> %LOG_FILE%
                        """
                        error("Stopping pipeline due to test failure.")
                    }
                }
            }
        }
    }

    post {
        success {
            echo '🎉 Build succeeded!'
        }
        failure {
            echo '⚠️ Build failed. Check log for details.'
            // Append failure timestamp to log file (Windows environment variable)
            bat """
            echo Build failed at %date% %time% >> %LOG_FILE%
            """
            // Archive the log file even if the build failed
            archiveArtifacts artifacts: "%LOG_FILE%", onlyIfSuccessful: false
        }
    }
}
