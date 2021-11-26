import struct

# ��������� �� ������� ���� (data) ����� ������ (opcode, file_name � �.�.)
def get_package(data):
	package = {}
	package["opcode"] = int.from_bytes(bytes = data[:2], byteorder = "big")
	match package["opcode"]:
		case 1|2:
			package["file_name"] = data[2:-1].split(b'\x00')[0].decode()
		case 3:
			package["current_block"] = int.from_bytes(bytes = data[2:4], byteorder = "big")
			package["data"] = data[4:]
		case 4:
			package["current_block"] = int.from_bytes(bytes = data[2:], byteorder = "big")
		case 5:
			package["err_code"] = int.from_bytes(bytes = data[2:4], byteorder = "big")
			package["err_message"] = data[4:-1].decode()
	return package

# �������� ������ � ��������
def create_request_package(direction_value, filename):
	package = struct.pack(">h", direction_value)
	package += filename.encode()
	package += struct.pack(">c", b'\x00')
	package += "octet".encode()
	package += struct.pack(">c", b'\x00')
	return package

# �������� ������ � �������
def create_data_package(current_block, data):
	package = struct.pack(">h", 3)
	package += struct.pack(">h", current_block)
	package += data
	return package

# �������� ������ �������������
def create_ack_package(current_block):
	package = struct.pack(">h", 4)
	package += struct.pack(">h", current_block)
	return package

# �������� ������ � ����������� �� ������
def create_err_package(err_code, err_message):
	package = struct.pack(">h", 5)
	package += struct.pack(">h", err_code)
	package += err_message.encode()
	package += struct.pack(">c", b'\x00')
	return package