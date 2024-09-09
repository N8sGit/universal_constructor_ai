from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool, CodeInterpreterTool


@CrewBase
class UniversalConstructorCrew:
    """UniversalConstructor crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    file_writer_tool = FileWriterTool()
    code_interpreter_tool = CodeInterpreterTool()

    @staticmethod
    def python_argument_formatter(args):
        print(f"Formatting args: {args}")
        return f"file_writer_tool._run(filename={args['filename']}, content={args['content']}, directory={args['directory']}, overwrite={args['overwrite']})"

    @agent
    def instruction_tape_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['instruction_tape_agent'],
            verbose=True,
            planning=True
        )

    @agent
    def duplicator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['duplicator_agent'],
            verbose=True,
            model_name='chatgpt-4o-latest',
            # Taking these offline until I can figure out why the file_writer_tool won't trigger
            # allow_code_execution=True,
            # tools=[self.code_interpreter_tool, self.file_writer_tool],
            action_formatter=self.python_argument_formatter
        )

    @agent
    def manipulator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['manipulator_agent'],
            verbose=True,
            allow_code_execution=True,
            tools=[self.code_interpreter_tool]
        )

    @agent
    def resource_handler_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['resource_handler_agent'],
            verbose=True,
        )

    @agent
    def output_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['output_agent'],
            verbose=True,
            allow_code_execution=True,
            tools=[self.file_writer_tool]
        )
    
    @agent
    def control_unit_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['control_unit_agent'],
            verbose=True,
            planning=True,
            allow_delegation=True,
        )

    @task
    def retrieve_blueprint_task(self) -> Task:
        return Task(
            config=self.tasks_config['retrieve_blueprint_task'],
        )

    @task
    def duplicate_blueprint_task(self) -> Task:
        return Task(
            config=self.tasks_config['duplicate_blueprint_task'],
        )

    @task
    def build_machine_task(self) -> Task:
        return Task(
            config=self.tasks_config['build_machine_task'],
        )

    @task
    def gather_materials_task(self) -> Task:
        return Task(
            config=self.tasks_config['gather_materials_task'],
        )

    @task
    def deploy_machine_task(self) -> Task:
        return Task(
            config=self.tasks_config['deploy_machine_task'],
            output_file='deployment.log',
            human_input=True
        )

    @crew
    def crew(self) -> Crew:
        """Creates the UniversalConstructor crew"""
        return Crew(
            agents=[
                self.instruction_tape_agent(),
                self.duplicator_agent(),
                self.manipulator_agent(),
                self.resource_handler_agent(),
                self.output_agent(),
            ],
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_agent=self.control_unit_agent(),
        )