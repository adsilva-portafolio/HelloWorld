pipeline {
    agent any

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
                echo 'Ejecutando analisis estatico con SonarQube...'
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner -Dsonar.projectKey=HelloWorld -Dsonar.sources=.'
                }
            }
        }

        stage('Security Test (Dependency-Check)') {
            steps {
                echo 'Ejecutando analisis de dependencias...'
                dependencyCheck odcInstallation: 'Dependency-Check-12'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando aplicacion en entorno de prueba...'
            }
        }
    }
}
