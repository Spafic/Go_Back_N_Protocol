# Network Transmission Protocol Simulation

## Protocol 5 Sliding Window Transmission Simulator

### Overview
This Python script simulates a network transmission protocol using a sliding window technique, demonstrating frame transmission, error handling, and wire efficiency calculation.

### Diagram

![Sliding Window Protocol](./assets/GoBackN_protocol.png)


### Features
- Simulates network frame transmission with potential frame failures
- Implements sliding window protocol
- Calculates wire efficiency
- Provides detailed transmission statistics
- Converts messages to binary representation
- Handles dynamic window sizes

### Installation

#### Prerequisites
- Python 3.8+
- `random` module (standard library)

#### Clone Repository
```sh
git clone https://github.com/Spafic/Go_Back_N_Protocol.git
cd Go_Back_N_Protocol
```

#### Install Dependencies
No additional dependencies are required as the script uses Python's standard library.

#### Run the Simulator
```sh
python main.py
```

#### Example
```sh
Enter message: Hello
Enter window size: 3
```

#### User Inputs
1. Message to transmit
2. Window size for transmission

> [!NOTE]
> **Example Workflow**
> 
> ```sh
> Enter message: Hello
> Enter window size: 3
> ```

### Protocol Mechanics
- Dynamically sends frames based on window size
- Randomly simulates frame transmission success/failure
- Supports automatic retransmission of failed frames
- Tracks and reports transmission efficiency

### Output Details
- Received message
- Binary representation
- Total frames sent
- Failed frames
- Wire efficiency percentage

### Simulation Characteristics
- Random frame transmission success
- Sliding window frame management
- Adaptive retransmission strategy

### Contributing
1. Fork the repository
2. Create your feature branch (git checkout -b feature/YourFeatureName)
3. Commit your changes (git commit -m 'Add YourFeatureName')
4. Push to the branch (git push origin feature/YourFeatureName)
5. Open a Pull Request

### Inspiration
This project demonstrates fundamental concepts in network transmission protocols, specifically the sliding window technique used in data communication.

### License
This project is licensed under the MIT License. See the [MIT LICENSE](./LICENSE) file for more details.