#!/usr/bin/env bash

astyle --recursive "$PWD/*.c"\
    --style=java \
    --indent=spaces=4 \
    --indent-switches \
    --indent-col1-comments \
    --break-blocks \
    --pad-oper \
    --pad-comma \
    --errors-to-stdout \
    --quiet \
    >/dev/null 2>&1

astyle --recursive "$PWD/*.h"\
    --style=java \
    --indent=spaces=4 \
    --indent-switches \
    --indent-col1-comments \
    --break-blocks \
    --pad-oper \
    --pad-comma \
    --errors-to-stdout \
    --quiet \
    >/dev/null 2>&1

astyle --recursive "$PWD/*.cpp"\
    --style=java \
    --indent=spaces=4 \
    --indent-switches \
    --indent-col1-comments \
    --break-blocks \
    --pad-oper \
    --pad-comma \
    --errors-to-stdout \
    --quiet \
    >/dev/null 2>&1

astyle --recursive "$PWD/*.hpp"\
    --style=java \
    --indent=spaces=4 \
    --indent-switches \
    --indent-col1-comments \
    --break-blocks \
    --pad-oper \
    --pad-comma \
    --errors-to-stdout \
    --quiet \
    >/dev/null 2>&1

astyle --recursive "$PWD/*.java"\
    --style=java \
    --indent=spaces=4 \
    --indent-switches \
    --indent-col1-comments \
    --break-blocks \
    --pad-oper \
    --pad-comma \
    --errors-to-stdout \
    --quiet \
    >/dev/null 2>&1
    
find . -name "*.py" -exec black '{}' \; >/dev/null 2>&1;
find . -name "*.py" -exec reindent '{}' \; >/dev/null 2>&1;
find . -name "*.js" -exec js-beautify '{}' \; >/dev/null 2>&1
find . -name "*.html" -exec js-beautify '{}' \; >/dev/null 2>&1
find . -name "*.css" -exec js-beautify '{}' \; >/dev/null 2>&1

find . -name "*.orig" -delete
