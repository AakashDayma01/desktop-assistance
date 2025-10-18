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

        stage('Run Script') {
            steps {
                echo "▶️ Running main Python script..."
                // Replace main.py with your entry-point file
                bat "\"${env.PYTHON_PATH}\" main.py"
            }
        }
    }

    post {
        success {
            echo "✅ Build and script execution completed successfully!"
        }
        failure {
            echo "⚠️ Build failed — please check the logs."
        }
    }
}
