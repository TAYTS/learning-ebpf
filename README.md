# Learning eBPF

Book reference: [Learning eBPF](https://www.oreilly.com/library/view/learning-ebpf/9781098135119/)

# Local Setup (For Mac Apple Silicon Only)

1. Install Vagrant
    ```bash
    brew install qemu
    brew install --cask vagrant
    vagrant plugin install vagrant-qemu
    ```

2. Start Vagrant
    ```bash
    # For apple silicon
    vagrant up --provider=qemu
    ```

3. Access virtual machine
    ```bash
    vagrant ssh
    ```

4. File permission setup

    > System Settings > File Sharing > Enable Windows File Sharing for your Mac user account.

    This is to bind the local directory to virtual machine created by Vagrant