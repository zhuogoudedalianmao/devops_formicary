FROM python:2.7.13

# set timezone
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# set workdir & copy files
WORKDIR /opt/formicary

EXPOSE 8080
CMD ["python", "--version"]