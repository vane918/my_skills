# Source Analysis Guide

Use this guide to build a grounded architecture model before producing diagrams.

## Input Discovery

Start with user-provided Markdown files, then inspect code and configuration:

- Documentation: `README*`, `docs/**`, architecture/design/spec Markdown, ADRs.
- Build and package metadata: `CMakeLists.txt`, `package.xml`, `setup.py`, `pyproject.toml`, `build.gradle*`, `settings.gradle*`, `AndroidManifest.xml`.
- Runtime entry points: `main.*`, node constructors, app/activity/service classes, launch files, container composition, dependency injection setup.
- Interface definitions: ROS 2 `msg/`, `srv/`, `action/`, IDL, Protobuf, OpenAPI, WebSocket schemas, REST clients, CAN frame definitions.
- Configuration: `launch/**`, `config/**`, YAML/TOML/JSON env/config files, calibration files, parameters.
- Tests and examples: integration tests, simulation launch files, demo scripts.

## Evidence Model

For each significant claim, capture:

- Component: exact name and type.
- Responsibility: one sentence.
- Evidence: file path and symbol/config/doc section.
- Interfaces: inputs, outputs, protocols, topics, services, APIs, callbacks, files, devices.
- Runtime boundary: process, node, thread, board, container, package, module, library, or external service.
- Confidence: confirmed, inferred, or unknown.

Use this compact table shape in the report:

```markdown
| Component | Responsibility | Inputs | Outputs | Evidence |
|---|---|---|---|---|
| `planner_node` | Creates navigation plans | `/goal_pose` | `/cmd_path` | `src/planner_node.cpp`, `launch/nav.launch.py` |
```

## Relationship Extraction

Infer relationships from concrete signals:

- Constructor wiring, dependency injection, imports/includes, function calls.
- ROS 2 publishers, subscribers, services, clients, actions, parameters, TF frames.
- JNI bindings, native method registration, shared library loading, Android services.
- Network clients/servers, ports, endpoints, topics, streams, sockets.
- Database/file/cache access, shared queues, event buses, worker pools.
- Launch files, manifests, composition containers, Gradle/CMake dependencies.

Avoid using directory nesting alone as proof of runtime communication.

## Robotics-Specific Checks

When the project is a ROS 2 or robot system, explicitly look for:

- Board/deployment split, for example Android RK3588S versus Ubuntu/ROS 2 AGX Orin.
- Node graph, topics, services, actions, parameters, lifecycle nodes, and QoS where visible.
- Sensor and actuator data paths.
- Localization, mapping, planning, control, perception, task/business layers.
- Hardware buses such as CAN, serial, USB, RTSP cameras, IMU, lidar, motor drivers.
- Simulation versus real-robot paths.

## Analysis Stop Condition

Stop reading when you can confidently answer:

- What are the main runtime components?
- What data/control flows between them?
- Which components own core decisions?
- What are the highest-value flows and sequences to diagram?
- What remains uncertain and should be listed as a verification gap?
