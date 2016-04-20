class BaseProcess:
  priority = 0
  required = {}

  def start(self):
    pass

  def setup(self):
    pass
  
  def execute(self, entity):
    pass
  
  def teardown(self):
    pass
  
  def end(self):
    pass


class Registry:
  def __init__(self):
    self.processes = list()

    class ProcessType(type):
      def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        self.processes.append(cls())
        self.processes.sort(key=lambda p: p.priority)
        return cls

    self.Process = ProcessType("Process", (BaseProcess,), dict())

