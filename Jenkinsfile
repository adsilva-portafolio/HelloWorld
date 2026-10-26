pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Compilando el código fuente...'
                // Aquí iría el comando de compilación real según tu lenguaje
            }
        }
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                sh 'python3 test_app.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Desplegando la aplicación en el entorno de prueba...'
            }
        }
    }
}
