import anthropic


class ClaudeProvider:
    def __init__(self, api_key, model):
        self.client = anthropic.Anthropic(
            api_key=api_key
        )
        self.model = model

    def generate_video_idea(self):
        raise NotImplementedError()

    def generate_script(self, *args, **kwargs):
        raise NotImplementedError()