class Motor:
    def __init__(self, id: int, merk: str, model: str, engine_type: str):
        self.id = id
        self.merk = merk
        self.model = model
        self.engine_type = engine_type

    def to_dict(self):
        return {
            "id": self.id,
            "merk": self.merk,
            "model": self.model,
            "engine_type": self.engine_type
        }

    @staticmethod
    def from_dict(data: dict):
        return Motor(
            id=data["id"],
            merk=data["merk"],
            model=data["model"],
            engine_type=data["engine_type"]
        )
