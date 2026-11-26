
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Compilando el codigo fuente y preparando dependencias...'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                sh 'python3 test_app.py'
            }
        }

        stage('Generate Documentation') {
            steps {
                echo 'Generando documentacion automatizada con Doxygen...'
                sh 'doxygen Doxyfile'
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
                echo 'Ejecutando analisis de dependencias...'
                dependencyCheck odcInstallation: 'Dependency-Check-12', additionalArguments: '--noupdate --format XML --format HTML'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }

        stage('Version Control') {
            steps {
                echo 'Verificando trazabilidad y estado del repositorio Git...'
                sh 'git status'
                sh 'git log -n 3 --oneline'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando aplicacion en entorno de pruebas...'
                sh 'echo "Despliegue simulado exitoso en http://localhost:5000"'
            }
        }
    }

    post {
        always {
            echo 'Finalizacion del pipeline de documentacion y trazabilidad.'
        }
        success {
            echo 'Pipeline completado con exito.'
        }
        failure {
            echo 'El pipeline ha fallado. Revise los registros de consola en Jenkins.'
        }
    }
}
