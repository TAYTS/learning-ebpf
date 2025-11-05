TARGETS = hello hello-func

all: $(TARGETS)
.PHONY: all

$(TARGETS): %: %.bpf.o

%.bpf.o: %.bpf.c
	clang \
		-target bpf \
		-l/usr/aarch64-linux-gnu \
		-g \
		-O2 -c $< -o $@

load-net: hello.bpf.o
	sudo bpftool prog load hello.bpf.o /sys/fs/bpf/hello

load-func: hello-func.bpf.o
	sudo bpftool prog load hello-func.bpf.o /sys/fs/bpf/hello-func

attach-bpftool:`
	sudo bpftool net attach xdp pinned /sys/fs/bpf/hello dev eth0

detach-bpftool:
	sudo bpftool net detach xdp dev eth0

attach-ip:
	ip link set dev eth0 xdp obj hello.bpf.o sec xdp

detach-ip:
	ip link set dev eth0 xdp off

clean: detach-bpftool detach-ip
	- rm -f *.bpf.o
	- rm -f /sys/fs/bpf/hello
	- rm -f /sys/fs/bpf/hello-func