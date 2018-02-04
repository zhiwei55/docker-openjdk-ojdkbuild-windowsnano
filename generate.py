#!/bin/usr/env python

import requests
import itertools

T='''FROM microsoft/nanoserver:latest

MAINTAINER Boshi Lian <farmer1992@gmail.com>

ENV JDK_URL %s
ENV JDK_VERSION %s

''' 

STATIC=r'''
RUN powershell -NoProfile -Command \
        Invoke-WebRequest %JDK_URL% -OutFile jdk.zip; \
        Expand-Archive jdk.zip -DestinationPath '%ProgramFiles%'; \
        Move-Item '%ProgramFiles%\java*' '%ProgramFiles%\jdk'; \
        Remove-Item -Force jdk.zip

RUN setx /M JAVA_HOME "%ProgramFiles%\jdk\jre"

RUN setx /M PATH "%PATH%;%ProgramFiles%\jdk\bin"
'''

def pull_release():
    r = requests.get('https://api.github.com/repos/ojdkbuild/ojdkbuild/releases')

    keyf = lambda x: '-'.join((x['name'].split('-')[:2]))

    releases = filter(lambda x: not x['prerelease'], r.json())
    releases.sort(key=keyf)

    for k, g in itertools.groupby(releases, keyf):
        g = list(g)
        g.sort(key=lambda r: r['id'], reverse=True)
        
        latest = g[0]

        url = filter(lambda u: u.endswith('windows.x86_64.zip') , [a['browser_download_url'] for a in latest['assets']])[0]

        ver = url.split('/')[7] + '-ojdkbuild'

        yield k + '-openjdk', ver, url


for d,v,u in pull_release():
    f = open(d + '/Dockerfile', 'w')
    with(f):
        f.write(T % (v,u))
        f.write(STATIC)
