#!/bin/bash
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

# resolve links - $0 may be a softlink
PRG="$0"

while [ -h "$PRG" ]; do
  ls="$(ls -ld "$PRG")"
  link="$(expr "$ls" : '.*-> \(.*\)$')"
  if expr "$link" : '/.*' > /dev/null; then
    PRG="$link"
  else
    PRG="$(dirname "$PRG")"/"$link"
  fi
done

PRGDIR="$(dirname "$PRG")"
BASEDIR="$(cd "$PRGDIR"/.. >/dev/null 2>&1 && pwd)"

REPO=

cygwin=false
darwin=false
case "$(uname)" in
  CYGWIN*) cygwin=true ;;
  Darwin*)
    darwin=true
    if [ -z "$JAVA_VERSION" ] ; then
      JAVA_VERSION="CurrentJDK"
    else
      echo "Using Java version: $JAVA_VERSION"
    fi
    if [ -z "$JAVA_HOME" ]; then
      if [ -x "/usr/libexec/java_home" ]; then
        JAVA_HOME=$(/usr/libexec/java_home)
      else
        JAVA_HOME=/System/Library/Frameworks/JavaVM.framework/Versions/"${JAVA_VERSION}"/Home
      fi
    fi
    ;;
esac

if [ -z "$JAVA_HOME" ] ; then
  if [ -r /etc/gentoo-release ] ; then
    JAVA_HOME="$(java-config --jre-home)"
  fi
fi

if $cygwin ; then
  [ -n "$JAVA_HOME" ] && JAVA_HOME="$(cygpath --unix "$JAVA_HOME")"
  [ -n "$CLASSPATH" ] && CLASSPATH="$(cygpath --path --unix "$CLASSPATH")"
fi

if [ -z "$JAVACMD" ] ; then
  if [ -n "$JAVA_HOME"  ] ; then
    if [ -x "$JAVA_HOME/jre/sh/java" ] ; then
      JAVACMD="$JAVA_HOME/jre/sh/java"
    else
      JAVACMD="$JAVA_HOME/bin/java"
    fi
  else
    JAVACMD="$(which java)"
  fi
fi

if [ ! -x "$JAVACMD" ] ; then
  echo "Error: JAVA_HOME is not defined correctly." 1>&2
  echo "  We cannot execute $JAVACMD" 1>&2
  exit 1
fi

if [ -z "$REPO" ]; then
  REPO="$BASEDIR"/lib
fi

CLASSPATH="$BASEDIR"/lib/*

ENDORSED_DIR=
if [ -n "$ENDORSED_DIR" ] ; then
  CLASSPATH="$BASEDIR/$ENDORSED_DIR/*:$CLASSPATH"
fi

if [ -n "$CLASSPATH_PREFIX" ] ; then
  CLASSPATH="$CLASSPATH_PREFIX:$CLASSPATH"
fi

if [ -z "$PLUGINS_CLASSPATH" ] ; then
  if [ -z "$PLUGINS_DIR" ] ; then
    PLUGINS_DIR="$BASEDIR"/plugins
  else
    if [[ "$PLUGINS_DIR" = *,* ]]; then
      echo "\$PLUGINS_DIR should use ; as the delimiter"
      exit 1
    fi
  fi

  export IFS=';'
  for DIR in $PLUGINS_DIR; do
    if [ -d "$DIR" ] ; then
      unset IFS
      if [ -n "$PLUGINS_INCLUDE" ] ; then
        if [[ "$PLUGINS_INCLUDE" = *,* ]]; then
          echo "\$PLUGINS_INCLUDE should use ; as the delimiter"
          exit 1
        fi
        export IFS=';'
        for PLUGIN_JAR in $PLUGINS_INCLUDE; do
          PLUGIN_JAR_PATH=$(find "$DIR" -path \*/"$PLUGIN_JAR"/"$PLUGIN_JAR"-\*.jar)
          if [ -n "$PLUGINS_CLASSPATH" ] ; then
            PLUGINS_CLASSPATH="$PLUGINS_CLASSPATH:$PLUGIN_JAR_PATH"
          else
            PLUGINS_CLASSPATH="$PLUGIN_JAR_PATH"
          fi
        done
        unset IFS
      else
        PLUGIN_JARS=$(find "$DIR" -name \*.jar)
        for PLUGIN_JAR in $PLUGIN_JARS ; do
          if [ -n "$PLUGINS_CLASSPATH" ] ; then
            PLUGINS_CLASSPATH="$PLUGINS_CLASSPATH:$PLUGIN_JAR"
          else
            PLUGINS_CLASSPATH="$PLUGIN_JAR"
          fi
        done
      fi
    fi
  done
  unset IFS
fi

if [ -n "$PLUGINS_CLASSPATH" ] ; then
  CLASSPATH="$CLASSPATH:$PLUGINS_CLASSPATH"
fi

if $cygwin; then
  [ -n "$CLASSPATH" ] && CLASSPATH="$(cygpath --path --windows "$CLASSPATH")"
  [ -n "$JAVA_HOME" ] && JAVA_HOME="$(cygpath --path --windows "$JAVA_HOME")"
  [ -n "$HOME" ] && HOME="$(cygpath --path --windows "$HOME")"
  [ -n "$BASEDIR" ] && BASEDIR="$(cygpath --path --windows "$BASEDIR")"
  [ -n "$REPO" ] && REPO="$(cygpath --path --windows "$REPO")"
fi

jdk_version() {
  IFS='
'
  lines=$("$JAVACMD" -Xms32M -Xmx32M -version 2>&1 | tr '\r' '\n')
  local result=""
  for line in $lines; do
    if [ -z "$result" ] && echo "$line" | grep -q 'version "'; then
      ver=$(echo "$line" | sed -e 's/.*version "\(.*\)"\(.*\)/\1/; 1q')
      if [[ "$ver" =~ ^1\. ]]; then
        result=$(echo "$ver" | sed -e 's/1\.\([0-9]*\)\(.*\)/\1/; 1q')
      else
        result=$(echo "$ver" | sed -e 's/\([0-9]*\)\(.*\)/\1/; 1q')
      fi
    fi
  done
  unset IFS
  echo "$result"
}

if [ -z "$JAVA_OPTS" ] ; then
  ALL_JAVA_OPTS="-Xms4G -Dlog4j2.configurationFile=conf/log4j2.xml -Dpinot.admin.system.exit=true"
else
  ALL_JAVA_OPTS="$JAVA_OPTS"
fi

if [ "$(jdk_version)" -gt 11 ]; then
  ALL_JAVA_OPTS="--add-opens=java.base/java.nio=ALL-UNNAMED \
  --add-opens=java.base/sun.nio.ch=ALL-UNNAMED \
  --add-opens=java.base/java.lang=ALL-UNNAMED \
  --add-opens=java.base/java.util=ALL-UNNAMED \
  --add-opens=java.base/java.lang.reflect=ALL-UNNAMED \
  $JAVA_OPTS"
fi

if [ -z "$PLUGINS_DIR" ] ; then
  PLUGINS_DIR="$BASEDIR"/plugins
fi
ALL_JAVA_OPTS="$ALL_JAVA_OPTS -Dplugins.dir=$PLUGINS_DIR"
if [ -n "$PLUGINS_INCLUDE" ] ; then
  ALL_JAVA_OPTS="$ALL_JAVA_OPTS -Dplugins.include=$PLUGINS_INCLUDE"
fi

exec "$JAVACMD" $ALL_JAVA_OPTS \
  -classpath "$CLASSPATH" \
  -Dapp.name="pinot-admin" \
  -Dapp.pid="$$" \
  -Dapp.repo="$REPO" \
  -Dapp.home="$BASEDIR" \
  -Dbasedir="$BASEDIR" \
  org.apache.pinot.tools.admin.PinotAdministrator \
  "$@"
