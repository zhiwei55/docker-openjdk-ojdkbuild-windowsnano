# OpenJDK Docker image for Windows
![Docker build](https://farmer1992.visualstudio.com/_apis/public/build/definitions/3686302e-40e0-495b-a6f8-f2926767661b/10/badge)

This docker image build using binaries from <https://github.com/ojdkbuild/ojdkbuild>.


## Quick Start

Java 9

```
docker run --rm -ti farmer1992/openjdk-ojdkbuild-windowsnano java -version
```

Java 8

```
docker run --rm -ti farmer1992/openjdk-ojdkbuild-windowsnano:8 java -version
```
