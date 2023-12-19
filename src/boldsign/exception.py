class BoldsignError(Exception):
    def __init__(self, response):
        self.status = response.status_code
        self.message = self._parse_error(response)
        super().__init__(f"Error: HTTP Code {self.status}: {self.message}")

    @staticmethod
    def _parse_error(response):
        error_message = ""

        try:
            data = response.json()
            print("=========================")
            errors = data.get("errors", {})
            print(errors)
            for k, v in errors.items():
                if type(v) == list:
                    error_message += ' / '.join(v)
                else:
                    error_message += v
        except ValueError:
            print(response.headers)
            print(response.text)
            return response.text[:200]

