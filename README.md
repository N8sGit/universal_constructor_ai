# Universal Constructor Multi-Agent Model

Welcome to the Universal Constructor Multi-Agent Model experiment. The project is inspired by mathematician  [John von Neumann's Universal Constructor cellular automaton](https://en.wikipedia.org/wiki/Von_Neumann_universal_constructor). A UC is essentially a theoretical machine that is capable of self-replication and can also construct any other machine. In the case of this project, the objective is a "program that can construct any other program (including itself)". Although admittedly in its current incarnation it's more of a toy meant to get the intellectual juices flowing.

Self-replicating code isn't actually very useful in practice, granted that it doesn't do anything else but perfectly copy itself. The real interest would be in a system that can self-modify and self-extend its code autonomously. To do so it may have to self-replicate, since it would have to send a serialized snapshot of itself through an encoder, add in new code at various points, and then somehow redeploy, all while remaining stable. At least that's one implementation of it I can imagine. But self-modifying code that runs in real-time without instantly crashing sounds like an unheard of feat of engineering. 

It's built using CrewAI's multi-agent system. Why?

I personally believe the theoretical boundary pushes of AI research are to be found in concepts such as self-reference and self-reflection. A multi-agent paradigm doesn't quite fit this picture, although it does fit Minsky's Society of Mind's modular view of intelligence, which proposes that the mind is not a single, unified entity but rather a collection of smaller, simpler processes or “agents” that work together to create the overall effect of intelligence. So, you would have, for example, a conjecture agent, a reflection (or critic) agent, an information gathering sensor agent, a coordinating executive agent, and so on.

The Universal Constructor is not necessairly a cognitive model, but it plays with these ideas in a way that could stimulate further investigation.

## What it does 
 Ask it for a program. It will try writing it. The files will be written to ``/constructor_outputs``

## What I would like it to do
Print out a better version of its own code and use it for the next iteration. 

## Some notes of interest:

- One interesting feature of this codebase is the instruction tape generator agent. This I talked into generating a structured "DNA sequence" for a program, which is a JSON-like nested dictionary of schematic details of various programming components that could serve as the basis of an evolutionary programming paradigm . It then feeds this schematic to the manipulator agent, (aka the programmer). I can't tell if this leads to better results but one could see how it might. Every program it writes gets a neatly organized specification so the programming agent isn't starting from scratch but has a relatively "thought out" sequence to work from. 

- Ideally I could figure out how to successively modify this copies of this "DNA sequence" of a program over a series of trials.

- Process style is hierarchical. This is effectively the "coordinate construction task", except it is removed from the task list:

```bash
coordinate_construction_task:
  description: >
    Read the blueprint and manage the construction sequence by delegating tasks to other agents.
    Ensure that all agents work in the proper order and that the construction process runs smoothly.
  expected_output: >
    A fully coordinated construction process with clear instructions sent to the manipulator_agent and resource_handler_agent.
  agent: control_unit_agent
  ```

- At first I thought resource collector agent wouldn't have much of a use in a digital context. UC's were initially meant to work for physical materials and there's no digital analogue to material collection. I want to keep the same spirit of von Neumann's original vision even if much of it is impractical for a code generator (and notoriously unperformant). But to my suprise it was basically a QA agent, collecting libraries to provide to the manipulator agent (the programmer) and in one instance finding a securer alternative to the exploitable eval() method for a calculator app. 

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/universal_constructor/config/agents.yaml` to define your agents
- Modify `src/universal_constructor/config/tasks.yaml` to define your tasks
- Modify `src/universal_constructor/crew.py` to add your own logic, tools and specific args
- Modify `src/universal_constructor/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```
or
```bash
poetry run universal_constructor
```

This command initializes the universal_constructor Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The universal_constructor Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.
