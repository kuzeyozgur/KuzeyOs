# KuzeyOS

> **Public Showcase Repository**
>
> This repository is a **public showcase and architecture reference** for KuzeyOS.
>
> It is **not the production source-code repository** and does **not** contain the complete source code used by the live KuzeyOS system.
>
> Production code, credentials, private network configuration, biometric data, privileged system-control logic and other sensitive implementation details are intentionally excluded.

---

## What is KuzeyOS?

KuzeyOS is a local-first automation, computer vision and AI platform designed around distributed edge services.

The system is being developed to connect:

* Home automation
* Computer vision
* Local artificial intelligence
* Edge devices
* Sensors
* Future PLC control
* Future robotics systems

under a unified architecture.

---

## Purpose of This Repository

This repository exists to:

* Showcase the KuzeyOS project
* Explain the system architecture
* Demonstrate selected implementation concepts
* Document design decisions
* Present safe example code
* Help others understand how the system is structured

This repository should **not** be treated as a complete build of the production KuzeyOS system.

---

## Repository Structure

```text
KuzeyOs/
├── showcase/
│   ├── kuzeyos-node/
│   └── face-ai/
│
├── docs/
│   └── Architecture and technical documentation
│
├── README.md
└── .gitignore
```

---

# Showcase Components

## KuzeyOS Node Showcase

Location:

`showcase/kuzeyos-node/`

This directory demonstrates selected concepts used by the KuzeyOS Node architecture.

Examples include:

* Web application structure
* Dashboard concepts
* Event APIs
* Device representation
* Edge-service integration
* Example configuration
* Frontend structure

The real production KuzeyOS Node contains additional private functionality that is **not included** in this repository.

---

## Face AI Showcase

Location:

`showcase/face-ai/`

This directory demonstrates selected concepts from the KuzeyOS Face AI architecture.

The production Face AI system uses technologies such as:

* YuNet face detection
* SFace face recognition
* Local camera processing
* Face tracking
* Recognition events
* Person enrollment
* Edge-to-Core communication

The public showcase does **not** contain:

* Real face photographs
* Face embeddings
* Recognition galleries
* Personal identity data
* Runtime recognition state
* Event snapshots

---

# Current Production Components

The current KuzeyOS environment includes:

* KuzeyOS Node
* Face AI

These production systems run separately from this public showcase repository.

The public repository does not mirror the full live deployment.

---

# Coming Soon

The following components are planned for future KuzeyOS development.

## KuzeyOS Local AI

Planned local AI operator layer.

Future concepts include:

* Local LLM inference
* Natural-language interaction
* Context-aware commands
* Device Registry
* Structured actions
* Permission-controlled device operations
* Local memory
* Event interpretation

---

## Home Assistant Integration

Planned smart-home integration layer for standardized device control and entity management.

---

## Node-RED Integration

Planned automation and workflow layer for KuzeyOS events and integrations.

---

## Authentication and Permissions

Planned unified authentication system including:

* Login
* Secure sessions
* User accounts
* Role-based permissions
* Restricted administrative actions

---

## PLC Control

**Coming Soon**

PLC integration is planned for future physical infrastructure and electrical-control use cases.

PLC functionality is not currently included as an active production module in this showcase.

Critical safety and interlock logic will remain outside unrestricted AI control.

---

## Moveo Robotics

**Coming Soon**

Moveo robotic-arm integration is planned as a future KuzeyOS robotics module.

Planned concepts include:

* Joint control
* Real-time state feedback
* Motion sequences
* Timeline / keyframe control
* 3D digital twin
* Automation integration

Moveo is not currently an active production component.

---

# High-Level Architecture

```text
                     User
                       |
                       v
                +-------------+
                |  KuzeyOS    |
                |    Node     |
                +------+------+
                       |
             +---------+---------+
             |                   |
             v                   v
        +---------+          +---------+
        | Face AI |          | Future  |
        |  Edge   |          | AI Core |
        +---------+          +----+----+
                                  |
                           +------+------+
                           |             |
                           v             v
                    Home Assistant    Node-RED
                           |
                           v
                     Smart Devices

                    Future Extensions
                           |
                  +--------+--------+
                  |                 |
                  v                 v
                 PLC             Moveo
```

---

# Design Principles

KuzeyOS is being developed around several principles:

* Local-first processing
* Privacy-aware architecture
* Distributed edge computing
* Minimal cloud dependency
* Modular services
* Controlled AI actions
* Independent hardware nodes
* Centralized user experience
* Separation between public showcase code and production implementation

---

# Security and Privacy

Sensitive production information is intentionally excluded from this repository.

This repository does **not** contain:

* Production passwords
* API tokens
* MQTT credentials
* SSH private keys
* Authentication secrets
* Real private-network topology
* Production filesystem paths
* Face photographs
* Face embeddings
* Recognition galleries
* Runtime databases
* Event snapshots
* Private configuration files
* Complete privileged system-control implementation
* Complete production administrative functionality

Example values and synthetic data may be used when necessary to explain the architecture.

---

# Source Code Notice

**The complete KuzeyOS production source code is not publicly available in this repository.**

Files inside `showcase/` are simplified reference implementations and examples intended to demonstrate selected concepts.

They should not be assumed to be identical to the code running on the live KuzeyOS environment.

---

# Project Status

KuzeyOS is under active development.

### Active

* KuzeyOS Node
* Face AI

### Planned / Coming Soon

* Local AI Operator
* Device Registry
* Context Manager
* Home Assistant integration
* Node-RED integration
* Authentication and permissions
* Friendly local domain / reverse proxy
* PLC control
* Moveo robotics

---

## Disclaimer

KuzeyOS is an experimental personal technology project.

This repository is provided primarily for demonstration, documentation and architectural reference purposes.
