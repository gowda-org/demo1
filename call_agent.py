class AgenticAI:
    def connect(self):
        pass

    def run_task(self, task):
        print(task)

    class Session:
        def disconnect(self):
            pass

    @property
    def session(self):
        return self.Session()

agent = AgenticAI()
agent.connect()
agent.run_task("summarize customer chat")
agent.session.disconnect()
