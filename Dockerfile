FROM python:3.8

# update debian
RUN apt-get -y update

# install dependencies
RUN pip install jupyterlab creme chantilly

# Add custom flavors.py for showing prediction and
# ground truth value in chantilly dashboard
ADD flavors.py /usr/local/lib/python3.8/site-packages/chantilly/flavors.py

# Add starting script
Add start.sh /

# Make executable
RUN chmod +x /start.sh

# working dir
WORKDIR /work

# expose ports
EXPOSE 8888
EXPOSE 5000

# launch jupyter lab + chantilly
CMD ["/start.sh"]
