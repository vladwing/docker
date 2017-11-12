FROM phusion/baseimage
COPY default_keys.pub /tmp/keys.pub
RUN rm -f /etc/service/sshd/down && \
	/etc/my_init.d/00_regen_ssh_host_keys.sh && \
	cat /tmp/keys.pub > /root/.ssh/authorized_keys && \
	rm -f /tmp/keys.pub

