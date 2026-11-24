pipeline {
    agent any

    tools {
        'dependency-check': 'Dependency-Check-12'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Compilando y preparando el entorno...'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                sh 'python3 test_app.py'
            }
        }

        stage('Analyze (SonarQube)') {
            steps {
                echo 'Ejecutando análisis estático con SonarQube...'
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner -Dsonar.projectKey=HelloWorld -Dsonar.sources=.'
                }
            }
        }

        stage('Security Test (Dependency-Check)') {
            steps {
                echo 'Ejecutando análisis de dependencias...'
                dependencyCheck odcInstallation: 'Dependency-Check-12'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando aplicación en entorno de prueba...'
            }
        }
    }
}
