from ._entityindex import EntityIndex
from ._registry import Registry
import messages


class Cycle(Registry):
    def __init__(self):
        self.index = EntityIndex()
        self.running = True
        messages.requests.start_cycle.connect(self.start)
        messages.requests.end_cycle.connect(self.end)

    def start(self, e=None):
        messages.events.start_cycle.send(self)
        while self.running:
            messages.events.before_tick.send(self)
            self.tick()
            messages.events.after_tick.send(self)
        messages.events.end_cycle.send(self)

    def tick(self):
        for process in self.processes:
            process.setup()
  
    def stop(self, e=None):
        self.running = False
  
