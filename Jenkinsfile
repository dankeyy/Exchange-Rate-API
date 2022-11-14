
Jenkinsfile (Declarative Pipeline)

pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        // wasn't asked
        // stage('Build') {
        //     steps {
        //         sh ''
        //     }
        // }
        stage('Test'){
            steps {
                sh 'pytest'
            }
        }
        // wasn't asked
        // stage('Deploy') {
        //     steps {
        //         sh ''
        //     }
        // }
    }
}
