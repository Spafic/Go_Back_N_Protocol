import random
import time

def protocol5(window_size, number_of_frames):
    failed_frames = 0  # To count the number of frames that fail to send
    total_sent_frames = 0  # Total frames sent, including retransmissions
    last_successful_frame = 0  # Tracks the last successfully sent frame

    # Send the first set of frames in the window
    for j in range(1, min(window_size + 1, number_of_frames + 1)):
        print(f"Sending Frame {j}")
        total_sent_frames += 1

    i = 1
    while i <= number_of_frames:
        for j in range(i, min(i + window_size, number_of_frames + 1)):
            random_result = random.randint(0, 1)  # Simulate frame sending success or failure
            if random_result:
                # Frame sent successfully
                print(f"Frame {j} sent successfully")
                last_successful_frame = j
                if j + window_size <= number_of_frames:
                    print(f"Sending Frame {j + window_size}")
                    total_sent_frames += 1  # Increment for the next frame to be sent
            else:
                # Frame failed, all frames in the current window are resent
                failed_frames += 1
                print(f"Frame {j} execute timeout")
                for k in range(j, min(j + window_size, number_of_frames + 1)):
                    print(f"Resending Frame {k}")
                    total_sent_frames += 1  # Increment for retransmissions
                break  # Exit to resend the current window
        i = last_successful_frame + 1  # Update i to the next frame to send

    # Calculate wire efficiency
    wire_efficiency = ((total_sent_frames - failed_frames) / total_sent_frames) * 100

    # Print the statistics after completion
    print("\nTransmission complete!")
    print(f"Total frames sent (including retransmissions): {total_sent_frames}")
    print(f"Number of failed frames: {failed_frames}")
    print(f"Wire efficiency: {wire_efficiency:.2f}%")

def main():
    try:
        window_size = int(input("Enter window size: "))
        if window_size <= 0:
            print("Invalid window size")
            return

        number_of_frames = int(input("Enter number of frames to be sent: "))
        if number_of_frames <= 0:
            print("Invalid number of frames")
            return

        protocol5(window_size, number_of_frames)

    except ValueError:
        print("Invalid input. Please enter integer values.")

if __name__ == "__main__":
    main()
