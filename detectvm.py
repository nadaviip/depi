import subprocess

def check_registry_keys():
    try:
        output = subprocess.check_output('reg query "HKEY_LOCAL_MACHINE\\HARDWARE\\DESCRIPTION\\System" /v SystemBiosVersion', shell=True).decode().strip()
        if any(vendor in output for vendor in ["VMware", "VirtualBox", "QEMU", "KVM", "Hyper-V", "VBOX"]):
            return True
    except Exception as e:
        pass
    return False


if __name__ == "__main__":
    if check_registry_keys():
        print("This is a virtual machine.")
    else:
        print("This is not a virtual machine.")
        
# Check common virtualization hardware strings
import subprocess


virtual_hardware = ["VirtualBox", "VMware", "QEMU", "KVM", "Microsoft Hyper-V"]
output = subprocess.check_output('reg query "HKEY_LOCAL_MACHINE\\HARDWARE\\DESCRIPTION\\System" /v SystemBiosVersion', shell=True).decode().strip()
print(output)
