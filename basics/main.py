print("This is a virtual environment")
course_title = "         Python for Devops               "
print(course_title.strip())

# Sets

unique_ports = set([80, 443, 22, 80, 8080, 443])
server_names = {"web01", "web02"}

print(unique_ports)

unique_ports.add(3000)

print(unique_ports)
print(server_names)

port = {
    "http": 80,
    "https": 443,
    "react": 3000,
    "backend": 8000
}

print(port.items())
print(port.keys())
print(port.values())
print("http" in port)