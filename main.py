import random

def protocol5(window_size, number_of_frames, message):
    message_after_received = ""
    failed_frames = 0  # Count the number of frames that fail to send
    total_sent_frames = 0  # Total frames sent, including retransmissions
    last_successful_frame = 0  # Tracks the last successfully sent frame
    if len(message) % 2 != 0:
        odd_size=1

    # Send the first set of frames in the window
    for j in range(1, min(window_size + 1, number_of_frames + 1)):
        frame_data = message[(j-1)*2:j*2]  # Get 2 characters for the frame
        print(f"Sending Frame {j}: Data: {frame_data}, Binary Representation: {convert_to_8bit_binary(frame_data)}")
        total_sent_frames += 1
        

    i = 1
    while i <= number_of_frames:
        for j in range(i, min(i + window_size, number_of_frames + 1)):
            random_result = random.randint(0, 1)  # Simulate frame sending success or failure
            if random_result:
                # Frame sent successfully
                print(f"Frame {j} sent successfully")
                frame_data = message[(j-1)*2:j*2]
                message_after_received += convert_to_8bit_binary(frame_data)
                last_successful_frame = j
                if j + window_size <= number_of_frames:
                    next_frame_data = message[(j + window_size - 1) * 2: (j + window_size) * 2]
                    print(f"Sending Frame {j + window_size}: Data: {next_frame_data}, Binary Representation: {convert_to_8bit_binary(next_frame_data)}")
                    total_sent_frames += 1
            else:
                # Frame failed, all frames in the current window are resent
                failed_frames += 1
                print(f"Frame {j} execution timeout")
                for k in range(j, min(j + window_size, number_of_frames + 1)):
                    frame_data = message[(k-1)*2:k*2]
                    print(f"Resending Frame {k}: Data: {frame_data}, Binary Representation: {convert_to_8bit_binary(frame_data)}")
                    total_sent_frames += 1
                break  # Exit to resend the current window
        i = last_successful_frame + 1  # Update i to the next frame to send

    # Calculate wire efficiency
    wire_efficiency = ((total_sent_frames - failed_frames) / total_sent_frames) * 100

    # Print the statistics after completion
    print("\nTransmission complete!")
    print(f"Received Message (binary): {message_after_received}")
    print(f"Decoded Message: {binary_to_text_8bit(message_after_received)}")
    print(f"Total frames sent (including retransmissions): {total_sent_frames}")
    print(f"Number of failed frames: {failed_frames}")
    print(f"Wire efficiency: {wire_efficiency:.2f}%")

def convert_to_8bit_binary(string):
    return ''.join(format(ord(char), '08b') for char in string)

def binary_to_text_8bit(binary_string):
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    text = ''.join(chr(int(char, 2)) for char in chars)
    return text

def main():
    message = input("Enter message: ")
    
    if len(message) % 2 != 0:
        message += ' '  # Add ' ' to make the length even

    number_of_frames = len(message) // 2  # frame consists of 2 characters

    try:
        window_size = int(input("Enter window size: "))
        if window_size <= 0:
            print("Invalid window size")
            return

        if number_of_frames <= 0:
            print("Invalid message length")
            return

        protocol5(window_size, number_of_frames, message)

    except ValueError:
        print("Invalid input. Please enter integer values.")

if __name__ == "__main__":
    main()