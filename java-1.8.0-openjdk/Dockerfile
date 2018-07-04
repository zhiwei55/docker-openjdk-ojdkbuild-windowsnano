FROM microsoft/nanoserver:latest

MAINTAINER Boshi Lian <farmer1992@gmail.com>

ENV JDK_URL https://github.com/ojdkbuild/ojdkbuild/releases/download/1.8.0.171-1/java-1.8.0-openjdk-1.8.0.171-1.b10.ojdkbuild.windows.x86_64.zip
ENV JDK_VERSION 1.8.0.171-1-ojdkbuild


RUN powershell -NoProfile -Command \
        Invoke-WebRequest %JDK_URL% -OutFile jdk.zip; \
        Expand-Archive jdk.zip -DestinationPath '%ProgramFiles%'; \
        Move-Item '%ProgramFiles%\java*' '%ProgramFiles%\jdk'; \
        Remove-Item -Force jdk.zip

RUN setx /M JAVA_HOME "%ProgramFiles%\jdk"

RUN setx /M PATH "%PATH%;%ProgramFiles%\jdk\bin"
