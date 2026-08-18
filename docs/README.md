# KuzeyOS

KuzeyOS is a local-first automation, computer vision and AI platform designed to connect home automation, edge devices, local artificial intelligence and robotics under a single system.

## Current Modules

### KuzeyOS Node

Central web and coordination layer.

Current responsibilities include:

- Web dashboard
- Face AI integration
- Sensor registry
- Occupancy state
- Event handling
- System state management
- UI settings
- Edge service integration

Source:

`kuzeyos-node/`

### Face AI

Dedicated local computer vision node.

Current features include:

- YuNet face detection
- SFace face recognition
- Face tracking
- Camera streaming
- Person enrollment
- Recognition events
- KuzeyOS Node integration

Source:

`face-ai/`

Biometric data, face photographs, embeddings and runtime event data are intentionally excluded from this repository.

## Architecture

```text
User
  |
  v
KuzeyOS Node
  |
  +--> Face AI
  |
  +--> Future Local AI
  |
  +--> Home Assistant / Node-RED
  |
  +--> PLC / Robotics
