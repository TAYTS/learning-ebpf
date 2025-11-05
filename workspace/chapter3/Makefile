hello.bpf.o: %.o: %.c
	clang \
		-target bpf \
		-l/usr/aarch64-linux-gnu \
		-g \
		-O2 -c $< -o $@

load: hello.bpf.o
	sudo bpftool prog load hello.bpf.o /sys/fs/bpf/hello

attach:
	sudo bpftool net attach xdp pinned /sys/fs/bpf/hello dev eth0

detach:
	sudo bpftool net detach xdp dev eth0

clean: detach
	- rm -f *.bpf.o
	- rm -f /sys/fs/bpf/hello
