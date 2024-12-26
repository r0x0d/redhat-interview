FROM fedora:42 as base

ENV PYTHON python3
ENV PIP pip3
ENV REQUIREMENTS_FILE "requirements.tests.txt"

FROM base as system_dependencies

RUN dnf update --refresh -y \
    && dnf install -y python3-dnf python3 python3-pip make \
    && dnf clean all

FROM system_dependencies as pip_dependencies

COPY $REQUIREMENTS_FILE /tmp
RUN $PIP install -r tmp/$REQUIREMENTS_FILE

FROM pip_dependencies as final

WORKDIR /redhat_interview

RUN groupadd --gid=1000 -r guest \
    && useradd -r --uid=1000 --gid=1000 guest \
    && chown -R guest:guest .

COPY --chown=guest:guest . .
USER guest:guest