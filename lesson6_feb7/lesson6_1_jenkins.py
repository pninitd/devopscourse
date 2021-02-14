# jenkins start from Git directory: java -jar jenkins.war
# http://localhost:8080/

# https://github.com/Dgotlieb/Jenkins

# pipeline {
#  agent any
#  options {
#     buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '10'))
#   }
#  stages {
#   stage("test") {
#    steps {
#     script {
#      try {
#       echo 'do your stuff'
#      } catch (Exception e) {
#       echo 'Handle the exception!'
#      }
#     }
#    }
#   }
#  }
# }