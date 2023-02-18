class News:

    def __init__(self, id, title, content):
        self.id = id
        self.title = self.validate_title(title)
        self.content = self.validate_content(content)


    def validate_content(self, content):
        if len(content) < 10 or len(content) > 1000:
            raise TypeError(
                "Content must have least 10 letters and at most 1000 letters")
        return content

    def validate_title(self, title):
        if len(title) < 3 or len(title) > 30:
            raise TypeError(
                "title must have least 3 letters and at most 30 letters")
        return title

    def __str__(self) -> str:
        return f"{self.title}"

    def __repr__(self):
        return f"{self.title}"


if __name__ == "__main__":
    print(__file__)
