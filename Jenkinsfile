pipeline { 
    agent any 
    
    tools { 
        dependencyCheck 'Dependency-Check-12' 
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
                sh 'python3 test\_app.py' 
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
        
        stage('Security Test (Dependency-Check &amp; ZAP)') {
            steps {
                echo 'Ejecutando analisis de dependencias OWASP Dependency-Check...' 
                dependencyCheck update: true, generateReport: true 
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml' 
                
                echo 'Ejecutando analisis dinamico con OWASP ZAP...' 
                sh 'docker run --net=host -t owasp/zap2docker-stable zap-baseline.py -t http://localhost:5000/hello?name=TEST -r zap_report.html || true' 
            } 
        } 
        
        stage('Deploy') {
            steps {
                echo 'Desplegando aplicacion en entorno de prueba...' 
            } 
        } 
    } 
} 
