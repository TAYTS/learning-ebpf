VAGRANTFILE_API_VERSION = "2"

$bootstrap=<<SCRIPT
dnf install make glibc-devel elfutils-libelf-devel wget tar vim tmux jq systemtap-sdt-devel clang bcc strace kernel-devel git bcc libbpf-devel gcc-aarch64-linux-gnu gcc-c++-aarch64-linux-gnu -y
export PATH=$PATH:/usr/aarch64-linux-gnu/bin
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
	ipv4 = "10.0.0.10"
	config.vm.define "learnbpf" do |fedora|
		fedora.vm.box = "roboxes/fedora39"
		net_index = 1
		fedora.vm.hostname = "learnbpf"
		fedora.vm.provider "virtualbox" do |vb|
			vb.customize ["modifyvm", :id, "--memory", "1024"]
		end
		fedora.vm.provider "libvirt" do |lv|
			lv.memory = 1024
		end
        fedora.vm.provider "qemu" do |qe|
            qe.memory = 1024
        end

		fedora.vm.network :private_network, ip: "#{ipv4}"
		fedora.vm.provision :shell, inline: $bootstrap, :args => "#{ipv4}"
        fedora.vm.synced_folder "./workspace", "/vagrant"
	end
end
