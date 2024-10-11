def hex_to_ip_and_port(hex_string_data):
    parts = hex_string_data.split('3B')
    ip_hex = parts[0]
    port_hex = parts[1]
    ip_data = ''.join(chr(int(ip_hex[i:i+2], 16)) for i in range(0, len(ip_hex), 2))
    port_data = int(port_hex, 16)
    return ip_data, port_data


# Example
if __name__ == "__main__":
    hex_string = "3132302E39322E38392E3132323B23823B"
    ip, port = hex_to_ip_and_port(hex_string)
    print(f"IP: {ip}, Porta: {port}")
