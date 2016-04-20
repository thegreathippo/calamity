from ._entityindex import EntityIndex
from ._registry import Registry
import blinker


class Cycle(Registry):
  def __init__(self):
    self.world = EntityIndex()
    self.running = True
    blinker.signal("start").connect(self.start)
    blinker.signal("stop").connect(self.stop)
    self.start()

  def start(self, e=None):
    blinker.signal("starting").send(self)
    while self.running:
      self.tick()
    blinker.signal("stopping").send(self)
  
  def tick(self):
    for process in self.processes:
      process.setup()
  
  def stop(self, e=None):
    self.running = False
  
