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
                script {
                    def scannerHome = tool 'SonarQubeScanner'
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=HelloWorld -Dsonar.sources=."
                    }
                }
            }
        }

        stage('Security Test (Dependency-Check)') {
            steps {
                echo 'Ejecutando analisis de dependencias (OWASP Dependency-Check v12.x.x)...'
                // Se usa --noupdate para evitar la descarga masiva de la API NVD que congela la maquina virtual
                dependencyCheck odcInstallation: 'Dependency-Check-12', additionalArguments: '--noupdate --format XML --format HTML'
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
