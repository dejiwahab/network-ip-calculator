from calculator import calculate_network

print("=== Network IP Calculator ===")

ip = input("Enter an IP address (e.g. 192.168.1.10/24): ")

try:
    result = calculate_network(ip)

    print("\nResults")
    print("----------------------------")
    print("Network Address :", result["network"])
    print("Broadcast Address:", result["broadcast"])
    print("Subnet Mask     :", result["mask"])
    print("First Host      :", result["first_host"])
    print("Last Host       :", result["last_host"])
    print("Total Addresses :", result["total"])

except ValueError:
    print("Invalid IP address. Please try again.")