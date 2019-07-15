pipeline {
  agent any
  stages {
    stage('Install') {
      steps {
        sh 'npm install'
      }
    }
    stage('Testing') {
      steps {
        sh 'nmp test --coverage'
      }
    }
    stage('Building') {
      steps {
        sh 'npm build'
      }
    }
    stage('Pre Verification') {
      steps {
        sh '/usr/local/bin/python ./custom_script/website_tester.py -u "http://www.yomanyoyo.com.s3-website.us-east-2.amazonaws.com/"'
        sh '/usr/local/bin/python ./custom_script/aws_tester.py --profile default'
      }
    }
    stage('Deploy') {
      steps {
        sh 'npm deploy'
      }
    }
    stage('Post Verification') {
      steps {
        sh '/usr/local/bin/python ./custom_script/website_tester.py -u "http://www.yomanyoyo.com.s3-website.us-east-2.amazonaws.com/"'
      }
    }
  }
  environment {
    CI = 'true'
  }
}
