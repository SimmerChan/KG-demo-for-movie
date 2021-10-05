@REM Licensed to the Apache Software Foundation (ASF) under one
@REM or more contributor license agreements.  See the NOTICE file
@REM distributed with this work for additional information
@REM regarding copyright ownership.  The ASF licenses this file
@REM to you under the Apache License, Version 2.0 (the
@REM "License"); you may not use this file except in compliance
@REM with the License.  You may obtain a copy of the License at
@REM
@REM     http://www.apache.org/licenses/LICENSE-2.0
@REM
@REM Unless required by applicable law or agreed to in writing, software
@REM distributed under the License is distributed on an "AS IS" BASIS,
@REM WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@REM See the License for the specific language governing permissions and
@REM limitations under the License.

@echo off
@REM modify this to name the server jar
java -Xmx1200M -jar fuseki-server.jar %*

@REM Adding custom code to the Fuseki server:
@REM  
@REM It is also possible to launch Fuseki using 
@REM   java ..jvmarsg... -cp $JAR org.apache.jena.fuseki.cmd.FusekiCmd %*
@REM 
@REM In this way, you can add custom java to the classpath:
@REM 
@REM  java ... -cp fuseki-server.jar;MyCustomCode.jar org.apache.jena.fuseki.cmd.FusekiCmd %*
