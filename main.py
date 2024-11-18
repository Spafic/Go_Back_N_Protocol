import random

def protocol5(window_size, number_of_frames, message):
    message_after_received = ""
    failed_frames = 0  # To count the number of frames that fail to send
    total_sent_frames = 0  # Total frames sent, including retransmissions
    last_successful_frame = 0  # Tracks the last successfully sent frame

    # Send the first set of frames in the window
    for j in range(1, min(window_size + 1, number_of_frames + 1)):
        print(f"Sending Frame {j}: Data: {message[j-1]}, Binary Representation: {convert_to_binary(message[j-1])}")
        total_sent_frames += 1

    i = 1
    while i <= number_of_frames:
        for j in range(i, min(i + window_size, number_of_frames + 1)):
            random_result = random.randint(0, 1)  # Simulate frame sending success or failure
            if random_result:
                # Frame sent successfully
                print(f"Frame {j} sent successfully")
                message_after_received +=convert_to_binary( message[j-1] )
                last_successful_frame = j
                if j + window_size <= number_of_frames:
                    print(f"Sending Frame {j + window_size}: Data: {message[j + window_size - 1]}, Binary Representation: {convert_to_binary(message[j + window_size - 1])}")
                    total_sent_frames += 1
            else:
                # Frame failed, all frames in the current window are resent
                failed_frames += 1
                print(f"Frame {j} execution timeout")
                for k in range(j, min(j + window_size, number_of_frames + 1)):
                    print(f"Resending Frame {k}: Data: {message[k-1]}, Binary Representation: {convert_to_binary(message[k-1])}")
                    total_sent_frames += 1
                break  # Exit to resend the current window
        i = last_successful_frame + 1  # Update i to the next frame to send

    # Calculate wire efficiency
    wire_efficiency = ((total_sent_frames - failed_frames) / total_sent_frames) * 100

    # Print the statistics after completion
    print("\nTransmission complete!")
    print(f"Received Message : {message_after_received}")
    n = int(message_after_received, 2)
    print( "Received Message after convert : "+n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())

    print(f"Total frames sent (including retransmissions): {total_sent_frames}")
    print(f"Number of failed frames: {failed_frames}")
    print(f"Wire efficiency: {wire_efficiency:.2f}%")
   
def convert_to_binary(string):
    return ' '.join(format(ord(x), '08b') for x in string)

def main():
    message = input("Enter message: ")
    try:
        window_size = int(input("Enter window size: "))
        if window_size <= 0:
            print("Invalid window size")
            return

        number_of_frames = len(message)
        if number_of_frames <= 0:
            print("Invalid message length")
            return

        protocol5(window_size, number_of_frames, message)

    except ValueError:
        print("Invalid input. Please enter integer values.")

if __name__ == "__main__":
    main()
