pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Program Files\\Python311\\python.exe"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                echo "🔽 Cloning repository..."
                checkout scm
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
                echo "📦 Skipping dependencies installation (no requirements.txt)"
            }
        }

        stage('Run Main Script') {
            steps {
                echo "▶️ Running desktop_assis.py..."
                bat "\"${env.PYTHON_PATH}\" desctop_assis.py"
            }
        }

        stage('Run Tests') {
            steps {
                echo "🧪 Running test_voice_assistant.py..."
                bat "\"${env.PYTHON_PATH}\" -m unittest test_voice_assistant.py"
            }
        }
    }

    post {
        success {
            echo "✅ Build completed successfully!"
        }
        failure {
            echo "⚠️ Build failed — please check the logs."
        }
    }
}
