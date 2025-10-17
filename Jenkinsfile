// ✅ Trigger pipeline on GitHub push
properties([
    pipelineTriggers([
        githubPush()
    ])
])

pipeline {
    agent any

    environment {
        LOG_FILE = 'jenkins_build_log.txt'
        PYTHON_CMD = 'python' // Update if python path is different on your agent
    }

    stages {

        stage('Install Dependencies') {
            steps {
                echo "📦 Installing Python dependencies..."
                // Use Windows batch commands
                bat """
                %PYTHON_CMD% -m pip install --upgrade pip
                if exist requirements.txt (
                    %PYTHON_CMD% -m pip install -r requirements.txt
                )
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo "🧪 Running unit tests..."
                script {
                    try {
                        // Run all test files matching test_*.py and save output to a file
                        bat """
                        %PYTHON_CMD% -m unittest discover -s . -p "test_*.py" > test_output.txt 2>&1
                        if errorlevel 1 exit /b 1
                        """

                        // Print test output to Jenkins console
                        bat 'type test_output.txt'

                        echo "✅ All tests passed."
                    } catch (err) {
                        echo "❌ Tests failed! Saving logs..."
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
            bat """
            echo Build failed at %date% %time% >> %LOG_FILE%
            """
            archiveArtifacts artifacts: "%LOG_FILE%", onlyIfSuccessful: false
        }
    }
}
