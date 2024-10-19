import xbee
import time
import sys

xbee_device = xbee.XBee()
simulate = 1
def get_identifier():
    # Check if the device is a coordinator
    return xbee.atcmd("NI")

def is_coordinator():
    # Check if the device is a coordinator
    return xbee.atcmd("CE") == 1


def get_network_id():
    # Get the current network ID
    id_hex = xbee.atcmd("ID")
    # print(len(id_hex))
    # print("ID:")
    id_dec = int.from_bytes(id_hex, 'big')
    # print(id_dec)
    return id_dec


def set_network_id(new_id):
    # Set the network ID
    xbee.atcmd("ID", new_id)
    xbee.atcmd("WR")  # Write changes to non-volatile memory

def set_unit_id(new_id):
    # Set the network ID
    xbee.atcmd("NI", new_id)
    xbee.atcmd("WR")  # Write changes to non-volatile memory


def get_internal_baudrate():
    # Get the internal UART baudrate from the XBee register
    baudrate_code = xbee.atcmd("BD")
    baudrate_map = {
        0: 1200,
        1: 2400,
        2: 4800,
        3: 9600,
        4: 19200,
        5: 38400,
        6: 57600,
        7: 115200
    }
    return baudrate_map.get(baudrate_code, 9600)  # Default to 9600 if code is not in map


def set_uart_baudrate(new_baudrate):
    # This function is now redundant since we're not using UART.
    pass


def set_coordinator_mode(is_coordinator):
    # Set the device as coordinator or router
    xbee.atcmd("CE", 1 if is_coordinator else 0)
    xbee.atcmd("WR")  # Write changes to non-volatile memory


def read_with_timeout(timeout_ms=100):
    start_time = time.ticks_ms()  # Get the current time in milliseconds
    accumulated_data = bytearray()

    while True:
        # Read available data
        data = sys.stdin.buffer.read()

        if data:
            accumulated_data.extend(data)
            start_time = time.ticks_ms()  # Reset the timeout timer with new data

        # Check if the timeout has expired
        current_time = time.ticks_ms()
        elapsed_time = time.ticks_diff(current_time, start_time)
        if elapsed_time > timeout_ms:
            break

        # Sleep briefly to avoid busy-waiting
        time.sleep(0.01)

    return accumulated_data.decode('utf-8')


def process_command(data):
    buffer = data
    if buffer.startswith("####UID="):
        try:
            new_id = buffer[8:]
            set_unit_id(new_id)
            print("UNIT ID set to {}".format(new_id))
        except ValueError:
            print("Invalid ID format")
        return False
    elif buffer.startswith("####ID="):
        try:
            new_id = int(buffer[7:])
            set_network_id(new_id)
            print("Network ID set to {}".format(new_id))
        except ValueError:
            print("Invalid ID format")
        return False
    elif buffer.startswith("####BAUD="):
        try:
            new_baudrate = int(buffer[9:])
            set_uart_baudrate(new_baudrate)
            print("UART baud rate set to {}".format(new_baudrate))
        except ValueError:
            print("Invalid baud rate format")
        return False
    elif buffer.startswith("####MODE="):
        mode = buffer[9:]
        if mode == "COORD":
            set_coordinator_mode(True)
            print("Mode set to Coordinator")
        elif mode == "ROUTER":
            set_coordinator_mode(False)
            print("Mode set to Router")
        else:
            print("Invalid mode")
        return False
    else:
        return True


def main():
    time.sleep(2)
    coordinator = is_coordinator()
    network_id = get_network_id()
    identifier = get_identifier()
    internal_baudrate = get_internal_baudrate()

    print("Coordinator: {}".format(coordinator))
    print("Network ID: {}".format(network_id))
    print("Identifier: {}".format(identifier))
    print("Internal Baudrate: {}".format(internal_baudrate))

    if coordinator:
        last_sequence_numbers = {}  # Dictionary to store last sequence number for each sender
        is_send_payload = False
        while True:
            try:
                data = xbee.receive()
                if data:
                    payload = data['payload'].decode()
                    print("{}".format(payload))
                    # Extract the sequence number and sender identifier from the payload
                    seq_num_str = payload.split(',')[0][1:]  # Assuming sequence number is in "#{:03}," format
                    sequence_number = int(seq_num_str)
                    sender_identifier = data['sender_eui64'].decode('utf-8')  # Use sender's EUI-64 address as the identifier
                    # print("sender_eui64:{}".format(sender_identifier))
                    is_send_payload = True
                    if sender_identifier not in last_sequence_numbers:
                        # First message from this sender
                        last_sequence_numbers[sender_identifier] = sequence_number
                        # print("First message from sender {}. Processed: {}".format(sender_identifier, payload))
                    elif sequence_number > last_sequence_numbers[sender_identifier]:
                        # New sequence number is higher
                        # print("Processed: {}".format(payload))
                        last_sequence_numbers[sender_identifier] = sequence_number
                    elif sequence_number < last_sequence_numbers[sender_identifier]:
                        # Sequence number wraparound
                        # print("Sequence number wrapped around for sender {}. Processed: {}".format(sender_identifier, payload))
                        last_sequence_numbers[sender_identifier] = sequence_number
                    else:
                        is_send_payload = False
                        # print("Duplicate or out-of-order message discarded from sender {}: {}".format(sender_identifier, payload))

                    if is_send_payload:
                        # Strip the sequence number from the payload
                        # The sequence number is assumed to be in the format "#{:03},"
                        stripped_payload = payload.split(',', 1)[1]  # Remove the sequence number
                        print(stripped_payload)  # Print the payload without the sequence number

            except Exception as e:
                print("Error receiving data:", e)

            time.sleep_ms(1)
    else:
        status = xbee.atcmd('AI')
        print("status {}".format(status))

        buffer_size = 10
        data_queue = []
        sequence_number = 0  # Initialize sequence number

        while True:
            # data = sys.stdin.readline()
            data = read_with_timeout()

            if len(data) > 4:
                # status = xbee.atcmd('AI')
                # print("status {}".format(status))
                print("read: {}".format(data))
                if process_command(data):
                    formatted_data = "#{:03},".format(sequence_number)
                    formatted_data += "*{:02}".format(int(network_id))
                    formatted_data += ",{:0>4}".format(identifier)
                    formatted_data += "@{}$".format(data)

                    if len(data_queue) >= buffer_size:
                        # Queue is full, remove the oldest item
                        data_queue.pop(0)

                    # Add new data to the queue
                    data_queue.append(formatted_data)

                    sequence_number = (sequence_number + 1) % 1000  # Increment and wrap sequence number

            while data_queue:
                try:
                    next_data = data_queue.pop(0)  # Get and remove the oldest item
                    xbee.transmit(xbee.ADDR_BROADCAST, next_data)
                except Exception as e:
                    print("Error sending data:", e)
                    if "message too long" not in str(e):
                        time.sleep(2)
                        data_queue.insert(0, next_data)
                    else:
                        print("Message too long, skipping retry.")


main()