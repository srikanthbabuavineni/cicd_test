pipeline {
  agent any
  stages {
    stage('Install') {
      steps {
        sh 'yarn install'
      }
    }
    stage('Testing') {
      steps {
        sh 'yarn test --coverage'
      }
    }
    stage('Building') {
      steps {
        sh 'yarn build'
      }
    }
    stage('Pre Verification') {
      steps {
        sh '/usr/local/bin/python /usr/local/share/website_tester.py -u "http://www.yomanyoyo.com.s3-website.us-east-2.amazonaws.com/"'
      }
    }
    stage('Deploy') {
      steps {
        sh 'yarn deploy'
      }
    }
    stage('Post Verification') {
      steps {
        sh '/usr/local/bin/python /usr/local/share/website_tester.py -u "http://www.yomanyoyo.com.s3-website.us-east-2.amazonaws.com/"'
      }
    }
  }
  environment {
    CI = 'true'
  }
}
