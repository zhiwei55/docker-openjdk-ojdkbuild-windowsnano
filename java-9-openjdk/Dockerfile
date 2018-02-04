FROM microsoft/nanoserver:latest

MAINTAINER Boshi Lian <farmer1992@gmail.com>

ENV JDK_URL 9.0.4-1-ojdkbuild
ENV JDK_VERSION https://github.com/ojdkbuild/ojdkbuild/releases/download/9.0.4-1/java-9-openjdk-9.0.4-1.b11.ojdkbuild.windows.x86_64.zip


RUN powershell -NoProfile -Command \
        Invoke-WebRequest %JDK_URL% -OutFile jdk.zip; \
        Expand-Archive jdk.zip -DestinationPath '%ProgramFiles%'; \
        Move-Item '%ProgramFiles%\java*' '%ProgramFiles%\jdk'; \
        Remove-Item -Force jdk.zip

RUN setx /M JAVA_HOME "%ProgramFiles%\jdk\jre"

RUN setx /M PATH "%PATH%;%ProgramFiles%\jdk\bin"
